import streamlit as st
import time

def slow_print(text, delay=0.017):
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(text[:i] + "▌")
        time.sleep(delay)
    placeholder.markdown(text)