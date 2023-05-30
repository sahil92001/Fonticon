import requests
import random


url="https://www.googleapis.com/webfonts/v1/webfonts?key=AIzaSyDW2gZ2GC-uIaRHrxu0zVK1tscYGMRaZ1E"
response = requests.get(url)

if response.status_code == 200:
    fonts_data = response.json()
    fonts = fonts_data.get("items", [])
    random_font = random.choice(fonts)

    font= random_font["family"]
    download=random_font['files']['regular']
else:
    font="Failed to get font"

