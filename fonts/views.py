from django.shortcuts import render
import random
import requests


<<<<<<< HEAD
def fontname():
=======
def font_var():
>>>>>>> 13485d91ca3f8d0d51f2cf46ddfb4265968e0c67
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
<<<<<<< HEAD
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
=======
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

>>>>>>> 13485d91ca3f8d0d51f2cf46ddfb4265968e0c67
