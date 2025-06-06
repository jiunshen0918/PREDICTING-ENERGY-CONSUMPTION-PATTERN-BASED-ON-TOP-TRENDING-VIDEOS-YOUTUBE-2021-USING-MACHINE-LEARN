import streamlit as st
from explore_page import show_explore_page
from predict_page import show_predict_page

def sidebar():
  page = st.sidebar.selectbox("Explore or Predict the energy.", ("Explore","Predict"))
  st.sidebar.image("bongo-cat.gif")
  return page

page = sidebar()
if page == "Explore":
  show_explore_page()
elif page == "Predict":
  show_predict_page()
 
