import streamlit as st
from importlib import import_module
import importlib


# Set custom color palette and styles
st.set_page_config(
    page_title="Atlas Recovery Connect",
    page_icon="pic/logo_arc_black.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(f"""
    <style>
        body {{
            background-color: #f7f4ec;
        }}
        h1, h2, h3, h4 {{
            color: #9c544f;
        }}
        .css-1d391kg {{
            color: #1a1a1a;
        }}
        .css-h5rgaw {{
            background-color: #9c544f !important;
            color: #f7f4ec !important;
        }}
        .bubble {{
            display: inline-block;
            padding: 20px 30px;
            border-radius: 50%;
            margin: 10px;
            text-align: center;
            background-color: #f7f4ec;
            color: #9c544f;
            font-weight: bold;
            font-size: 1rem;
            cursor: pointer;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s, box-shadow 0.2s, background-color 0.2s;
        }}
        .bubble:hover {{
            transform: scale(1.1);
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.3);
            background-color: #9c544f;
            color: #f7f4ec;
        }}
        
        [data-testid="stSidebarNav"] {{
            display: none;  /* Hide the default Streamlit sidebar navigation */
        }}
        
    </style>
""", unsafe_allow_html=True)

# Add the logo at the top of the sidebar
st.sidebar.image("pic/logo_arc.png", use_column_width=True)  # Replace with your actual logo file

# Sidebar navigation menu
st.sidebar.title("Navigation")
pages = {
    "Overview": "pages.overview",
    "Cultural Heritage": "pages.emergency_response",   
    "Cooperatives": "pages.cooperatives",
    "Succesful Initiatives": "pages.actions",
    
}
selected_page = st.sidebar.selectbox("Go to", options=list(pages.keys()))

# Dynamically load the selected page
module = importlib.import_module(pages[selected_page])

module.show_page()