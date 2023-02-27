from url import url
import requests


def get_cases():
    return requests.get(url+"/all/germany/cases/").json()

def get_deaths():
    return requests.get(url+"/all/germany/deaths/").json()

def get_recovered():
    return requests.get(url+"/all/germany/recovered/").json()