import requests
import datetime as dt
import 

MY_LAT = 37.478489
MY_LNG = 126.864288
params = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)

data = response.json()['results']
sunset = data['sunset'].split('T')[1]
sunset_hour = (int(sunset.split(':')[0]) + 9) % 24
sunset_min = int(sunset.split(':')[1])

current = dt.datetime.now()
current_hour = current.hour
current_min = current.minute

response = requests.get(url='http://api.open-notify.org/iss-now.json')
data = response.json()['iss_position']
iss_lat = float(data['latitude'])
iss_lng = float(data['longitude'])
print((iss_lat, iss_lng))

def is_iss_nearby():
    if  MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG  -5 <= iss_lng <= MY_LNG + 5:
        return True

def is_it_night():
    if current_hour >= sunset_hour and current_min >= sunset_min:
        return True

if is_iss_nearby() and is_it_night():
