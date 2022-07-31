import streamlit as st
import pickle 
import numpy as np

def load_model():
    with open('saved.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

lin_reg = data["model"]
totalenergy = data["totalenergy"]
views = data["views"]

def show_predict_page():
    st.title("Youtube Energy Estimate Page")

    st.write("""### Welcome""")
    
    ok = st.button("Show energy consumption pattern")
    if ok:
