from url import url
import requests


# def get_confirmed(a:str):
#     country = a.capitalize()
#     return (requests.get(url+f"/confirmed/{country}")).json()

# def get_deaths(a:str):
#     country = a.capitalize()
#     return requests.get(url+f"/deaths/{country}").json()

# def get_recovered(a:str):
#     country = a.capitalize()
#     return requests.get(url+f"/recovered/{country}").json()

def get_countries():
    return (requests.get(url+f"/countries")).json()

def get_data(db_name, country):
    return (requests.get(f"http://127.0.0.1:8000/{db_name}/{country}")).json()