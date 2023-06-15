from django.shortcuts import render
import random
import requests


def font_var():
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
    return context

def fontgen(request):
    context = font_var()
    return render(request,"fontgen/fontgen.html",context)

def cardgen(request):
    context = font_var()
    return render(request,"fontgen/cardbody.html",context)

def icons(request):
    return render(request,"icons/icons.html")

