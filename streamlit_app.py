import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

spreadsheet_url = st.secrets.connections.gsheets["spreadsheet"]

st.write(f"Reading data from spreadsheet: {spreadsheet_url}")

df = conn.read(spreadsheet=spreadsheet_url)
 
st.dataframe(df)