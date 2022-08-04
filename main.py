import streamlit as st
from explore_page import show_explore_page
from predict_page import show_predict_page

def sidebar():
  st.sidebar.image("/home/rzwitch/Downloads/randy-streamlit.png", use_column_width=True)
  page = st.sidebar.selectbox("Explore or Predict", ("Explore","Predict"))
  return page

page = sidebar()
if page == "Explore":
  show_explore_page()
elif page == "Predict":
  show_predict_page()
 
