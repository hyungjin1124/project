import requests
from twilio.rest import Client
import env

# get my twilio account_sid
account_sid = env.ACCOUNT_SID
# get my twilio autho_token
auth_token = env.AUTH_TOKEN
# get my api key of openweathermap
api_key = env.API_KEY

# latitude and longitude of Gwangmyung
MY_LAT = 37.478489
MY_LNG = 126.864288

# set openweathermap api end point
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall?"

# set params
params = {
    'lat': MY_LAT,
    'lon': MY_LNG,
    'exclude': 'current,minutely,daily',
    'appid': api_key
}

# get response from api request
response = requests.get(url=OWM_ENDPOINT, params = params)
response.raise_for_status()
weather_data = response.json()

# slicing data
weather_12hours = weather_data['hourly'][:12]

will_rain = False

# extract weather code from siliced data
weather_12hours_code = [data['weather'][0]['id'] for data in weather_12hours]
for code in weather_12hours_code:
    if int(code) <= 700:
        will_rain = True

if will_rain:
    # create client object
    client = Client(account_sid, auth_token)

    # send a mobile text message saying it will rain.
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an umbrella",
                        from_='+19108382898',
                        to=env.TO_NUMBER
                    )

    print(message.status)