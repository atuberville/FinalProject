# The getWinner Function using parameters and features
# from the college_football_ml_oneTeam_Final.ipynb code
from math import exp
import pandas as pd

# Read in the coefficients from the csv
fileName='/Users/benpeyton/Desktop/Project 20/Interactive/coefs.csv'
coefs_df=pd.read_csv(fileName)
coefs=coefs_df.iloc[0].values.tolist()

# define the function
def getWinner(a_points, b_points, a_offense_rush_yards, b_offense_rush_yards,
    a_offense_pass_yards, b_offense_pass_yards, \
    a_incomplete_pass, b_incomplete_pass, \
    a_penalty_yards, b_penalty_yards, b_home):
    
    r1=a_points, b_points, a_offense_rush_yards, b_offense_rush_yards,         a_offense_pass_yards, b_offense_pass_yards, a_incomplete_pass, b_incomplete_pass, a_penalty_yards, b_penalty_yards, b_home
    
    index=0
    linearSum=0
    for value in r1:
        linearSum = linearSum + value*coefs[index]
        index = index+1
    sigmoid=int(round(1/(1+exp(-1*linearSum)),0))
    return sigmoid




