import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# This function creates a linear chart for confirmed, deaths and recovered cases
def chart1(data):
    raw1 = list(data[0].keys())
    raw2 = list(data[0].values())

    dates = [datetime.date(datetime.strptime(date_string, '%m/%d/%y')) for date_string in raw1[3:]]
    cases = [int(n) for n in raw2[3:]]

    df = pd.DataFrame([dates, cases]).T
    df.columns = ["Date", "Cases"]

    return plt.plot(df['Date'], df['Cases']), plt.xlabel('Dates'), plt.ylabel('Confirmed Cases'), plt.grid('minor'), plt.show()
    