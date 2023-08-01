import requests
import json
import os



city = input('Enter the name of the city\n')

url = f"https://api.weatherapi.com/v1/current.json?key=6f7660513b194b0186b170606230108&q={city}"

r = requests.get(url)

wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

os.system(f"espeak 'The current weather in {city} is {w} degrees'")




