from urllib import response
from xmlrpc.client import boolean
import requests

# set the parameter used when requesting api.
params = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get(url='https://opentdb.com/api.php', params=params)
response.raise_for_status()
# set question data from api response
question_data = response.json()['results']