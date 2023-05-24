import requests

api_key = "asdf"
lat = 51.507351
lon = -0.127758

response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={'current, minutely, daily'}&appid={api_key}")
response.raise_for_status()
weather_data = response.json()

will_rain = False
weather_slice = weather_data['hourly'][:12]
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")

