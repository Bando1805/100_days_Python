import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

dict = { row.letter: row.code for index,row in df.iterrows() }

word = input('Type a word: ')

code_list = [dict[letter.upper()] for letter in word]

print(code_list)
