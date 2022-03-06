import requests
from datetime import datetime
import json

# open config file
with open('config.json', 'r') as f:
    config = json.load(f)

APP_ID = config['DEFAULT']['APP_ID'] 
API_KEY = config['DEFAULT']['API_KEY'] 

# Use api to process natural language and receive exercise statistics.
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

GENDER = config["PRIVATE"]['GENDER']
WEIGHT = config["PRIVATE"]['WEIGHT']
HEIGHT = config["PRIVATE"]['HEIGHT']
AGE = config["PRIVATE"]['AGE']

exercise_config = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, headers=exercise_headers, json=exercise_config)
result = response.json()

# get the current time
now = datetime.now()
date = now.strftime('%d/%m/%Y')
time = now.strftime('%H:%M:%S')

# extract information from exercise sstatistics.
exercise = result['exercises'][0]['name']
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']

# authenticates sheety api and stores data in Google Sheet.
AUTHORIZATION = config["AUTHORIZATION"]
sheety_endpoint = "https://api.sheety.co/e1ba0e7b0597e0a28db2bb215a602972/workoutTracking/workouts"
sheety_headers = {
    'Authorization': config["AUTHORIZATION"]["AUTH"]
}
sheety_config = {
    'workout': {
        'date': date,
        "time": time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories 
    }
}

response = requests.post(url=sheety_endpoint, json = sheety_config, headers=sheety_headers)
print(response.text)