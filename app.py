import streamlit as st
import pandas as pd
import numpy as np

DATA_URL= (
"/home/rhyme/Desktop/Project/Motor_Vehicle_Collisions_-_Crashes.csv"
)

st.title("Motor Vehicle Collisions in New York city")
st.markdown("This application is a Streamlit dahboard that can be used"
"to analyze motor vehicle collisions in NYC")


@st.cache(persist = True)
def load_data(nrows):
    data =pd.read_csv(DATA_URL, nrows=nrows, parse_dates = [["CRASH_DATE","CRASH_TIME"]])
    data.dropna(subset= ["LATITUDE","LONGITUDE"],inplace = True)
    lowercase = lambda x:str(x).lower()
    data.rename(lowercase,axis ="columns",inplace= True)
    data.rename(columns={"crash_date_crash_tİme":"date/tİme"},inplace = True)
    return data

data =load_data(100000)

st.header("Where are the most people injured in NYC")
injured_people =st.slider("Number of Person injured in vehicel collisions",0,19)
st.map(data.query("injured_persons >= @injured_people")[["latitude","longitude"]].dropna(how="any"))


st.header("How many collisions occur during a given time of day?")
hour = st.sidebar("Hour to look at", 0, 23)
data =data[data["data/time"].dt.hour == hour]




if st.checkbox("Show Raw Data",False):
    st.subheader("Raw Data")
    st.write(data)


