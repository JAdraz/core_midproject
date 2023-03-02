from fastapi import APIRouter
from mongo.connection import db
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/confirmed/{country}")
def confirmed_cases(country:str):
    filt = {"Country/Region":country}
    project = {"_id":0, "Country/Region":0, "Lat":0, "Long":0}
    res = db["confirmed_cases"].find(filt, project)
    return loads(json_util.dumps(res))

@router.get("/deaths/{country}")
def death_cases(country:str):
    filt = {"Country/Region":country}
    project = {"_id":0, "Country/Region":0, "Lat":0, "Long":0}
    res = db["deaths_cases"].find(filt, project)
    return loads(json_util.dumps(res))

@router.get("/recovered/{country}")
def recovered_cases(country:str):
    filt = {"Country/Region":country}
    project = {"_id":0, "Country/Region":0, "Lat":0, "Long":0}
    res = db["recovered_cases"].find(filt, project)
    return loads(json_util.dumps(res))