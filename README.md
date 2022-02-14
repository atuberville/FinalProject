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
Our machine learning model was based on a logistic regression. We started with removing games that we considered ‘blow outs’ any games that had teams that were leading by greater than 14 points at the half. Logistic regression is the choosen method for analysis, with the ultimate goal being to integrate this model into a fully functioning flask app that will be used to predict future games.

## Prediction Application


## Dashboard
The dashboard is presently a draft where you can select three teams in to compare their first half stats among teams (app2.py). The second companent will be a general overview of statistics for your single selected team (app.py).

### Week two completed itesms
Brain: update machine learning module with new .csv
Lauren: further data cleaning and starting Google Sheets powerpoint
Ben: integration of prediction Flask app
Ambrea: draft of dashboard application via dash app

### Week Three Deliverables
Brain: google slides, review other machine learning models
Lauren: data modification for dash app and flask apps
Ben: complete flask application
Ambrea: complete dashboard appication and being deploying to heroku

