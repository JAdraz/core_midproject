from fastapi import APIRouter
from mongo.connection import db

router = APIRouter()

# @router.get("/cases/{country}/{MM/DD/AA}")
# def country_cases(country):