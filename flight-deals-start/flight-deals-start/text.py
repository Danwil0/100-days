import requests
shetty_endpoint = "https://api.sheety.co/648b83c87d44aebfbed181bec458061e/flightDeals"

tequila_endpoint = "https://api.tequila.kiwi.com/locations/query"
tequila_api_key = "yx5w2USItJTJkpQGAGS5MTfLWdykIj_l"
header_tequila = {
    "apikey": "yx5w2USItJTJkpQGAGS5MTfLWdykIj_l"
}

row_response_shetty = requests.get(f"{shetty_endpoint}/prices")
dictionary_of_flight_deals = row_response_shetty.json()
cities = [cities["city"] for cities in dictionary_of_flight_deals["prices"]]


cities = [cities["city"] for cities in dictionary_of_flight_deals["prices"]]
# prices = [cities["Lowest Price"] for cities in dictionary_cities["prices"]]
prices = {"cites": "prices" in dictionary_of_flight_deals}
print(prices)
# search in location api and get the the codes and put them sheets
location_codes = []
row_no = 1
for places in cities:
    parameters_for_loc = {
        "term": f"{places}",
        "locale": "en-US",
        "location_types": "city",
        "limit": "1",
    }
    location_request = requests.get(tequila_endpoint, params=parameters_for_loc, headers=header_tequila)
    locate_dict = location_request.json()

    code = locate_dict["locations"][0]["code"]
    row_no += 1
    sheet_input = {
        "price":
            {
                "codes": f"{code}",
             }
    }
    row_code_request = requests.put(f"{shetty_endpoint}/prices/{row_no}", json=sheet_input)
    print(code)
    print(row_no)
    print(sheet_input)
    print(row_code_request.text)
    print(row_code_request.status_code)
    print(row_code_request.json())



# search prices and collect prices
# to_code = input("code of your destination")
# date_to = input("what is the date")
#
#
# se_hearder = {
#     "apikey": "yx5w2USItJTJkpQGAGS5MTfLWdykIj_l"
# }
# search_params = {
#     "fly_from": "PAR",
#     "fly_to": "LON",
#     "date_from": "05/02/2024",
#     "date_to": "05/03/2024",
#     "limit": "5"
#
# }
# search_request = requests.get(f"https://api.tequila.kiwi.com/v2/search", headers=se_hearder, params=search_params)
# search_request.raise_for_status()
#
# jj = search_request.json()
# print(jj["data"][0]["price"])
