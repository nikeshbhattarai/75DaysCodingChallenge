import requests
from datetime import datetime

APP_ID = "2eca663a"
API_KEY = "bfb11d9f7369b3b8a0cbfab934baf8c1"

exercises = input("Tell me which exercises you did: ")

exercise_config = {
    "query": exercises,
    "weight_kg": 71,
    "height_cm": 170,
    "age": 25

}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise" 

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
response.raise_for_status()
result = response.json()

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

sheety_endpoint = "https://api.sheety.co/801fbe4745f4dc3d31565ea97424b62a/workoutTracking/workouts"
for exercise in result['exercises']:
    sheety_json = {
        "workout" : {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'] 
        }
    }

sheety_response = requests.post(url=sheety_endpoint, json=sheety_json)
print(sheety_response.text)