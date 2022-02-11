# Import Dependencies
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from pathlib import Path
from collections import Counter

# Read CSV
df = pd.read_csv('/Users/benpeyton/Desktop/vandy_boot_camp/Module_20/20-Final_Project/goldcopyhalfstats.csv')
df.head()

# Create empty team lists
aHome=[]
bHome=[]

# Neutral game string
neutral=str(df.iloc[1]['site'])

for index,row in df.iterrows():
  gameCode=str(row['game_code'])
  aTeam=str(row['a_team_code'])
  bTeam=str(row['b_team_code'])
  site=str(row['site'])

  homeTeam=''
  try:
    i1=gameCode.index(aTeam)
  except ValueError:  # For when a team code isn't in game code
    homeTeam='NOT IN CODE'
  try:
    i2=gameCode.index(bTeam)
  except ValueError:  # For when a team code isn't in game code
    homeTeam='NOT IN CODE'

  if(homeTeam==''):
      if(site==neutral):
        aHome.append(0)  # Neutral Field Game
        bHome.append(0)
      elif (i1>i2):      
        aHome.append(1)  # The aTeam team code was second  
        bHome.append(0)   
      else:
        aHome.append(0)  
        bHome.append(1)  # The aTeam team code was second
  else:
      # One of the teams did not have its team code in the game code
      if(index < 150):
        print(index)
      aHome.append(0)  # Neutral Field Game
      bHome.append(0)

df['a_home']=aHome
df['b_home']=bHome

df.head()

# Drop the null columns where all values are null
df2 = df.dropna(axis='columns', how='all').copy()

# Drop the null rows
df2 = df2.dropna()

df2.reset_index(inplace=True, drop=True)

print(len(df2))
df2.head(10)

df3=df2.copy()
df3["result"]=df3['a_result']
df3=df3.drop(['a_result', 'b_result'], axis=1)

df3=df3.drop(['a_defense_rush_yards','b_defense_rush_yards','a_defense_pass_yards','b_defense_pass_yards'],axis=1)

df3.head()


# Filter Data
df_filter=df3.copy()

# Throw out "blowout" games
blowoutThresh=14
df_filter=df_filter[df_filter['half_diff_score_abs'] <= blowoutThresh]

# reset index
df_filter.reset_index(inplace=True, drop=True)

print(len(df_filter))
df_filter.head(5)

df_filter.columns


# Split into testing and training data and scale
# Create our features
X = df_filter.copy()

X=X.drop({'year', 'game_code', 'a_team_name', 'a_name_conference', 'a_team_code',
          'b_team_code', 'team_name', 'name_conference','half_leader',
          'half_diff_score', 'half_diff_score_abs', 'visit_date', 'stadium_code',
          'stadium_name', 'site', 'city', 'state', 'capacity',
          'year_opened', 'result'},axis=1)

# Need to convert columns with strings to numeric
# Get column names that are non-numeric
column_names=X.select_dtypes(exclude=[np.number]).columns
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for columnName in column_names:
  X[columnName]=le.fit_transform(X[columnName])

# Create our target
y = df_filter['result'].copy()

X.head()

# Check the balance of our target values
print(len(X))
abs(X['a_points']-X['b_points']).value_counts()


# Sampling Methods and Scale
from sklearn.model_selection import train_test_split

# stratify by point spread
stratify_values=abs(df_filter['a_points']-df_filter['b_points'])
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    stratify=stratify_values, 
                                                    test_size=0.25)


# Models
# Import Dependencies
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.metrics import balanced_accuracy_score
from imblearn.metrics import classification_report_imbalanced

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


# Logistic Regression
classifier = LogisticRegression(solver='lbfgs',
                                max_iter=1500,
                                random_state=42)

#result=classifier.fit(X_train_scaled, y_train)
result=classifier.fit(X_train, y_train)

ml_df=pd.DataFrame(columns=X.columns.tolist())

log_coefs=list(zip(X.columns.tolist(),
                   result.coef_.tolist()[0]))
log_coefs.sort(key = lambda x:abs(x[1]),reverse=True)
print(log_coefs)

