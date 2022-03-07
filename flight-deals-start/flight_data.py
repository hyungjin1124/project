class FlightData:
    def __init__(self, flight_data):
        self.flight_information = {
            "fly_from": flight_data["flyFrom"],
            'fly_to': flight_data["flyTo"],
            'city_from': flight_data["cityFrom"],
            'city_to': flight_data["cityTo"],
            'flight_price': flight_data["price"],
            'utc_departure': flight_data["utc_departure"].split("T")[0],
            'utc_arrival': flight_data["utc_arrival"].split("T")[0]
        }
