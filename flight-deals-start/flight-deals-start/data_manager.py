import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.shetty_endpoint = "https://api.sheety.co/648b83c87d44aebfbed181bec458061e/flightDeals"

    def get_rows(self):
        row_retrieve_shetty = requests.get(f"{self.shetty_endpoint}/prices")
        return row_retrieve_shetty.json()

    def edit_row(self, row_no, sheet_input):
        row_code_request = requests.put(f"{self.shetty_endpoint}/prices/{row_no}", json=sheet_input)
        print(row_code_request.text)
        print(row_code_request.status_code)
        print(row_code_request.json())
