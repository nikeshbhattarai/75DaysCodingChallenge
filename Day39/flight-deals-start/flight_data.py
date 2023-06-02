import requests
from data_manager import DataManager
from datetime import datetime

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILE_API_KEY = "c_T_StxMuX0IYja8dgE2552yQpImhcot"

data_manager = DataManager()
data = data_manager.get_destination_data()
print(data)
class FlightData:
    #This class is responsible for structuring the flight data.
    def get_flight_price(self):
        data = data_manager.get_destination_data()
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey" : TEQUILE_API_KEY}
        query = {
            "fly_from" : "LON",
            "fly_to" : data['iataCode'],
            "date_from" : ,
            "date_to" :  
        }