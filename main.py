#Setting up files for Project Rubric Assignment

# Imports
import pandas as pd

# Importing CSV using Pandas Dataframe - Data from : https://www.kaggle.com/idoyo92/epl-stats-20192020
data = pd.read_csv('players_1920_fin.csv')

# Checking Data size( Print Col & Row's) using shape
print(data.shape)

# Prints out first 30  rows
print(data.head(30))

# Checking for missing data
print(data.isnull().values.any())

# Printing out FPL player names
player_names = pd.unique(data.full)
print(player_names)

#Creating Array of Top 6 Clubs
Top_6_Clubs = ['Liverpool','Manchester United','Manchester City','Arsenal','Chelsea','Tottenham']

#Then slice the dataset to just show data from Top 6 Teams
Top_6_Clubs_Data = data.loc[data['team'].isin(Top_6_Clubs)]

print(Top_6_Clubs_Data)

