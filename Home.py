import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="San Francisco Rental Price Prediction",
    layout='wide',
    page_icon="🏠"
)

# --- Hide Streamlit UI Elements ---
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- Theme-Adaptive CSS ---
theme_aware_style = """
    <style>
    h1, h2, h3 {
        color: var(--text-color);
        font-family: 'Segoe UI', sans-serif;
    }
    .highlight-box {
        background-color: var(--background-color);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid var(--secondary-background-color);
        margin-bottom: 30px;
    }
    .center-text {
        text-align: center;
    }
    ul {
        padding-left: 30px;
    }
    ul li {
        margin-bottom: 10px;
        color: var(--text-color);
    }
    .footer-note {
        font-size: 18px;
        line-height: 1.7;
        margin-top: 20px;
        color: var(--text-color);
    }
    p {
        color: var(--text-color);
    }
    </style>
"""
st.markdown(theme_aware_style, unsafe_allow_html=True)

# --- Centered Main Title ---
st.markdown("<h1 class='center-text'>San Francisco Rental Price Predictor 🏙️</h1>", unsafe_allow_html=True)

# --- Objective Section ---
st.markdown("""
<div class="highlight-box">
    <h3>🎯 Objective</h3>
    <p style='font-size: 18px; line-height: 1.6;'>
        Rental prices in San Francisco are influenced by several key features such as location, property size, amenities, and pet-friendliness.
        In this project, we developed a machine learning model to <b>predict the rental price of housing units in San Francisco</b> using a dataset of real rental listings.
    </p>
</div>
""", unsafe_allow_html=True)

# --- Map Section ---
st.markdown("<h2 class='center-text'>📍 Map of San Francisco Neighborhoods</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(
        "Data/SFAR_map.png",
        caption="🗺️ Neighborhoods of San Francisco - Each area has unique rental characteristics that impact pricing.",
        use_container_width=True
    )

# --- Detailed Overview Section ---
st.markdown("""
<div class="highlight-box">
    <h3>🔎 Detailed Overview</h3>
    <p style='font-size: 18px; line-height: 1.6;'>
        This application aims to assist users in estimating rental prices for homes in San Francisco by applying machine learning techniques to historical data.
        Whether you're a tenant, landlord, or analyst, this tool helps you make data-backed decisions in real estate.
    </p>
</div>
""", unsafe_allow_html=True)

# --- Features Used ---
st.markdown("""
<div class="highlight-box">
    <h3>🧩 Features Used for Prediction</h3>
    <ul style='font-size: 18px; line-height: 1.7;'>
        <li><b>Square Footage:</b> Living area in square feet.</li>
        <li><b>Bedrooms & Bathrooms:</b> Comfort and occupancy details.</li>
        <li><b>Laundry Facilities:</b> Availability of in-unit/shared laundry.</li>
        <li><b>Pet Policy:</b> Whether cats, dogs, both, or none are allowed.</li>
        <li><b>Housing Type:</b> Apartments, duplexes, or standalone homes.</li>
        <li><b>Parking Availability:</b> Includes street, garage, or no parking.</li>
        <li><b>Neighborhood/District:</b> San Francisco area with different pricing trends.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- Final Summary ---
st.markdown("""
<div class="footer-note">
    <p>
        This tool streamlines the rental estimation process and provides accurate pricing insights using advanced predictive models.
        Make smarter rental choices with confidence.
    </p>
</div>
""", unsafe_allow_html=True)

# --- Navigation ---
st.markdown("---")
st.markdown("<h3 class='center-text'>🔍 Ready to Predict Rental Prices?</h3>", unsafe_allow_html=True)

col_left, col_center, col_right = st.columns([2.2, 1, 2])
with col_center:
    st.page_link("pages/Predict.py", label="🧠 🚀 Start Prediction", icon="💡")
