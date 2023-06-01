import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager

response = requests.get(url="https://api.sheety.co/75327416cb3e93bd5260e25a6055c289/flightDeals/prices")
response.raise_for_status()
sheet_data = response.json()['prices']

flight_search = FlightSearch()
data_manager = DataManager()
if sheet_data[0]['iataCode'] == "":
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

