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
url = 'https://api.coinbase.com/v2/prices/EUR/spot?'
response = requests.get(url).json()
print(response)


# Importing CSV using Pandas Dataframe - Data from : https://www.kaggle.com/idoyo92/epl-stats-20192020
data = pd.read_csv('players_1920_fin.csv')

# Checking Data size( Print Col & Row's) using shape
print(data.shape)

# Prints out first 30  rows
print(data.head(30))

# Checking for missing data (There is none so no dropping of tables required.)
print(data.isnull().values.any())


# Checking types of data in the dataframe
data.info()

# Printing out FPL player names
player_names = pd.unique(data.full)
print(player_names)

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
print(Restrcuted_Data_By_GW.head(40))

#Using grouping to find the Mean Bonus Points scored by Aaron Connolly each time he scored
Aaron_Connolly = ['Aaron Connolly']

Aaron_Connolly_Stats = data.loc[data['full'].isin(Aaron_Connolly)]

Aaron_Connolly_BPS = Aaron_Connolly_Stats.groupby('goals_scored').bps.mean()
print(Aaron_Connolly_BPS)



#x = Aaron_Connolly_Stats['ppm']
#y = Aaron_Connolly_Stats['bonus']

# Bar chart
#plt.xlabel('ppm', fontsize=18)
#plt.ylabel('bonus', fontsize=16)
#plt.plot(x, y)

#plt.show()