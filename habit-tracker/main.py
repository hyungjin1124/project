from email import header
import requests
from datetime import datetime

USERNAME = 'hyungjin'
TOKEN = 'hefjkahfkjadf'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers = headers)
# print(response.text)

graph_value_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}'

today = datetime.now().strftime('%Y%m%d')
# print(today.strftime('%Y%m%d'))

graph_value_params = {
    'date': today,
    'quantity': input('How many kilometers did you cycle today?'),
}

# response = requests.post(url=graph_value_endpoint, headers = headers, json = graph_value_params)
# print(response.text)

update_value_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}/{today}'

update_value_params = {
    'quantity': '5.5'
}

# response = requests.put(url=update_value_endpoint, headers= headers, json = update_value_params)
# print(response.text)

# response = requests.delete(url=update_value_endpoint, headers = headers)
# print(response.text)