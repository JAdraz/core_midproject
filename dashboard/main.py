import streamlit as st
from gets import get_cases, get_deaths, get_recovered
from charts import chart1

# Header
st.title("COVID-19 Dashboard")

data = get_cases()
chart1(data)