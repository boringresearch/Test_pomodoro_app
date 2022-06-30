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

# Title + wider window
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

local_css("style.css")

# Timer
# Created by changing:
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
# https://docs.streamlit.io/en/latest/api.html#lay-out-your-app

event_name = st.sidebar.text_input("What do you want to do", '躺平')
focus_time = st.sidebar.slider('Select focus time (mins)', 0, 60, 25)
audio_type = st.sidebar.selectbox(
     '背景音乐',
     ('雨声', '风声', '读书声'))
# audio_file = open(audio_type+'.mp3', 'rb')
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format='audio/ogg')
html_string = """
            <audio controls autoplay>
              <source src="https://github.com/boringresearch/Test_pomodoro_app/blob/main/%E9%9B%A8%E5%A3%B0.mp3?raw=true" type="audio/mp3">
            </audio>
            """
sound = st.empty()
sound.markdown(html_string, unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it

button_clicked = st.sidebar.button("Start")

focus_sec = focus_time*60
break_time = 300

import os
os.system("curl --create-dirs -o $HOME/.postgresql/root.crt -O https://cockroachlabs.cloud/clusters/15f22c6a-7413-42be-b232-ca4adf391767/cert")
os.environ["DATABASE_URL"] = "postgresql://pomodoro:M6LajZ2nQ_XFCaiYyvnlpg@free-tier7.aws-eu-west-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dkingly-druid-2749"

# test sql
import psycopg2

if button_clicked:
    # st.header(event_name)
    # conn = psycopg2.connect(os.environ["DATABASE_URL"])

    # with conn.cursor() as cur:
    #     cur.execute("SELECT now()")
    #     res = cur.fetchall()
    #     conn.commit()
    #     st.text(res)

    with st.empty():
        my_bar = st.progress(0)

        while focus_sec:
            mins, secs = divmod(focus_sec, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            # st.header(f"⏳ {timer}")
            st.markdown('<p class="big-font">'+timer+'</p>', unsafe_allow_html=True)

            time.sleep(1)
            focus_sec -= 1
            my_bar.progress(1-focus_sec/(focus_time*60))
            st.success("🔔 25 minutes is over! Time for a break!")


    with st.empty():
        while break_time:
            # Start the break
            mins2, secs2 = divmod(break_time, 60)
            timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
            st.markdown('<p class="big-font">'+timer2+'</p>', unsafe_allow_html=True)
            time.sleep(1)
            break_time -= 1
            st.error("⏰ 5 minute break is over!")
