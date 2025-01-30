import streamlit as st
import pandas as pd
import plotly.express as px

# Debugging statement to check if the file is read correctly
try:
    df = pd.read_csv("vehicles_us.csv")
    st.write("CSV file loaded successfully")
except Exception as e:
    st.write(f"Error loading CSV file: {e}")

# Debugging statement to check if df is defined
if 'df' in locals():
    df['manufacturer'] = df['model'].apply(lambda x: x.split()[0] if isinstance(x, str) and len(x.split()) > 0 else None)
    st.write("DataFrame 'df' is defined and 'manufacturer' column added")
else:
    st.write("DataFrame 'df' is not defined")