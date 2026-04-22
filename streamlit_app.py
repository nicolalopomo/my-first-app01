import streamlit as st
import pandas as pd
import numpy as np


with st.sidebar:
    st.header("Sidebar")
    st.write("This is the sidebar of the app.")
    st.radio("Select a page", ["Page 1", "Page 2", "Page 3"], key="page_selection"  )

st.write("This is the main page of the app.")

if st.session_state.page_selection == "Page 1":
    st.write("You are on Page 1.")
elif st.session_state.page_selection == "Page 2":
    st.write("You are on Page 2.")
elif st.session_state.page_selection == "Page 3":
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/1/15/Cat_August_2010-4.jpg")
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/0/06/Blue_merle_koolie_short_coat_heading_sheep_%28cropped%29.jpg")