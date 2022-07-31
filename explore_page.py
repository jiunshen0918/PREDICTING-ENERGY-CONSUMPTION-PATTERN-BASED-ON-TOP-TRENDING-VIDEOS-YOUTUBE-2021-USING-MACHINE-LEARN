import streamlit as st
import pandas as pd
from matplotlib.pyplot as plt


def show_predict_page():
    st.title("Youtube Energy Estimate Page")

    st.write("""### Welcome""")
    
    ok = st.button("Show energy consumption pattern")
    
show_predict_page()
