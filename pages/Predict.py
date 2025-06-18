import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import joblib

# Page config
st.set_page_config(page_title="SF Rent Predictor", layout='centered', page_icon="🏠")

# Hide Streamlit branding
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        h1, h2, h3 {
            font-family: 'Segoe UI', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)


model = joblib.load('./model.pkl')

# Mapping dictionaries
laundry_map = {
    '(a) in-unit': 'in-unit',
    '(b) on-site': 'not in-unit',
    '(c) no laundry': 'not in-unit'
}
pet_map = {
    '(a) both': 'allows_dogs',
    '(b) dogs': 'allows_dogs',
    '(c) cats': 'no_dogs',
    '(d) no pets': 'no_dogs'
}
house_map = {
    '(a) single': 'single',
    '(b) double': 'multi',
    '(c) multi': 'multi'
}
district_map = {
    1.0: "west",
    2.0: "southwest",
    3.0: "southwest",
    4.0: "central",
    5.0: "central",
    6.0: "central",
    7.0: "marina",
    8.0: "north beach",
    9.0: "FiDi/SOMA",
    10.0: "southwest"
}

# Title
st.markdown("## 🏙️ San Francisco Rental Price Predictor")

# Form UI
with st.form("predict_form"):
    st.markdown("### 📝 Enter Property Details")

    col1, col2 = st.columns(2)
    with col1:
        sqft = st.number_input("Area (sqft)", value=800, min_value=100)
        beds = st.number_input("Number of Bedrooms", value=1, min_value=0)
        bath = st.number_input("Number of Bathrooms", value=1.0, min_value=0.5, step=0.5)
        laundry = st.selectbox("Laundry Type", list(laundry_map.keys()))
        pets = st.selectbox("Pet Policy", list(pet_map.keys()))
    with col2:
        housing_type = st.selectbox("Housing Type", list(house_map.keys()))
        parking = st.selectbox("Parking", ['(a) unknown', '(b) protected', '(c) off-street', '(d) no parking'])
        hood_district = st.selectbox("District (Code)", list(district_map.keys()))

    submitted = st.form_submit_button("🚀 Predict Rent")

# Prediction logic
if submitted:
    user_input = pd.DataFrame([{
        'sqft': sqft,
        'beds': beds,
        'bath': bath,
        'laundry': laundry_map[laundry],
        'pets': pet_map[pets],
        'housing_type': house_map[housing_type],
        'parking': parking,
        'hood_district': district_map[hood_district]
    }])

    input_encoded = pd.get_dummies(user_input)
    X_train_cols = model.model.exog_names

    for col in X_train_cols:
        if col not in input_encoded.columns and col != 'const':
            input_encoded[col] = 0

    input_encoded['const'] = 1.0
    input_encoded = input_encoded[X_train_cols].astype(float)

    pred_log_price = model.predict(input_encoded)[0]
    pred_price = round(np.exp(pred_log_price), 2)

    st.success(f"💲 Estimated Monthly Rent: **${pred_price}**")
