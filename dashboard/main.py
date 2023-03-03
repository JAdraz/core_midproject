import streamlit as st
from datetime import datetime
from gets import get_countries
from charts import gen_chart

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")
dataset_countries_names = get_countries()
min_date = datetime.date(datetime(2020,1,22))
max_date = datetime.date(datetime(2021,4,10))

# Header
st.title("COVID-19 Dashboard")
st.write("By Jesus Adraz")

# Body
# Sidebar
with st.container():
    st.sidebar.title("Menu")
    countries_name = st.sidebar.multiselect("Select one or more countries", [i["Country/Region"] for i in dataset_countries_names])
    
    database = st.sidebar.selectbox("Select the type of cases: ",["Confirmed", "Deaths", "Recovered"])

    min_date = st.sidebar.date_input("Star Date:",  min_date, min_value=min_date, max_value=max_date)

    max_date = st.sidebar.date_input("End Date:",  max_date, min_value=min_date, max_value=max_date)

    reset = st.sidebar.button('Clear')

    date_range=(min_date, max_date)

    fig = gen_chart(countries_name, date_range, database)
    st.plotly_chart(fig)

# colocar un if cuando llame a la grafica