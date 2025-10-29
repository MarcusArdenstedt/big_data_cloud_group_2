import duckdb 
import pandas as pd 
import os
import requests
import streamlit as st


db_path = os.getenv("DUCKDB_PATH")

# Create GEOJSON_URL in .env and get the url from azure blob container
# change this to your own blob url.
geojson_url = "https://asa9zosoy.blob.core.windows.net/group29zosoy/geojson_data" 

def query_job_listings(occupational_field):

    with duckdb.connect(db_path, read_only=True) as conn:
        if occupational_field == "Data/IT":
            query='SELECT * FROM marts.mart_data_it'
        elif occupational_field == "Säkerhet och bevakning":
            query='SELECT * FROM marts.mart_safety'
        else:
            query='SELECT * FROM marts.mart_social_work'
        # Execute the query
        df = pd.read_sql(query, conn)
        
        return df

@st.cache_data
def load_geojson():
    url = geojson_url
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
    
