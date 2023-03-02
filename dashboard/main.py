import streamlit as st
from datetime import datetime
import requests

st.set_page_config(page_title="Germany COVID-19 Dashboard", layout="wide")

# Header
st.title("Germany COVID-19 Dashboard")
st.write("By Jesus Adraz")

# Sidebar
db_selected = st.selectbox("What do you want to show?", ["Confirmed Cases", "Deaths", "Recovered"])

data = get_cases()
st.text(data[0])
chart1(data[0])