import streamlit as st
import pandas as pd     
import plotly
import requests
import numpy as np
import tweepy


primaryColor="#346094"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="serif"


option = st.sidebar.selectbox(
    'Which Dashboard?',
    ('Twitter', 'WallStreetBets', 'Mobile Phone','Stock Tweets','Chart', 'Pattern'))

st.write('You Selected:', option)

st.header(option)

if option == 'Twitter':
    st.subheader("Twitter dashboard")

if option == 'WallStreetbets':
    st.subheader("WallStreetBets dashboard:")

if option == 'chart':
    st.subheader("this is the chart dashboard")


if option == 'Stock Tweets':
   # st.subheader("stocktwits")

   symbol = st.sidebar.text_input("Symbol", value='TSLA', max_chars=5)
  
   r=requests.get(f'https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json')

   data= r.json()
   
   for messages in data["messages"]:
    
 
       st.write(messages['body'])
       st.write(messages['user']['username'])
       st.write(messages['created_at'])
       st.image(messages['user']['avatar_url'])
   

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)