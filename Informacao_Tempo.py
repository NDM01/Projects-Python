import requests
from pprint import pprint

API_Key = 'd6c56935b30dd7b5d81044d5b6d7a0d0'

cidade = input("Insira a cidade: ")

base_url = "http//api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+cidade

weather_data = requests.get(base_url).json()

print(weather_data)
