import os
from os.path import join, dirname
from dotenv import load_dotenv
import streamlit as st

# streamlit.ioでデプロイする場合に使用する
client_id = st.secrets['CLIENT_ID']
client_secret = st.secrets['CLIENT_SECRET']

# ローカルで使用する
#load_dotenv()
#client_id = os.environ.get('CLIENT_ID')
#client_secret = os.environ.get('CLIENT_SECRET')
