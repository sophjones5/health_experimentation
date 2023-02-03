import importlib.util
import sys
import streamlit as st
from oura import OuraClient
import pandas as pd
from streamlit_autorefresh import st_autorefresh
import datetime 
from datetime import date
from dateutil.relativedelta import relativedelta
from navbutton.py import *

# update every 5 mins
st_autorefresh(interval=1 * 60 * 1000, key="dataframerefresh")

st.title('Welcome to your Oura Ring Experiment Dashboard!')
st.write("")
st.write('We just need the following information to make your own personalised dashboard :smile:')
st.write("")
experiment = st.text_input("What factor/experiment do you wish to observe the effect of?", 'a carnivore diet')
st.session_state['experiment'] = experiment
start_date = st.text_input("What date did you start your experiment?", date.today().strftime("%d-%m-%Y"))
st.session_state['start_date'] = datetime.datetime.strptime(start_date, "%d-%m-%Y").date()
user_AT = st.text_input("What is your oura ring access token? \n Log in at https://cloud.ouraring.com/personal-access-tokens to create a new one and copy it.", type="password")
st.session_state['access_token'] = user_AT

if st.button("To your Dashboard!"):
    nav_page("Experiment")
