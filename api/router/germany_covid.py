from fastapi import APIRouter
from mongo.connection import db
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/{country}/cases/")
def confirmed_cases(country:str):
    filt = {"Country/Region"}
    project = 
    res = db["germany_covid_confirmed"].find({}, {"_id":0})
    return loads(json_util.dumps(res))

@router.get("/germany/deaths/")
def death_cases():
    res = db["germany_covid_deaths"].find({}, {"_id":0})
    return loads(json_util.dumps(res))

@router.get("/all/germany/recovered/")
def recovered_cases():
    res = db["germany_covid_recovered"].find({}, {"_id":0})
    return loads(json_util.dumps(res))