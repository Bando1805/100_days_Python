import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 48.9 # Your latitude
MY_LONG = 2.3# Your longitude
MY_EMAIL = '18gianlucab@gmail.com'
PASSWORD = 'fpbuqkkekwlshjft'



response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_iss_close(lat,lng):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (iss_latitude > MY_LAT - 5 and iss_latitude < MY_LAT + 5) and (iss_longitude > MY_LONG -5 and iss_longitude < MY_LONG + 5):
        return True
    else:
        return True

def is_dark():
    current_hour = time_now.hour
    if current_hour < sunrise or current_hour > sunset:
        return True
    else:
        return False


while True:
    time.sleep(1)

    if is_dark() and is_iss_close(MY_LAT,MY_LONG):

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password = PASSWORD)
            connection.sendmail(
                from_addr = MY_EMAIL,
                to_addrs = MY_EMAIL ,
                msg = f'Subject:ISS is close!\n\nThe iss sation is currently flying over Paris')




