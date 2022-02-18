# Predicting College Football Outcome (Win/Lose) Based on First-Half Statistics

## Goals

•	Can a game be predicted win/lose based on first-half stats, and to what level of accuracy?

•	How close does predicted meet actual results?

•	What values contribute most heavily to the predicted outcome?

•	What other values may contribute to win/lose?

•	Is the model used in machine learning the best model for this exercise?

## Data Selection and Exploration
We started exploring the databases availiable on collegefootballreference.com, beginning options included analyzing the economic impact of sports games. This idea eventually evolved into prediciting the outcomes of college games based on the scores at the half. We chose this dataset because the entire team was interested and could relate to college football statistics. Our dataset came from Kaggle (https://www.kaggle.com/mhixon/college-football-statistics) datasets for use included game statistics from 2005-2013, details on stadiums and conferences. In addition, there is an expansive capability to bring in additional data that may contribute to outcome and subsequent visual representation and interaction to a user interested in predicting game outcomes at the half.

## Database Building and Cleaning
Databases for the project were built in Postgres and SQLite with multiple Kaggle .csv files joined to create the ‘Gold’ database for machine learning and visualization integration. We also decided we were only going to use the data from 2008-2013 as the timeframe provided enough records for baseline prediction (>3k) and would keep the data relevant to current games without burdening the database. 

## Machine Learning
We started with removing games that we considered "blow outs" - any games that had teams that were leading by greater than 14 points at the half. Not only are these games much easier to predict, their presence in the data may unduly influence the fit, as well as the fact that these types of games are typically between teams that are not evenly matched.
We then removed features from the dataframe that are used for identification purposes such as game code"game_code", team names, conference names, team codes, and stadiums names, as they should have no influence in the model. <br />
We used train_test_split from the skilearn library to split our data into training and testing groups, utilizing a training size of 25 percent of the full data set. This proportion was determined via trial-and-error to give better accuracy in predicting the testing data.<br />
Our machine learning model was based on a logistic regression that was created via python using Google Colab. A logistic regression model was chosen for several reasons:<br />
* it is useful for binary classification (team A or team B wins)
* the simplicity of the fucntion enables coefficients to be outputted and studied (i.e. no "black box" model)
* the simplicity of the model also allows a closed-form of the prediction function to be written, which can then easily be read into other scripts (visualization) and used for plotting
* initial models produced a 74 percent accuracy<br />

After an initial model which utlized all the available features, we tested the singular contribution of each feature by removing it and re-training the model.  After dropping uneeded features, we achieved a balanced model accuracy of roughly 74 percent.<br />


## Dashboard
The dashboard is presently a webpage that has an interactive model to predict future game outcomes, the second page is an interactive menu where you can select up to three teams and compare their statistics from the initial dataset. 


### Week Three Deliverables
Brain: google slides, review other machine learning models
Lauren: data modification for dash app and flask apps
Ben: complete flask application
Ambrea: complete dashboard appication and being deploying to heroku

### Google Slides
https://docs.google.com/presentation/d/17MsOsjI0Ukt9Tt1H7SNCW1TySk2Vdx8QivNd-x8_eVk/edit#slide=id.gcb9a0b074_1_140

