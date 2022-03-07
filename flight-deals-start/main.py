from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import Notification

# create data management object
d_m = DataManager()
# get destination data from google sheet
sheet_datas = d_m.get_destination_data()
# flight information list
info_list = []
# create flight searching object
search = FlightSearch()

for data in sheet_datas:
    # search a ticket that meets the conditions
    searched_data = search.check_flights(data['iataCode'], data['lowestPrice'])
    # if there's a ticket that meets the conditions, find the cheapest ticket
    if searched_data != None:
        cheapest_data = searched_data[0]
        for s_data in searched_data:
            if s_data['price'] < cheapest_data['price']:
                cheapest_data = s_data
        flight_info = d_m.extract_info(cheapest_data)
        # store information on the cheapest ticket in the list
        info_list.append(flight_info)

# message content
message = ""
# about the cheapest ticket information to each city,
n_m = Notification()
for info in info_list:   
    message += f"Low price alert! Only £{info['flight_price']} to fly from {info['city_from']}-{info['fly_from']} to {info['city_to']}-{info['fly_to']}, from {info['utc_departure']} to {info['utc_arrival']}\n\n"

n_m.send_sms(message)

