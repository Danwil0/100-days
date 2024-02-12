# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
import requests
from datetime import datetime
import pandas as pt
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

input_place = input("country code")
date_to_flight = input("date to stop ticket search in DD/MM/YY ")

data_manager = DataManager()

notification_manager = NotificationManager()

dictionary_cities = data_manager.get_rows()
cities = [cities["city"] for cities in dictionary_cities["prices"]]
city_prices = {item['city']: item['lowestPrice'] for item in dictionary_cities['prices']}


row_no = 1
for places in cities:
    flight_data = FlightData(date_to_data=date_to_flight, input_place=input_place, places=places)
    flight_search = FlightSearch(date_to_data=date_to_flight, input_place=input_place, places=places)
    location = flight_search.location_request()
    code = location["locations"][0]["code"]
    row_no += 1
    sheet_input = {
        "price":
            {
                "codes": f"{code}",
            }
    }
    data_manager.edit_row(row_no, sheet_input)

country_codes = [cities["codes"] for cities in dictionary_cities["prices"]]
city_prices = {item['codes']: item['lowestPrice'] for item in dictionary_cities['prices']}
print(country_codes)
print(city_prices)

for c_codes in country_codes:
    flight_data = FlightData(date_to_data=date_to_flight, input_place=input_place, places=c_codes)
    flight_search = FlightSearch(date_to_data=date_to_flight, input_place=input_place, places=c_codes)
    flight_price = flight_search.search_flight()
    if flight_price < city_prices[c_codes]:
        msg = (f"Only ${flight_price} To fly from {input_place} to {c_codes},\nFrom {datetime.now().strftime("%d/%m/%Y")}"
               f" to {date_to_flight}.")
        notification_manager.send_msg(article=msg)
