import streamlit as st
from explore_page import show_explore_page
from predict_page import show_predict_page

def _sidebar(self):
    st.sidebar.selectbox("Explore or Predict", ("Explore","Predict"))
    """Format sidebar."""
    st.sidebar.image(
        "https://github.com/compomics/deeplc/raw/master/img/deeplc_logo.png",
        width=150,
    )
    st.sidebar.markdown(self.texts.Sidebar.badges)
    st.sidebar.header("About")
    st.sidebar.markdown(self.texts.Sidebar.about, unsafe_allow_html=True)
        

page = sidebar()

if page == "Explore":
  show_explore_page()
elif page == "Predict":
  show_predict_page()
 
