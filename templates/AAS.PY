import requests
import random

def get_random_font():
    # API endpoint URL
    url="https://www.googleapis.com/webfonts/v1/webfonts?key=AIzaSyDW2gZ2GC-uIaRHrxu0zVK1tscYGMRaZ1E"

    # Make the API request
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the response JSON
        fonts_data = response.json()

        # Get the list of available fonts
        fonts = fonts_data.get("items", [])

        # Select a random font from the list
        random_font = random.choice(fonts)

        return random_font["family"]
    else:
        print("Failed to fetch fonts from Google Fonts API")
        return None

# Usage
random_font = get_random_font()
if random_font:
    print("Random Font:", random_font)
