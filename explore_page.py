import streamlit as st
import numpy as np
import pandas as pd

#define explore coding
def show_explore_page():
    st.title("Youtube Energy Estimate Page")

    st.write("""### Welcome""")
    
    #load data
    youtube=pd.read_csv("YoutubeDataset.csv")
    
    #buttons
    head = st.button("Show top 5 records of data")
    tail = st.button("Show last 5 records of data")
    
    if head:
        st.write("""Top 5 records of data is""",youtube.head())
    
show_explore_page()
    
