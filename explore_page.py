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
    info = st.button("Show data information")
    desc = st.button("Show data description")
    
    if head:
        st.write("""Top 5 records of data is""",youtube.head())
    elif tail:
        st.write("""Last 5 records of data is""",youtube.tail())
    elif info:
        st.write("""Last 5 records of data is""",youtube.info())
    elif desc:
        st.write("""Last 5 records of data is""",youtube.describe())
    
show_explore_page()
    
