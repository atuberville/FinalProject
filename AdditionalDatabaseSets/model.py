from sqlite_guide import engine
engine.execute(
    '''CREATE TABLE IF NOT EXISTS 
        user_input_java_winner (
        id INTEGER NOT NULL,
        username VARCHAR, 
        a_points INTEGER NOT NULL,
        b_points INTEGER NOT NULL,
        a_offense_rush_yards INTEGER NOT NULL,
        b_offense_rush_yards INTEGER NOT NULL,
        a_offense_pass_yards INTEGER NOT NULL,
        b_offense_pass_yards INTEGER NOT NULL,
        a_incomplete_pass INTEGER NOT NULL,
        b_incomplete_pass INTEGER NOT NULL,
        a_penalty_yards INTEGER NOT NULL,
        b_penalty_yards INTEGER NOT NULL,
        b_home INTEGER NOT NULL,
        result INTEGER NOT NULL,
        PRIMARY KEY (id))''' )