import streamlit as st
from explore_page import show_explore_page
from predict_page import show_predict_page

st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

def sidebar():
  page = st.sidebar.selectbox("Explore or Predict", ("Explore","Predict"))
  st.sidebar.image("bongo-cat.gif")
  return page

page = sidebar()
if page == "Explore":
  show_explore_page()
elif page == "Predict":
  show_predict_page()
 
