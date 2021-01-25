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


