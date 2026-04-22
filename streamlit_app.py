import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

public_url = st.secrets.connections.gsheets["spreadsheet"]

df = conn.read(spreadsheet=st.secrets.connections.gsheets["spreadsheet"])

st.dataframe(df)