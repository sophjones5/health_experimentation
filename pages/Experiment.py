import streamlit as st
from oura import OuraClient
import pandas as pd
from streamlit_autorefresh import st_autorefresh
import datetime
from dateutil.relativedelta import relativedelta

st.title(F'Effect of {st.session_state.experiment} on your health')

#scrpping required data from api
client = OuraClient(personal_access_token=st.session_state.access_token)
user_info = client.user_info()
carnivorestartdate = datetime.datetime.strptime("2023-01-25", "%Y-%m-%d").date()
carnivoresleepdf = pd.DataFrame(client.sleep_summary(start = str(carnivorestartdate))['sleep'])
precarnivoresleepdf = pd.DataFrame(client.sleep_summary(start = str(carnivorestartdate- relativedelta(years=2)), end = str(carnivorestartdate))['sleep'])

#analysisng sleep scores
precarnivoresleepdf['average_sleep_score'] = precarnivoresleepdf['score_total'].mean()
samplesize = len(carnivoresleepdf)
st.header('Average sleep scores')
col1, col2 = st.columns(2)
col1.metric("Before carnivore", str(round(precarnivoresleepdf['score_total'].mean(),1)))
col2.metric("During carnivore", str(round(carnivoresleepdf['score_total'].mean(),1)), f"{round(((carnivoresleepdf['score_total'].mean()-precarnivoresleepdf['score_total'].mean())/carnivoresleepdf['score_total'].mean())*100,2)}%")
st.write("")
df=pd.concat([precarnivoresleepdf['average_sleep_score'].sample(n=samplesize).rename("average_pre_carnivore").reset_index(drop=True),carnivoresleepdf['score_total'].rename("carnivore").reset_index(drop=True)],axis=1)
st.line_chart(df, height=250)
st.write("")

#analysis effect on rem sleep- something found during my inital exploration
st.header('Average Percentage of Rem sleep')
#adding percentage of rem as a new column
carnivoresleepdf['percentage_rem'] = carnivoresleepdf['rem']/carnivoresleepdf['total']*100
precarnivoresleepdf['percentage_rem'] = precarnivoresleepdf['rem']/precarnivoresleepdf['total']*100
precarnivoresleepdf['average_rem_percentage'] = precarnivoresleepdf['percentage_rem'].mean()

col1, col2 = st.columns(2)
col1.metric("Before carnivore", f"{round(precarnivoresleepdf['percentage_rem'].mean(),1)}%")
col2.metric("During carnivore", f"{round(carnivoresleepdf['percentage_rem'].mean(),1)}%", f"{round(carnivoresleepdf['percentage_rem'].mean()-precarnivoresleepdf['percentage_rem'].mean(),2)}%")
st.write("")
df=pd.concat([precarnivoresleepdf['average_rem_percentage'].sample(n=samplesize).rename("average_pre_carniovre").reset_index(drop=True),carnivoresleepdf['percentage_rem'].rename("carnivore").reset_index(drop=True)],axis=1)
st.area_chart(df, height=250)
st.write("")

#analysis effect on heart rate
precarnivoresleepdf['average_hr'] = precarnivoresleepdf['hr_average'].mean()
st.header('Average night HR')
col1, col2 = st.columns(2)
col1.metric("Before carnivore", str(round(precarnivoresleepdf['hr_average'].mean(),1)))
col2.metric("During carnivore", str(round(carnivoresleepdf['hr_average'].mean(),1)), str(round(carnivoresleepdf['hr_average'].mean()-precarnivoresleepdf['hr_average'].mean(),2)), delta_color ='inverse')
st.write("")
df1=pd.concat([precarnivoresleepdf['average_hr'].sample(n=samplesize).rename("average_pre_carnivore").reset_index(drop=True),carnivoresleepdf['hr_average'].rename("carnivore").reset_index(drop=True)],axis=1)
st.line_chart(df1, height=250)
st.write("")

#analysis effect on hrv
precarnivoresleepdf['average_rmssd'] = precarnivoresleepdf['rmssd'].mean()
st.header('Average hrv')
col1, col2 = st.columns(2)
col1.metric("Before carnivore", str(round(precarnivoresleepdf['rmssd'].mean(),1)))
col2.metric("During carnivore", str(round(carnivoresleepdf['rmssd'].mean(),1)), str(round(carnivoresleepdf['rmssd'].mean()-precarnivoresleepdf['rmssd'].mean(),2)))
st.write("")
df2=pd.concat([precarnivoresleepdf['average_rmssd'].sample(n=samplesize).rename("average_pre_carnivore").reset_index(drop=True),carnivoresleepdf['rmssd'].rename("carnivore").reset_index(drop=True)],axis=1)
st.area_chart(df2, height=250)
st.write("")


