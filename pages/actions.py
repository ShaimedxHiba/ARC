import streamlit as st

import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static


def load_seed_data():
    november_df = pd.read_excel('seed_distribution_consolidated.xlsx', sheet_name='November 2023')
    march_df = pd.read_excel('seed_distribution_consolidated.xlsx', sheet_name='March 2024')
    return november_df, march_df

# Function to Display Map
def display_map(november_df, march_df):
    # Filter out rows with missing coordinates
    november_filtered = november_df.dropna(subset=['Latitude', 'Longitude'])
    march_filtered = march_df.dropna(subset=['Latitude', 'Longitude'])

    # Determine map center
    if not november_filtered.empty:
        center_lat = november_filtered['Latitude'].median()
        center_lon = november_filtered['Longitude'].median()
    elif not march_filtered.empty:
        center_lat = march_filtered['Latitude'].median()
        center_lon = march_filtered['Longitude'].median()
    else:
        st.warning("No valid coordinates available for map display.")
        return

    # Create Folium map
    m = folium.Map(location=[center_lat, center_lon], zoom_start=10)

    # Function to generate popup content
    def generate_popup(row):
        popup_content = f"""
        <b>Douar:</b> {row['Douar']}<br>
        <b>Commune:</b> {row['Commune']}<br>
        <b>Farmers Benefited:</b> {row['Farmers Benefited']}<br>
        """
        return popup_content

    # Add markers for November data
    for _, row in november_filtered.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=folium.Popup(generate_popup(row), max_width=300),
            icon=folium.Icon(color="blue", icon="info-sign", prefix="fa"),
        ).add_to(m)

    # Add markers for March data
    for _, row in march_filtered.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=folium.Popup(generate_popup(row), max_width=300),
            icon=folium.Icon(color="green", icon="info-sign", prefix="fa"),
        ).add_to(m)

    # Render the map in Streamlit
    folium_static(m)
# Load the Excel data
def show_page():
    # Page Title
    st.title("Initiatives Highlight")
    st.write(
        """
        The **Actions** section highlights some of the successful initiatives undertaken to support communities 
        in the Atlas region. These initiatives focus on sustainable practices and long-term recovery efforts.
        """
    )

    
    
    # Tree Planting Initiative
    st.subheader("🌳 Tree Planting Initiative")
    st.write(
        """
        Led by **ReBuild**, the tree planting initiative -Green Atlas Project- proposes planting over **1.1 million trees**, and also focuses on medicinal and aromatic plants and olive oil valorization.
        This project aims to restore deforested areas, enhance biodiversity, and support local livelihoods through 
        sustainable agriculture and inclusion, over the next 10 years. The project will start by implementing plant nurseries in some villages, in collaboration with GDF and HAF.
        """
    )
    st.image("pic/pic3.jpeg", use_column_width=True)  # Replace with your image
    

    st.title("Seed Distribution")
    st.write(
        """
        The **Seed Distribution Program** supports local farmers by providing high-quality seeds for cereals, 
        legumes, and other essential crops. This initiative empowers farmers to restore agricultural activities, 
        ensuring food security and economic recovery in affected areas.
        """
    )

    # Load data
    november_df, march_df = load_seed_data()

    # Display statistics and map
    st.subheader("Summary Statistics")
    st.write("Below are the key statistics and details of the seed distribution program for November 2023 and March 2024.")

    # Calculate total seeds distributed and display as a summary table
    november_total = november_df.drop(columns=['Latitude', 'Longitude', 'Douar', 'Commune', 'Farmers Benefited']).sum().sum()
    march_total = march_df.drop(columns=['Latitude', 'Longitude', 'Douar', 'Commune', 'Farmers Benefited']).sum().sum()

    summary_data = {
        "Month": ["November 2023", "March 2024"],
        "Total Seeds Distributed (kg)": [int(november_total), int(march_total)],
        "Total Villages": [november_df['Douar'].nunique(), march_df['Douar'].nunique()],
        "Total Farmers Benefited": [november_df['Farmers Benefited'].sum(), march_df['Farmers Benefited'].sum()],
    }
    summary_df = pd.DataFrame(summary_data)
    st.dataframe(summary_df, use_container_width=True, hide_index=True)

    # Map Display
    st.subheader("Map of Douars with Seed Distribution")
    display_map(november_df, march_df)
    # PROMET Initiative Section
    st.subheader("PROMET Initiative")
    st.write(
        """
        The **PROMET Initiative**, carried out by **GIZ**, focuses on strengthening the revival of economic activities 
        of small and medium-sized enterprises (SMEs), self-employed individuals, and female cooperatives. This initiative 
        aims to provide the necessary support and resources to rebuild sustainable livelihoods and economic resilience 
        in affected communities.
        """
    )
    st.markdown("🎯 **Goal**: Strengthening the revival of economic activities by **December 2025**.")
    st.markdown("🌟 **Key Focus Areas**:")
    st.markdown(
        """
        - Supporting female cooperatives in the Atlas region.
        - Providing capacity-building and financial assistance to SMEs.
        - Enabling self-employed individuals to regain economic stability.
        """
    )