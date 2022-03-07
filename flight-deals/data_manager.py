import requests
from flight_data import FlightData
sheety_endpoint = "https://api.sheety.co/e1ba0e7b0597e0a28db2bb215a602972/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.data = {}

    # get data from google sheet by using sheety
    def get_destination_data(self):
        response = requests.get(url = sheety_endpoint)
        print(response.status_code)
        result = response.json()
        self.data = result["prices"]
        return self.data
    
    # extract the necesary data
    def extract_info(self, flight_data):
        flight_info = FlightData(flight_data)
        return flight_info.flight_information