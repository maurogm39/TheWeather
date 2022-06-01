import requests
from pprint import pprint

API_Key="2c7b2e292adc01d6f59e5e1bc2fc451e"

city=input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)