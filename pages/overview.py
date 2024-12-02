import streamlit as st

def show_page():
    # Page title
    st.title("Atlas Recovery Connect")
    st.image("pic/pic1.jpeg", use_column_width=True)  # Replace with your image
    

    # Introduction
    st.header("Introduction")
    st.write(
        """
        In the wake of the devastating earthquake that struck the Atlas region, emerged **Atlas Recovery Connect**,
        a digital solution that aims to accelerate the recovery process by consolidating, 
        mapping, and analyzing data from all the organizations involved in mid-to-long-term projects in the Atlas region.
        By keeping track 
        of "who did what, where, and when" ARC documentes the recovery journet and promotes collaboration, 
        ultimately rebuilding a stronger Atlas, together.

        
        """
    )
    # Styling bubbles
    st.markdown(
        """
        <div style="display: flex; justify-content: space-around; margin-top: 20px;">
            <div class="bubble">Collaborate</div>
            <div class="bubble">Document</div>
            <div class="bubble">Analyze</div>
            <div class="bubble">Rebuild</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br><br>", unsafe_allow_html=True)
    

    # Challenges
    st.header("Motivation")
    # Create columns for statistics
    col1, col2, col3, col4 = st.columns(4)

    # Statistics in each column
    with col1:
        st.metric("Buildings Damaged", "100,000+")
        st.metric("Villages Affected", "890+")

    with col2:
        st.metric("Schools Impacted", "300+")
        st.metric("Hospitals Impacted", "15+")

    with col3:
        st.metric("Students Disrupted", "50,000+")
        st.metric("Individuals Displaced", "500,000")

    with col4:
        st.metric("Economic Losses", "+50 billion")
        
    
    st.divider() 
    
    # Key Statistics
    st.header("Data Key Statistics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("NGOs in Contact", "40+")  # Replace with dynamic data
    with col2:
        st.metric("Projects Documented", "120+")  # Replace with dynamic data

    # Categories Section
    st.header("Scope of interest")
    st.write(
        """
        Explore the main areas of interest in rebuilding efforts. These include critical domains essential to restoring 
        communities and infrastructure after the disaster.
        """
    )

    # Bubble Section
    st.markdown(
        """
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 20px;">
            <div class="bubble">Architecture</div>
            <div class="bubble">Education</div>
            <div class="bubble">Infrastructure</div>
            <div class="bubble">Water</div>
            <div class="bubble">Medical & Health Services</div>
            <div class="bubble">Livelihoods & Economic Recovery</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Custom CSS for the bubbles
    st.markdown(
        """
        <style>
            .bubble {
                display: inline-block;
                padding: 20px 30px;
                border-radius: 50%;
                background-color: #9c544f;
                color: white;
                font-weight: bold;
                font-size: 1rem;
                text-align: center;
                cursor: pointer;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
                transition: transform 0.2s, box-shadow 0.2s;
            }
            .bubble:hover {
                transform: scale(1.1);
                box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.3);
                background-color: #7a3e3c; /* Slightly darker shade for hover */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Key Supporters
    st.divider()
    st.header("Key Supporters")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("pic/logo_gdf.png", width=200)
       
    with col2:
        st.image("pic/logo_rebuild.png", width=200)  # Replace with your logo file
    with col3:
        st.image("pic/logo_ebf.png", width=200)

    st.markdown(
    """
    <footer style='text-align: center; font-style: italic; font-size: 1.2rem; margin-top: 50px;'>
        Uniting for a stronger Atlas
    </footer>
    """,
    unsafe_allow_html=True,
    )    
    
    
   

    
    
