import requests
import datetime as dt
import smtplib
import time
import json

with open('config.json', 'r') as f:
    config = json.load(f)

# latitude and longitude in my city(Gwangmyung) 
MY_LAT = config['DEFAULT']['GWANGMYUNG_LAT']
MY_LNG = config['DEFAULT']['GWANGMYUNG_LNG']
# my email and password
MY_EMAIL = config['DEFAULT']['FROM_EMAIL']
MY_PASSWORD = config['DEFAULT']['PASSWORD']
# to email
TO_EMAIL = config['DEFAULT']['TO_EMAIL']

def is_iss_nearby():
    """If latitude and longitude of iss's fall within the scope of my city, return True """
    # Data is imported using api
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()['iss_position']

    # latitude and longitude of iss
    iss_lat = float(data['latitude'])
    iss_lng = float(data['longitude'])

    # the margin of error is -5 to +5
    if  (MY_LAT - 5 <= iss_lat <= MY_LAT + 5) and (MY_LNG - 5 <= iss_lng <= MY_LNG + 5):
        return True

def is_it_night():
    """if it's after the sun sets, return True"""
    # api parameter
    params = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()

    data = response.json()['results']
    # get time of sunset(UTC)
    sunset = data['sunset'].split('T')[1]
    # because my city time is 9 hours earlier than UTC, add 9 to find the sunset time in my city.
    sunset_hour = (int(sunset.split(':')[0]) + 9) % 24

    # get time of sunrise(UTC)
    sunrise = data['sunrise'].split('T')[1]
    # because my city time is 9 hours earlier than UTC, add 9 to find the sunset time in my city.
    sunrise_hour = (int(sunrise.split(':')[0]) + 9) % 24

    # get current time
    current = dt.datetime.now()
    current_hour = current.hour
    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True

while True:
    if is_iss_nearby() and is_it_night():
        # use smtplib module to send an email.
        with smtplib.SMTP('smtp.gmail.com') as connection:
            # puts the connection to the SMTP server into TLS mode.
            # all following SMTP commands are encrypted.
            connection.starttls()
            # login to my email 
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            # send email 
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Subject: Look Up👆\n\nThe ISS is above you in the sky."
            )
    # wait for a minute.
    time.sleep(60)