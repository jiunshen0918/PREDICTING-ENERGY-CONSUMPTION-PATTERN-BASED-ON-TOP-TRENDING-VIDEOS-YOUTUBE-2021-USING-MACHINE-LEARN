import streamlit as st
import numpy as np
import pandas as pd
import io
from PIL import Image

# CSS for table
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

#define explore coding
def show_explore_page():
    st.title("Youtube Energy Estimate Page")

    st.write("""### Explore the *Data!* :sunglasses:""")

    #display image
    image = Image.open('Excited_Hedgehog.jpg')
    new_image = image.resize((50, 75))
    st.image(new_image)
            
    #load data
    youtube=pd.read_csv("YoutubeDataset.csv")

    #buttons
    head = st.button("Show top 5 records of data")
    tail = st.button("Show last 5 records of data")
    info = st.button("Show data's information")
    desc = st.button("Show data's description")
    corr = st.button("Show target data's correlationship")
    
    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    
    if head:
        st.write("Top 5 records of data is")
        st.table(youtube.head())
    elif tail:
        st.write("Last 5 records of data is")
        st.table(youtube.tail())
    elif info: 
        buffer = io.StringIO() #to store as memory file-like object
        youtube.info(buf=buffer) #info is a standard file object
        st.write("""Data's information is""",buffer.getvalue())
    elif desc:
        st.write("""Data's description is""",youtube.describe())
    elif corr:
        corr_matrix=youtube.corr()
        st.write("""Target data's correlationship is""",corr_matrix['Total_Energy(kJ)'].sort_values(ascending=False))
    
show_explore_page()
    
