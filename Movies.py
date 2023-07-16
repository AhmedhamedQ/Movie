import requests 
from bs4 import BeautifulSoup as bs
import plotly.express as px 
import streamlit as st 
import pandas as pd 
st.set_page_config(page_title='Movies Data' , page_icon='🎞️')

df = pd.read_csv("25k IMDb movie Dataset cleand.csv")
st.header('Welcome 😊')
st.subheader('this data set have more than 20K Movies data and you can search about what you prefer in next page')
st.subheader('____________________________________________')
st.dataframe(df , use_container_width=True)
