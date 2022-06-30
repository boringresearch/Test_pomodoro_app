# App created by Data Professor http://youtube.com/dataprofessor
# GitHub repo of this app 
# Demo of this app

import streamlit as st
import time

# CSS by andfanilo
# Source: https://discuss.streamlit.io/t/creating-a-nicely-formatted-search-field/1804
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#def remote_css(url):
#    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

#def icon(icon_name):
#    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
#remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')


#---------------------------------#
st.write("""
# The Pomodoro App

Let's do some focus work in data science with this app.

Developed by: [Data Professor](http://youtube.com/dataprofessor)

""")

# Timer
# Created by adapting from:
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
# https://docs.streamlit.io/en/latest/api.html#lay-out-your-app

mins = st.sidebar.text_input("How many")
button_clicked = st.button("Start")

t1 = 1500
t2 = 300

import os
os.system("curl --create-dirs -o $HOME/.postgresql/root.crt -O https://cockroachlabs.cloud/clusters/15f22c6a-7413-42be-b232-ca4adf391767/cert")
os.environ["DATABASE_URL"] = "postgresql://pomodoro:M6LajZ2nQ_XFCaiYyvnlpg@free-tier7.aws-eu-west-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dkingly-druid-2749"

import os
from sqlalchemy import create_engine, text

# test sql
engine = create_engine(os.environ["DATABASE_URL"])
conn = engine.connect()
res = conn.execute(text("SELECT now()")).fetchall()
print(res)

if button_clicked:
    with st.empty():
        while t1:
            mins, secs = divmod(t1, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏳ {timer}")
            time.sleep(1)
            t1 -= 1
            st.success("🔔 25 minutes is over! Time for a break!")

    with st.empty():
        while t2:
            # Start the break
            mins2, secs2 = divmod(t2, 60)
            timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
            st.header(f"⏳ {timer2}")
            time.sleep(1)
            t2 -= 1
            st.error("⏰ 5 minute break is over!")
