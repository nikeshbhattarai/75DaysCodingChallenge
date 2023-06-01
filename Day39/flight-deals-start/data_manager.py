import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/75327416cb3e93bd5260e25a6055c289/flightDeals/prices/"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
               "price": {
                   "iataCode": city["iataCode"]
               } 
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)        