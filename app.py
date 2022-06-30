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

import streamlit as st

st.set_page_config(page_title="番茄钟", layout="wide")
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 400px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 400px;
        margin-left: -400px;
    }
     
    """,
    unsafe_allow_html=True,
)
#def remote_css(url):
#    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

#def icon(icon_name):
#    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
#remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')


#---------------------------------#

# Timer
# Created by adapting from:
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
# https://docs.streamlit.io/en/latest/api.html#lay-out-your-app

event_name = st.sidebar.text_input("What do you want to do", '躺平')
button_clicked = st.button("Start")

focus_time = st.sidebar.slider('Select focus time', 0, 60, 25)
focus_sec = focus_time*60
break_time = 300

import os
os.system("curl --create-dirs -o $HOME/.postgresql/root.crt -O https://cockroachlabs.cloud/clusters/15f22c6a-7413-42be-b232-ca4adf391767/cert")
os.environ["DATABASE_URL"] = "postgresql://pomodoro:M6LajZ2nQ_XFCaiYyvnlpg@free-tier7.aws-eu-west-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dkingly-druid-2749"

import os
# from sqlalchemy import create_engine, text

# test sql
import psycopg2


if button_clicked:
    st.write(event_name)
    conn = psycopg2.connect(os.environ["DATABASE_URL"])

    with conn.cursor() as cur:
        cur.execute("SELECT now()")
        res = cur.fetchall()
        conn.commit()
        st.text(res)

    with st.empty():
        

        my_bar = st.progress(0)
        while focus_sec:
            mins, secs = divmod(focus_sec, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏳ {timer}")
            time.sleep(1)
            focus_sec -= 1
            my_bar.progress(1-focus_sec/(focus_time*60))
            st.success("🔔 25 minutes is over! Time for a break!")


    with st.empty():
        while break_time:
            # Start the break
            mins2, secs2 = divmod(break_time, 60)
            timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
            st.header(f"⏳ {timer2}")
            time.sleep(1)
            break_time -= 1
            st.error("⏰ 5 minute break is over!")
