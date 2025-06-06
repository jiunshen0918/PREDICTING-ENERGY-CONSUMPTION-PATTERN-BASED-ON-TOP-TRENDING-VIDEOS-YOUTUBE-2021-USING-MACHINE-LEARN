import streamlit as st
import numpy as np
import pandas as pd
import io
from PIL import Image
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

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
    new_image = image.resize((125, 190))
    st.image(new_image, caption='Lets Go!')
            
    #load data
    youtube=pd.read_csv("YoutubeDataset.csv")

    #radio
    choice = st.radio("Select a data explore way!",(
                "Top 5 records", 
                "Last 5 records", 
                "Data's information", 
                "Data's description", 
                "Target data's correlationship",
                "Plot Relation graph"))
          
    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    
    if choice=="Top 5 records":
        st.write("Top 5 records of data is")
        st.table(youtube.head())
    elif choice=="Last 5 records":
        st.write("Last 5 records of data is")
        st.table(youtube.tail())
    elif choice=="Data's information": 
        buffer = io.StringIO() #to store as memory file-like object
        youtube.info(buf=buffer) #info is a standard file object
        st.write("""Data's information is""",buffer.getvalue())
    elif choice=="Data's description":
        st.write("""Data's description is""",youtube.describe())
    elif choice=="Target data's correlationship":
        corr_matrix=youtube.corr()
        st.write("""Target data's correlationship is""",corr_matrix['Total_Energy(kJ)'].sort_values(ascending=False))
    else:
        X = youtube['Total_Energy(kJ)'].values
        y = youtube['Views'].values
        fig = plt.figure(figsize=(5, 4))
        plt.plot (X, y, 'b.', markersize=6,label='samples')
        plt.xlabel ('TotalEnergy(kJ)', fontsize=18) 
        plt.ylabel('Views', fontsize=18)
        st.plotly_chart(fig) #to create unique chart types
    
show_explore_page()
    
