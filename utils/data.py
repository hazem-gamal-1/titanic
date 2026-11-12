import streamlit as st
import pandas as pd

@st.cache_data
def load_data(file_path):
    """
    Load data from a CSV file.
    """
    return pd.read_csv(file_path)