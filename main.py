import streamlit as st
from predict_page import show_predict_page

st.sidebar.selection("Explore or prediction",("Predict","Explore"))

show_predict_page()
