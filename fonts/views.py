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
    return render(request,"fontgen.html",context)

def quiz(request):
    q_number=0
    parameter={
        "amount":10,
        "type":"boolean",
        "category":18,
    }

    raw_data=requests.get("https://opentdb.com/api.php",params=parameter)
    raw_data.raise_for_status()

    data=raw_data.json()["results"][q_number]

    context={
        "question":data["question"],
        "correct_ans":data["correct_answer"],
    }
    return render(request,"quiz.html",context)