from tkinter import N
from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import NUMERIC, TEXT, VARCHAR, Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#def Load_Data(goldcopyhalfstats):
    #data = genfromtxt(goldcopyhalfstats, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    #return data.tolist()

#Base = declarative_base()

#class initial_model_input(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
   # __tablename__ = 'initial_model_input'
    #__table_args__ = {'sqlite_autoincrement': True}
    #tell SQLAlchemy the name of column and its attributes:
    #id = Column(Integer, primary_key=True, nullable=False) 
    #a_points = Column(NUMERIC)
    #b_points = Column(NUMERIC)
    #a_offense_rush_yards = Column(NUMERIC)
    #b_offense_rush_yards = Column(NUMERIC) 
    #a_penalty_yards = Column(NUMERIC)
    #b_penalty_yards = Column(NUMERIC)
    #surfaceint = Column(NUMERIC)
    #b_home = Column(NUMERIC)

    
#if __name__ == "__main__":
    #t = time()

    #Create the database
engine = create_engine('sqlite:///initial_model_input.sqlite')
    #Base.metadata.create_all(engine)

    #Create the session
    #session = sessionmaker()
    #session.configure(bind=engine)
    #s = session()

    
    #file_name = "goldcopyhalfstats.csv"
    #data = Load_Data("goldcopyhalfstats.csv") 

#for i in data:
            #record = initial_model_input(**{
                #'a_points' : i[6],
                #'b_points' : i[11],
                #'a_offense_rush_yards': i[15],
                #'b_offense_rush_yards' : i[18],
                #'a_penalty_yards' : i[29],
                #'b_penalty_yards' : i[30],
                #'surfaceint' : i[43],
                #'b_home' : i[34]
           # })
           # s.add(record) #Add all the records
           # s.commit() #Attempt to commit all the records

#engine.execute(
    #'''
        #ALTER TABLE initial_model_input ADD column result INTEGER 
             #''')
#engine.execute(
    #'''
        #ALTER TABLE initial_model_input ADD column username VARCHAR(10) 
             #''')
             
          #a_score_input = input("Team A's halftime score")
#user_input_list = [a_score_input]
#with open('test.csv') as file:
    #rows = csv.reader(file, delimiter=',')
    #list_of_rows = [row for row in rows]
    #list_of_rows.pop(0)
    #for row in list_of_rows:
        #row = tuple(row)
        #engine.execute(f'''
               #INSERT INTO user_input
               #(username,
                #a_points,
                #b_points,
                #a_offense_rush_yards,
                #b_offense_rush_yards,
                #a_incomplete_pass,
                #b_incomplete_pass,
                #a_penalty,
                #b_penalty,
                #a_penalty_yards,
                #b_penalty_yards,
                #surface,
                #b_home,
                #result)
               #VALUES {row}
               #''')
        
#'a_points', 'b_points', 'a_offense_rush_yards', 'b_offense_rush_yards',
#       'a_penalty_yards', 'b_penalty_yards', 'surface', 'b_home'
# list_of_inputs = ('last_one', 45,33,123,100,12,45,65,5,4,1,0,1,3)
# engine.execute(f'''
#                INSERT INTO user_input
#                (username,
#                 a_points,
#                 b_points,
#                 a_offense_rush_yards,
#                 b_offense_rush_yards,
#                 a_incomplete_pass,
#                 b_incomplete_pass,
#                 a_penalty,
#                 b_penalty,
#                 a_penalty_yards,
#                 b_penalty_yards,
#                 surface,
#                 b_home,
#                 result)
#                VALUES {list_of_inputs}
#                ''')
# def get_winner(user_input):
    
#     print('winner')
# get_winner(user_input = list_of_inputs)
# # brian_function = 