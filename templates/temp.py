import requests
parameters={
    "capability":"VF",

}
fontname=requests.get(url="https://www.googleapis.com/webfonts/v1/webfonts?key=AIzaSyDW2gZ2GC-uIaRHrxu0zVK1tscYGMRaZ1E",params=parameters)
fontname.raise_for_status()

print(fontname.json()["items"][2])
