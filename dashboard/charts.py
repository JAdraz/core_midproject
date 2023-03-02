import requests
import pandas as pd
from datetime import datetime
import plotly.graph_objs as go

# This function gets the data name







# This function creates a linear chart for confirmed, deaths and recovered cases
# def chart1(data):
#     raw1 = list(data[0].keys())
#     raw2 = list(data[0].values())

#     dates = [datetime.date(datetime.strptime(date_string, '%m/%d/%y')) for date_string in raw1[3:]]
#     cases = [int(n) for n in raw2[3:]]
    # for i in ["Country/Region", "Lat", "Long"]:
    #     data.pop(i)
    # pd.DataFrame.from_records([data])
    # return st.bar_chart(data)