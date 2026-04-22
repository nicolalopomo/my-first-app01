import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

spreadsheet_url = st.secrets.connections.gsheets["spreadsheet"]

connection_type = st.secrets.other_secrets.my_name

st.write(f"Connection type: {connection_type}")

df = conn.read(spreadsheet=spreadsheet_url)
 
st.dataframe(df)