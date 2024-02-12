import requests
from flight_data import FlightData


# This class is responsible for talking to the Flight Search API.

class FlightSearch(FlightData):
    def __init__(self, places, input_place, date_to_data):
        super().__init__(places, input_place, date_to_data)
        self.ticket_price = 0

    def location_request(self):
        location = requests.get("https://api.tequila.kiwi.com/locations/query", params=self.params_gl,
                                headers=self.header_tequila)
        return location.json()

    def search_flight(self):
        search_request = requests.get(f"https://api.tequila.kiwi.com/v2/search", headers=self.header_tequila,
                                      params=self.get_search_params)
        search_request.raise_for_status()
        jj = search_request.json()
        self.ticket_price = (jj["data"][0]["price"])
        return self.ticket_price
