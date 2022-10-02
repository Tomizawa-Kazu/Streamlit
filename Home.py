import streamlit as st
from pathlib import Path
import datetime

st.title('学習のためのサイト')

p = Path(r'Home.py')
update_time = datetime.datetime.fromtimestamp(p.stat().st_mtime)
update_time = update_time.strftime('%Y-%m-%d')
st.subheader(f'更新日：{update_time}')
