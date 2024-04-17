import streamlit as st
import pandas as pd


@st.cache_data
def get_data(path: str):
    return pd.read_csv(path)
