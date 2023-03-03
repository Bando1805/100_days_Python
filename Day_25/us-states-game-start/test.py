import pandas as pd

df = pd.read_csv('50_states.csv')

guesses = ['New york','colorado']
guesses = [item.lower() for item in guesses]
print(df.query('state not in @guesses'))
