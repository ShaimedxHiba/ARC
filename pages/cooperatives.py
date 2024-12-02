import streamlit as st
import pandas as pd
import plotly.express as px

def show_page():
    st.title("Cooperatives")
    map_html_file = "ARC_coop.html"  # Replace with your map file path
    with open(map_html_file, "r") as f:
        map_html = f.read()

    st.components.v1.html(map_html, height=600)