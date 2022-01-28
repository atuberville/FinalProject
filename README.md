# conference_stats code

I know I need to make better notes, and I will. Kinda got on a roll. I will make some edits. I read in team.csv, conference.csv, and play.csv. 

In play.csv, I changed "Offense Team Code" to "Team Code1" and "Defense Team Code" to "Team Code2", then dropped "Team Code2" due to redundancy. I renamed "Team Code 1" to just "Team Code."

I merged team_df and play_df into complete_stats_df by the "Team Code" columns. Then sorted by the "Game Code" and "Play Number" columns so that each play number coorelates with the correct game code.

I merged complete_stats_df with confernce_df by the "Conference Code" columns, dropped some duplicate columns and made a fairly solid initial dataframe.

Seems to work well with Brian's function.

I know this is as basic as it gets. I am more than open to any suggestions. 

Thanks,
Ben
