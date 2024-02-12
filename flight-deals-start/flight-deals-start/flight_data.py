from datetime import datetime


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, places, input_place, date_to_data):
        self.tequila_endpoint = "https://api.tequila.kiwi.com/"
        self.header_tequila = {
            "apikey": "yx5w2USItJTJkpQGAGS5MTfLWdykIj_l"
        }

        self.params_gl = {
            "term": f"{places}",
            "locale": "en-US",
            "location_types": "city",
            "limit": "1",
        }

        self.get_search_params = {
             "fly_from": f"{places}",
             "fly_to": f"{input_place}",
             "date_from": f"{datetime.now().strftime("%d/%m/%Y")}",
             "date_to": f"{date_to_data}",
             "limit": "5",
             }
