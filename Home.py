import importlib.util
import sys

name = 'oura'

if name in sys.modules:
    print(f"{name!r} already in sys.modules")
elif (spec := importlib.util.find_spec(name)) is not None:
    # If you choose to perform the actual import ...
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    print(f"{name!r} has been imported")
else:
    print(f"can't find the {name!r} module")

'''
import subprocess
import sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'oura'])
'''

import streamlit as st
from oura import OuraClient
import pandas as pd
from streamlit_autorefresh import st_autorefresh
import datetime 
from datetime import date
from dateutil.relativedelta import relativedelta

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
user_AT = st.text_input("What is your oura ring access token?", type="password")
url = "https://cloud.ouraring.com/personal-access-tokens"
st.markdown("""
<style>
.small-font {
    font-size:12px;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="small-font">Log in [here](%s) to create a new one and copy it.</p>'% url, unsafe_allow_html=True)
st.session_state['access_token'] = user_AT
