#Setting up files for Project Rubric Assignment

# Imports
import dateutil
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import requests


### SECTION 1 ###
#This Section is used to show off the dfferent Pyhton skills leanred over the course as per assignment guidelines.

# Using API Scraping to get latest pices from Coinbase.com in EUR(Not used in Visualisations)
#url = 'https://api.coinbase.com/v2/prices/EUR/spot?'
#response = requests.get(url).json()
#print(response)


# Importing CSV using Pandas Dataframe - Data from : https://www.kaggle.com/idoyo92/epl-stats-20192020
data = pd.read_csv('players_1920_fin.csv', encoding = 'utf-8')

# Checking Data size( Print Col & Row's) using shape
#print(data.shape)

# Prints out first 30  rows
#print(data.head(30))

# Checking for missing data (There is none so no dropping of tables required.)
#print(data.isnull().values.any())


# Checking types of data in the dataframe
data.info()

# Printing out FPL player names
player_names = pd.unique(data.full)
#print(player_names)

#Creating List of Top 6 Clubs
Top_6_Clubs = ['Liverpool','Manchester United','Manchester City','Arsenal','Chelsea','Tottenham']

#Then slice the dataset to just show data from Top 6 Teams
Top_6_Clubs_Data = data.loc[data['team'].isin(Top_6_Clubs)]

print(Top_6_Clubs_Data)

# Testing loc method to extract data from rows
# using row name of Full Name of premier League player as index

#data = pd.read_csv("players_1920_fin.csv", index_col="full")
#Player1 = data.loc["John Egan"]
#Player2 = data.loc["Joel Matip"]

#Printing out Player1 , followed by Player 2's stats for all Gameweeks
#print(Player1, "\n\n\n", Player2)


# Sorting Data by Gameweek using kickoff_time

Restrcuted_Data_By_GW = data.sort_values(['kickoff_time','team'])
#print(Restrcuted_Data_By_GW.head(40))

#Using grouping to find the Mean Bonus Points scored by Aaron Connolly each time he scored
Aaron_Connolly = ['Aaron Connolly']

Aaron_Connolly_Stats = data.loc[data['full'].isin(Aaron_Connolly)]

Aaron_Connolly_BPS = Aaron_Connolly_Stats.groupby('goals_scored').bps.mean()
#print(Aaron_Connolly_BPS)

# Using For Loop to display Aaron Connolly's Creativity V's each premier team this season
#print("Creativity, Opponent")
#for i in range(len(Aaron_Connolly_Stats)) :
   # print(Aaron_Connolly_Stats.iloc[i,5], Aaron_Connolly_Stats.iloc[i,14])


#Sorting Dataframe by Goals scored in a single game
Goals_Scored_Sort = data.sort_values(by='goals_scored', ascending=False)
#print(Goals_Scored_Sort[["full","goals_scored"]])

# Players scoring 2 or more goals in a game (Hattrick)
Players_Scoring_Over_2 = Goals_Scored_Sort[Goals_Scored_Sort.goals_scored > 2][
    ["full", "goals_scored"]]

#Using Itterows here
#print("Players Scoring a Hat-trick this season:")
#for index, row in Players_Sorring_Over_2.iterrows():
  #  print(str(row[1]) + " Goals were scored by " + row[0])

#Practicing Merging Dataframes

#FPL_Merge = pd.merge(Aaron_Connolly_Stats,Restrcuted_Data_By_GW[['goals_scored','kickoff_time','full']], on='goals_scored')
#FPL_Merge.head

#Below prints out the shape of both the Datafranes used, and the new Merged Datframe - Inner Merge
#print("Aaron_Connolly_Stats dimensions: {}".format (Aaron_Connolly_Stats.shape))
#print("Restrcuted_Data_By_GW: {}".format (Restrcuted_Data_By_GW[['goals_scored','kickoff_time','full']].shape))
#print("FPL_Merge dimensions: {}".format (FPL_Merge.shape))


#SECTION 2 - Visualisations


#Visualisation #1


#sns.set_theme(style="darkgrid")
#ax = sns.barplot(x="goals_scored", y="full", data=Players_Scoring_Over_2)
#ax.set_title('Players to score Hat-tricks')
#ax.set_ylabel('Player Name')
#ax.set_xlabel('Goals Scored')

#plt.show()

#plt.show()


#Visualisation #2
#Plotting the top 5 Players this season, based on their mean points total (total_points)

Top_5_Scoring_Players = data.groupby('full')['total_points'].mean().sort_values(ascending=False).index.values
#sns.catplot(data=data, x='total_points',  y='full',kind='bar',ci=None, legend_out=False, order=Top_5_Scoring_Players[1:6])

#plt.show()

#Visualisation #3
# Plotting the Most Selected 11  players on average over the entire season

Top_5_Selected_Players = data.groupby('full')['selected'].mean().sort_values(ascending=False).index.values
ax =sns.catplot(data=data, x='selected',  y='full',kind='bar',ci=None, legend_out=False, order=Top_5_Selected_Players[1:11])
plt.title("Most selected FPL Player %")
ax.set(xlabel='% Selected by', ylabel='Player')
plt.show()

