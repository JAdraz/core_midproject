from fastapi import APIRouter
from mongo.connection import db
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/all/germany/cases/")
def confirmed_cases():
    res = db["germany_covid_confirmed"].find({})[:10]
    return loads(json_util.dumps(res))

@router.get("/all/germany/deaths/")
def confirmed_cases():
    res = db["germany_covid_deaths"].find({})
    return loads(json_util.dumps(res))

@router.get("/all/germany/recovered/")
def confirmed_cases():
    res = db["germany_covid_recovered"].find({})
    return loads(json_util.dumps(res))