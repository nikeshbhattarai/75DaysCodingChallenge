#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from flight_search import FlightSearch

response = requests.get(url="https://api.sheety.co/75327416cb3e93bd5260e25a6055c289/flightDeals/prices")
response.raise_for_status()
sheet_data = response.json()['prices']
pprint(sheet_data)

flight_search = FlightSearch()
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        print(row)


