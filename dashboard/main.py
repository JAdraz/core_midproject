import streamlit as st
from gets import get_cases, get_deaths, get_recovered
from charts import chart1
import matplotlib.pyplot as plt

# Header
st.title("COVID-19 Dashboard")

data = get_cases()
st.text(data[0])
chart1(data[0])