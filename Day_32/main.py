##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas as pd
import datetime as dt
import random as ran
import glob
import smtplib

my_email = '18gianlucab@gmail.com'
password = 'fpbuqkkekwlshjft'


folder_path = 'letter_templates/*'

# Get a list of all files in the folder
files_with_path = glob.glob(folder_path)


#read csv with birthdays
birthdays_data = pd.read_csv('birthdays.csv')


#today
now = dt.datetime.now()
this_month = now.month
today = now.day


todays_birthdays = birthdays_data[(birthdays_data.month == this_month) & (birthdays_data.day == today)]

if len(todays_birthdays) != 0 :
    for i in range(len(todays_birthdays)):

        file_path = ran.choice(files_with_path)
        with open(file_path,'r') as f:
            letter = f.read()
            letter = letter.replace('[NAME]',todays_birthdays.name.iloc[i])

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(
                from_addr = my_email,
                to_addrs = todays_birthdays.email.iloc[i] ,
                msg = f'Subject:Birthday Wishes!\n\n{letter}')

        
