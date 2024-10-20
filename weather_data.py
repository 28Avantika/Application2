# weather_data.py
import requests
import time

API_KEY = 'fdd98ce59466ef6c4808dc3f28774a36'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
INTERVAL = 300  # 5 minutes

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fetch_data():
    while True:
        for city in CITIES:
            data = get_weather(city)
            temp = kelvin_to_celsius(data['main']['temp'])
            feels_like = kelvin_to_celsius(data['main']['feels_like'])
            condition = data['weather'][0]['main']
            dt = data['dt']
            print(f"{city}: Temp = {temp:.2f}°C, Feels like = {feels_like:.2f}°C, Condition = {condition}, Time = {dt}")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    fetch_data()
