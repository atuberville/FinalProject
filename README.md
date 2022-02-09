# Predicting College Football Outcome (Win/Lose) Based on First-Half Statistics

## Goals

•	Can a game be predicted win/lose based on first-half stats, and to what level of accuracy?

•	How close does predicted meet actual results?

•	What values contribute most heavily to the predicted outcome?

•	What other values may contribute to win/lose?

•	Is the model used in machine learning the best model for this exercise?

## Data Selection
We chose this dataset because the entire team was interested and could relate to college football statistics. Our dataset came from Kaggle (https://www.kaggle.com/mhixon/college-football-statistics) datasets for use included game statistics from 2005-2013, details on stadiums and conferences. In addition, there is an expansive capability to bring in additional data that may contribute to outcome and subsequent visual representation and interaction to a user interested in predicting game outcomes at the half.

## Database Building and Cleaning
Databases for the project were built in Postgres and SQLite with multiple Kaggle .csv files joined to create the ‘Gold’ database for machine learning and visualization integration. We also decided we were only going to use the data from 2008-2013 as the timeframe provided enough records for baseline prediction (>3k) and would keep the data relevant to current games without burdening the database. 

## Machine Learning
Our machine learning model was based on a logistic regression. We started with removing games that we considered ‘blow outs’ any games that had teams that were leading by greater than 14 points at the half. Presently we are using a trial-and-error method to determine which features are the most relevant for predicting. 


### Week one task owners
 ![image](https://user-images.githubusercontent.com/89363928/152465855-052d485b-cd72-4e63-8e38-79516f940003.png)

### Primary Communication Methods
Tuesday/Thursday are our status meetings where we will answer 

•	What have we done since we last met

•	What are we going to accomplish by the time we meet again 

•	We will communicate via Slack for times in between

### Conflict Management
Owner of the task listed above will ultimately decide how to proceed. As a team we will try to negotiate a solution that works for all parties if there is a project conflict. If there is interpersonal conflict it is recommended that the persons with issues take some time offline to try to resolve specific items in question

