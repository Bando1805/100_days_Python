import requests 

MY_LNG = 48.8
MY_LAT = 2.3


parameters = {
    'lat' : MY_LAT,
    'lng' : MY_LNG,
    'formatted' : 0
}

response = requests.get('https://api.sunrise-sunset.org/json',params= parameters )
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(sunrise,)