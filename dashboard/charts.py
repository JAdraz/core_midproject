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
    if database == 'Confirmed':
        db_name = 'confirmed'
    elif database == 'Deaths':
        db_name = 'deaths'
    else:
        db_name = 'recovered'
    return db_name


def get_df(data, date_range):
    MIN_DATE = date_range[0]
    MAX_DATE = date_range[1]
    res = data.json()
    raw = [list(res[0].keys()), list(res[0].values())]
    dates = [datetime.date(datetime.strptime(date_string, '%m/%d/%y')) for date_string in raw[0]]
    cases = [int(n) for n in raw[1]]

    df = pd.DataFrame([dates, cases]).T
    df.columns = ["Date", "Cases"]
    return df.loc[(df['Date']>=MIN_DATE) & (df['Date']<=MAX_DATE)] 

def gen_chart(countries_name, date_range, database):
    db_name = get_db_name(database)
    fig = go.Figure()
    for country in countries_name:
        data = requests.get(f"http://127.0.0.1:8000/{db_name}/{country}")
        df = get_df(data, date_range)
        fig.add_trace(go.Scatter(x=df["Date"], y=df["Cases"], name=country, mode='lines'))
    fig.update_yaxes(tickfont=dict(size=AXIS_FONT_SIZE))
    fig.update_xaxes(tickfont=dict(size=AXIS_FONT_SIZE))
    fig.update_layout(title=f"Numero total de {database.lower()} entre {date_range[0]} y {date_range[1]}",
        xaxis_title="Date",
        yaxis_title=f"{database}",
        legend_title="Countries:",
        font=dict(size=AXIS_FONT_SIZE)
        )
    return fig