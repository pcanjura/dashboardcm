# streamlit_app.py

import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from gsheetsdb import connect



# Create a connection object.
conn = connect()

@st.experimental_singleton()
def connect():
    # Create a connection object.
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[SCOPE],
    )
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.

@st.cache(ttl=60)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows


# sheet_url = st.secrets["public_gsheets_url"]
# rows = run_query(f'SELECT * FROM "{sheet_url}"')

# # Print results.
# for row in rows:
#     st.write(f"{row.name} has a :{row.pet}:")

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

st.write("Holi")

