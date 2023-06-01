from django.shortcuts import render
import random
import requests




def fontgen(request):
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
    context = {
        "variable":font,
        "download":download

    }
    return render(request,"fontgen/fontgen.html",context)

def cardgen(request):
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
    context = {
        "variable":font,
        "download":download

    }
    return render(request,"fontgen/cardbody.html",context)

