import requests
import pandas as pd
from datetime import datetime
import plotly.graph_objs as go

AXIS_FONT_SIZE = 20
FIG_HEIGHT = 400
FIG_WIDTH = 600
MIN_DATE = datetime.date(datetime(2020,1,22))
MAX_DATE = datetime.date(datetime(2021,4,10))


def get_db_name(database):
    if database == 'Confirmados':
        db_name = 'confirmed_cases'
    elif database == 'Muertes':
        db_name = 'deaths_cases'
    else:
        db_name = 'recovered_cases'
    return db_name


def chart1(data):
    raw1 = list(data[0].keys())
    raw2 = list(data[0].values())

    dates = [datetime.date(datetime.strptime(date_string, '%m/%d/%y')) for date_string in raw1[3:]]
    cases = [int(n) for n in raw2[3:]]
    for i in ["Country/Region", "Lat", "Long"]:
        data.pop(i)
    pd.DataFrame.from_records([data])
    return st.bar_chart(data)