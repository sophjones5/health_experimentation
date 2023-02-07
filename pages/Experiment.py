import streamlit as st
from oura import OuraClient
import pandas as pd
from streamlit_autorefresh import st_autorefresh
import datetime
from dateutil.relativedelta import relativedelta

st.markdown(f"<h1 style='text-align: center; color: white; font-size:55px;'>Effect of {st.session_state.experiment} on your health!</h1>", unsafe_allow_html=True)

#scrpping required data from api
client = OuraClient(personal_access_token=st.session_state.access_token)
user_info = client.user_info()
startdate = st.session_state.start_date
experimentsleepdf = pd.DataFrame(client.sleep_summary(start = str(startdate))['sleep'])
preexperimentsleepdf = pd.DataFrame(client.sleep_summary(start = str(startdate- relativedelta(years=2)), end = str(startdate))['sleep'])

#analysing sleep scores
preexperimentsleepdf['average_sleep_score'] = preexperimentsleepdf['score_total'].mean()
samplesize = len(experimentsleepdf)
st.markdown("<h2 style='text-align: center; color: white; font-size:35px;'>Average sleep scores</h2>", unsafe_allow_html=True)
st.write("")
col1, col2, col3,col4, col5 = st.columns([1,1,1,1,1])
col2.metric("Before", str(round(preexperimentsleepdf['score_total'].mean(),1)))
col4.metric("During", str(round(experimentsleepdf['score_total'].mean(),1)), f"{round(((experimentsleepdf['score_total'].mean()-preexperimentsleepdf['score_total'].mean())/experimentsleepdf['score_total'].mean())*100,2)}%")
st.write("")
df=pd.concat([preexperimentsleepdf['average_sleep_score'].sample(n=samplesize).rename("average_pre_experiment").reset_index(drop=True),experimentsleepdf['score_total'].rename("experiment").reset_index(drop=True)],axis=1)
st.line_chart(df, height=250)
st.write("")

#analysis effect on rem sleep- something found during my inital exploration
st.markdown("<h2 style='text-align: center; color: white; font-size:35px;'>Average Percentage of Rem sleep</h2>", unsafe_allow_html=True)
#adding percentage of rem as a new column
st.write("")
experimentsleepdf['percentage_rem'] = experimentsleepdf['rem']/experimentsleepdf['total']*100
preexperimentsleepdf['percentage_rem'] = preexperimentsleepdf['rem']/preexperimentsleepdf['total']*100
preexperimentsleepdf['average_rem_percentage'] = preexperimentsleepdf['percentage_rem'].mean()
col1, col2, col3,col4, col5 = st.columns([1,1,1,1,1])
col2.metric("Before", f"{round(preexperimentsleepdf['percentage_rem'].mean(),1)}%")
col4.metric("During", f"{round(experimentsleepdf['percentage_rem'].mean(),1)}%", f"{round(experimentsleepdf['percentage_rem'].mean()-preexperimentsleepdf['percentage_rem'].mean(),2)}%")
st.write("")
df=pd.concat([preexperimentsleepdf['average_rem_percentage'].sample(n=samplesize).rename("average_pre_carniovre").reset_index(drop=True),experimentsleepdf['percentage_rem'].rename("carnivore").reset_index(drop=True)],axis=1)
st.area_chart(df, height=250)
st.write("")

#analysis effect on heart rate
preexperimentsleepdf['average_hr'] = preexperimentsleepdf['hr_average'].mean()
st.markdown("<h2 style='text-align: center; color: white; font-size:35px;'>Average night HR</h2>", unsafe_allow_html=True)
st.write("")
col1, col2, col3,col4, col5 = st.columns([1,1,1,1,1])
col2.metric("Before carnivore", str(round(preexperimentsleepdf['hr_average'].mean(),1)))
col4.metric("During carnivore", str(round(experimentsleepdf['hr_average'].mean(),1)), str(round(experimentsleepdf['hr_average'].mean()-preexperimentsleepdf['hr_average'].mean(),2)), delta_color ='inverse')
st.write("")
df1=pd.concat([preexperimentsleepdf['average_hr'].sample(n=samplesize).rename("average_pre_carnivore").reset_index(drop=True),experimentsleepdf['hr_average'].rename("carnivore").reset_index(drop=True)],axis=1)
st.line_chart(df1, height=250)
st.write("")

#analysis effect on hrv
preexperimentsleepdf['average_rmssd'] = preexperimentsleepdf['rmssd'].mean()
st.markdown("<h2 style='text-align: center; color: white; font-size:35px;'>Average hrv</h2>", unsafe_allow_html=True)
st.write("")
col1, col2, col3,col4, col5 = st.columns([1,1,1,1,1])
col2.metric("Before carnivore", str(round(preexperimentsleepdf['rmssd'].mean(),1)))
col4.metric("During carnivore", str(round(experimentsleepdf['rmssd'].mean(),1)), str(round(experimentsleepdf['rmssd'].mean()-preexperimentsleepdf['rmssd'].mean(),2)))
st.write("")
df2=pd.concat([preexperimentsleepdf['average_rmssd'].sample(n=samplesize).rename("average_pre_carnivore").reset_index(drop=True),experimentsleepdf['rmssd'].rename("carnivore").reset_index(drop=True)],axis=1)
st.area_chart(df2, height=250)
st.write("")


