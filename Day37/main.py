import requests
from datetime import datetime

USERNAME = "nickvtrai10"
TOKEN = "secrettokenn234"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
print(today.strftime("%Y%m%d"))

post_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
post_value_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}

DATE = "20230525"
put_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
put_value_config = {
    "quantity": "8.9"
}

response = requests.put(url=put_value_endpoint, json=put_value_config, headers=headers)
print(response.text)


