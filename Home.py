import importlib.util
import sys
import streamlit as st
from oura import OuraClient
import pandas as pd
from streamlit_autorefresh import st_autorefresh
import datetime 
from datetime import date
from dateutil.relativedelta import relativedelta
from util import navbutton

st.set_page_config(page_title='Oura Experiments', page_icon='logo.png', layout="centered", initial_sidebar_state="auto", menu_items=None)

# update every 5 mins
st_autorefresh(interval=1 * 60 * 1000, key="dataframerefresh")

def text_field(label, columns=None, **input_params):
    c1, c2 = st.columns(columns or [1, 4])

    # Display field name with some alignment
    c1.markdown("##")
    c1.markdown(label)

    # Sets a default key parameter to avoid duplicate key errors
    input_params.setdefault("key", label)

    # Forward text input parameters
    return c2.text_input("", **input_params)


st.markdown("<h1 style='text-align: center; color: white; font-size:55px;'>Oura Ring Health Experimentation!</h1>", unsafe_allow_html=True)
st.write("")
st.markdown("<h2 style='text-align: center; color: white; font-size:20px;'>Input the following information to make your own personalised dashboard</h2>", unsafe_allow_html=True)
st.write("")


experiment = text_field("Experiment name:", placeholder = 'a carnivore diet')
st.session_state['experiment'] = experiment or 'a carnivore diet'
start_date = text_field("Start Date:", placeholder = "25-01-2023")
st.session_state['start_date'] = datetime.datetime.strptime(start_date or "25-01-2023", "%d-%m-%Y").date()
user_AT = text_field("Oura Access Token:", type="password")
st.session_state['access_token'] = user_AT
st.write("")
st.write('Log in at https://cloud.ouraring.com/personal-access-tokens to create a new one and copy it.')
st.write("")

c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    pass
with c2:
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4b5eff;font-size:25px;height:2em;width:10em;border-radius:10px 10px 10px 10px;

    }
    </style>""", unsafe_allow_html=True)
    if st.button("To your Dashboard!"):
        navbutton.nav_page("Experiment")
with c3:
    pass


