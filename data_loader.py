import pandas as pd
import streamlit as st

@st.cache_data
def load_rules():
    return pd.read_csv("data/fpg_rules.csv")

@st.cache_data
def load_order_segments():
    return pd.read_csv("data/order_segments.csv")

@st.cache_data
def load_user_segment_report():
    return pd.read_csv("data/user_segment_report.csv")

@st.cache_data
def load_dept_revenue():
    return pd.read_csv("data/dept_revenue.csv")