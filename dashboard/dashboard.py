import streamlit as st
from gets import get_cases, get_deaths, get_recovered
from charts import chart1

st.header("Prueba")
data = get_cases()
chart1(data)