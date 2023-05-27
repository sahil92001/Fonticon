from django.shortcuts import render
import random
import requests


def fontname():
    url="https://www.googleapis.com/webfonts/v1/webfonts?key=AIzaSyDW2gZ2GC-uIaRHrxu0zVK1tscYGMRaZ1E"
    response = requests.get(url)

    if response.status_code == 200:
        fonts_data = response.json()
        fonts = fonts_data.get("items", [])
        random_font = random.choice(fonts)

        font= random_font["family"]
    else:
        font="Failed to get font"
    return font

def fontgen(request):
    font1=fontname()
    font2=fontname()
    if font1!="Failed to get font":
        context = {
            "variable1":font1,
            "variable2":font2
        }
    else:
        context = {
            "variable1":font1,
            "variable2":""
        }

    return render(request,"fontgen.html",context)
