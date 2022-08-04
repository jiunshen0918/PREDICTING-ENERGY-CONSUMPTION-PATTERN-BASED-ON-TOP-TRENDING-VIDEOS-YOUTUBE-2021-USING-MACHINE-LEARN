import streamlit as st
from explore_page import show_explore_page
from predict_page import show_predict_page

def sidebar():
  st.sidebar.image("Excited_Hedgehog.jpg", use_column_width=True)
  page = st.sidebar.selectbox("Explore or Predict", ("Explore","Predict"))
  return page

page = sidebar()
if page == "Explore":
  show_explore_page()
elif page == "Predict":
  show_predict_page()
 
