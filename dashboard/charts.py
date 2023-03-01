import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt

# This function creates a linear chart for confirmed, deaths and recovered cases
def chart1(data):
    raw1 = list(data[0].keys())
    raw2 = list(data[0].values())

    dates = [datetime.date(datetime.strptime(date_string, '%m/%d/%y')) for date_string in raw1[3:]]
    cases = [int(n) for n in raw2[3:]]

    return st.plotly_chart(cases, dates)
    # plt.plot(dates, cases), plt.xlabel('Dates'), plt.ylabel('Confirmed Cases'), plt.yticks([1_000_000, 2_000_000, 3_000_000, 4_000_000], ["1M", "2M", "3M", "4M"]), plt.grid("minor")
    # return plt.show()