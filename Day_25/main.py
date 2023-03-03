from statistics import mean
import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

print(data['Primary Fur Color'].value_counts().to_csv('squirrel_colors.csv'))
