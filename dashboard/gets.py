from url import url
import requests


def get_sex():
    return requests.get(url+"/all/germany/cases/").json()

def get_island():
    return requests.get(url+"/all/germany/deaths/").json()

def get_species():
    return requests.get(url+"/all/germany/recovered/").json()