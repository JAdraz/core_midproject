import streamlit as st
from datetime import datetime
import requests

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")
dataset_countries_names = requests.get("http://127.0.0.1:8000/countries").json()
# Header
st.title("COVID-19 Dashboard")
st.write("By Jesus Adraz")

# Body
# Sidebar
st.sidebar.title("Menu")
countries_name = st.sidebar.multiselect("Select one or more countries", [i["Country/Region"] for i in dataset_countries_names])

print(countries_name)