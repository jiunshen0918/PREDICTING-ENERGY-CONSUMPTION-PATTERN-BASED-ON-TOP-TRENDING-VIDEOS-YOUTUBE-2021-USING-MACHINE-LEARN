import streamlit as st
from explore_page import show_explore_page
from predict_page import show_predict_page

def sidebar():
  st.markdown(
  """
  <style>
  .sidebar {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: blue;
  }
  </style>
  """,
    unsafe_allow_html=True,
  )
    
  page = st.sidebar.selectbox("Explore or Predict", ("Explore","Predict"))
  st.sidebar.image("bongo-cat.gif")
  return page

page = sidebar()
if page == "Explore":
  show_explore_page()
elif page == "Predict":
  show_predict_page()
 
