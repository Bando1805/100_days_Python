import smtplib 
import random as ran
import datetime as dt 

my_email = '18gianlucab@gmail.com'
password = 'fpbuqkkekwlshjft'


now = dt.datetime.now()

if now.weekday() == 4:

    with open('quotes.txt','r') as f:
        quotes_lines = f.readlines()
        quote = ran.choice(quotes_lines)
        print(quote)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = my_email ,
            msg = f'Subject: Motivational quote of the day\n\n{quote}')
