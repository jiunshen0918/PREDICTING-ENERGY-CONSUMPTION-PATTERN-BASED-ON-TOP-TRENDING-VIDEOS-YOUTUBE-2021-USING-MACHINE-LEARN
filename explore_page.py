import streamlit as st
import numpy as np
import pandas as pd
import io

#define explore coding
def show_explore_page():
    st.title("Youtube Energy Estimate Page")

    st.write("""### Explore the *Data!* :sunglasses:""")
    
    #load data
    youtube=pd.read_csv("YoutubeDataset.csv")
    
    #buttons
    head = st.button("Show top 5 records of data")
    tail = st.button("Show last 5 records of data")
    info = st.button("Show data's information")
    desc = st.button("Show data's description")
    corr = st.button("Show target data's correlationship")
    
    if head:
        st.write("""Top 5 records of data is""",youtube.head())
    elif tail:
        st.write("""Last 5 records of data is""",youtube.tail())
    elif info:
        buffer = io.StringIO()
        youtube.info(buf=buffer)
        info=buffer.getvalue()
        st.text("""Data's description is""",info)
    elif desc:
        st.write("""Data's description is""",youtube.describe())
    elif corr:
        corr_matrix=youtube.corr()
        st.write("""Target data's correlationship is""",corr_matrix['Total_Energy(kJ)'].sort_values(ascending=False))
    
show_explore_page()
    
