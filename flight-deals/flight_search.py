# Flight search by using tequila API
from datetime import datetime
from dateutil.relativedelta import relativedelta
import requests
import json

with open('config.json', 'r') as f:
    config = json.load(f)

TEQUILA_API_KEY = config["TEQUILA"]["API_KEY"]
tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"

class FlightSearch:
    def check_flights(self, to_city, lowest_price):
        # set the date want to view
        today = datetime.now()
        date_from = today.strftime("%d/%m/%Y")
        date_to = (today + relativedelta(months=6)).strftime("%d/%m/%Y")

        tequila_headers = {
            "apikey": TEQUILA_API_KEY
        }
        tequila_config = {
            "fly_from": "city:LON",
            "fly_to": f"city:{to_city}",
            "date_from": date_from,
            "date_to": date_to,
            "price_to": lowest_price
        }

        response = requests.get(url=tequila_endpoint, params = tequila_config, headers=tequila_headers)
        result = response.json()

        datas = result["data"]
        return datas