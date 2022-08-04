import streamlit as st
from explore_page import show_explore_page
from predict_page import show_predict_page

page = st.sidebar.selectbox("Explore or Predict", ("Explore","Predict"))

if page == "Explore":
  show_explore_page()
elif page == "Predict":
  show_predict_page()
  
"""### gif from local file"""
file_ = open("C:/Users/admin/OneDrive/FYP/UCCC3596-FYP2/bongocat.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)
