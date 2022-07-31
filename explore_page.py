import streamlit as st
import numpy as np
import pandas as pd

#define explore coding
def show_explore_page():
    st.title("Youtube Energy Estimate Page")

    st.write("""### Explore the *Data!* :sunglasses:""")
    
    #load data
    youtube=pd.read_csv("YoutubeDataset.csv")
    
    #buttons
    head = st.button("Show top 5 records of data")
    tail = st.button("Show last 5 records of data")
    desc = st.button("Show data's description")
    corr = st.button("Show target data's correlationship")
    
    st.table("q","a","z")
    
    if head:
        st.write("""Top 5 records of data is""",youtube.head())
    elif tail:
        st.write("""Last 5 records of data is""",youtube.tail())
    elif desc:
        st.write("""Data's description is""",youtube.describe())
    elif corr:
        corr_matrix=youtube.corr()
        st.write("""Target data's correlationship is""",corr_matrix['Total_Energy(kJ)'].sort_values(ascending=False))
    
show_explore_page()
    
