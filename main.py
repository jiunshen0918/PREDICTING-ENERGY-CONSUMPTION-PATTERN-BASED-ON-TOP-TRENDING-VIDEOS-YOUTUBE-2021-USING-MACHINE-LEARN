import streamlit as st
from explore_page import show_explore_page
from predict_page import show_predict_page

backgroundColor="#002b36"

page = st.sidebar.selectbox("Explore or Predict", ("Explore","Predict"))

if page == "Explore":
  show_explore_page()
elif page == "Predict":
  show_predict_page()
 