y_pred = classifier.predict(X_test)
results = pd.DataFrame({"Prediction": y_pred, "Actual": y_test}).reset_index(drop=True)
print(classifier.get_params())
results.head(10)

logRegAcc=balanced_accuracy_score(y_test, y_pred)
noDroplogRegAcc=logRegAcc
print('balanced accuracy score = ',logRegAcc)

# Display the confusion matrix
# Calculating the confusion matrix.
cm = confusion_matrix(y_test, y_pred)

# Create a DataFrame from the confusion matrix.
cm_df = pd.DataFrame(
    cm, index=["Actual B", "Actual A"], columns=["Predicted B", "Predicted A"])

print("")
print(cm_df)

# Print the imbalanced classification report
print("")
print(classification_report_imbalanced(y_test, y_pred))


# Sensitivity Test
# We will drop each column and see what the balanced score gives us
X.columns
print('No Drop Balanced Accuracy = ',round(noDroplogRegAcc,2))
for column in X.columns:
  #Creata new Dataframe with dropped column
  Xtest=X.drop(column,axis=1).copy()

  # Gotta train, test, split using same random seed
  # stratify by point spread
  stratify_values=abs(df_filter['a_points']-df_filter['b_points'])
  X_train, X_test, y_train, y_test = train_test_split(Xtest, y,
                                                    stratify=stratify_values, 
                                                    test_size=0.3)

  # ML with logistic Regression
  classifier = LogisticRegression(solver='lbfgs',
                                max_iter=2500,
                                random_state=42)

  #result=classifier.fit(X_train_scaled, y_train)
  result=classifier.fit(X_train, y_train)
  y_pred = classifier.predict(X_test)
  logResAcc=balanced_accuracy_score(y_test, y_pred)

  print('Dropped ',column,', balanced acc. = ',round(logResAcc,2))


# Drop Unneeded Features**
Xnew=X.drop({'a_pass','b_pass',
             'a_rush','b_rush',
             'a_penalty','b_penalty',
             'surface',
             'a_home'
            },axis=1).copy()


# Gotta train, test, split using same random seed
# stratify by point spread
stratify_values=abs(df_filter['a_points']-df_filter['b_points'])
X_train, X_test, y_train, y_test = train_test_split(Xnew, y,
                                                    stratify=stratify_values, 
                                                    test_size=0.25)

# ML with logistic Regression
classifier = LogisticRegression(solver='lbfgs',
                                max_iter=2500,
                                random_state=42)

#result=classifier.fit(X_train_scaled, y_train)
result=classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
logResAcc=balanced_accuracy_score(y_test, y_pred)
print('Old Balanced Accuracy = ',round(noDroplogRegAcc,2))
print('New Balanced Accuracy = ',round(logResAcc,2))

# Create Dataframe with fit coefficients and print to file
coefficients=result.coef_.tolist()[0]
coef_df=pd.DataFrame()
i=0;
for feature in Xnew.columns:
  coef_df[feature]=[coefficients[i]]
  i=i+1
coef_df

# Create Dataframe with fit coefficients and print to file
coefficients=result.coef_.tolist()[0]
coef_df=pd.DataFrame()
i=0;
for feature in Xnew.columns:
  coef_df[feature]=[coefficients[i]]
  i=i+1
print(coef_df)

coef_df.to_csv('coefs.csv',index=False)


y_pred = classifier.predict(X_test)
results = pd.DataFrame({"Prediction": y_pred, "Actual": y_test}).reset_index(drop=True)
print(classifier.get_params())

results.head(10)

logRegAcc=balanced_accuracy_score(y_test, y_pred)
noDroplogRegAcc=logRegAcc
print('balanced accuracy score = ',logRegAcc)

# Display the confusion matrix
# Calculating the confusion matrix.
cm = confusion_matrix(y_test, y_pred)

# Create a DataFrame from the confusion matrix.
cm_df = pd.DataFrame(
    cm, index=["Actual B", "Actual A"], columns=["Predicted B", "Predicted A"])

print("")
print(cm_df)

# Print the imbalanced classification report
print("")
print(classification_report_imbalanced(y_test, y_pred))

X.mean()

# Flatten data
import pickle

# Saving model to current directory
pickle.dump(result, open('model.pkl','wb'))

#Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

