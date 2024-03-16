import requests

data=requests.get("https://sky-scanner3.p.rapidapi.com/flights/price-calendar").text

print(data)