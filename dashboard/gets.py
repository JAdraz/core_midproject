from url import url
import requests


def get_confirmed(a:str):
    country = a.capitalize()
    print(requests.get(url+f"/confirmed/{country}"))

def get_deaths(a:str):
    country = a.capitalize()
    return requests.get(url+f"/deaths/{country}").json()

def get_recovered(a:str):
    country = a.capitalize()
    return requests.get(url+f"/recovered/{country}").json()