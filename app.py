import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('model.pkl')  

st.title("Restaurant Rating Predictor")
st.markdown("Predict the **Aggregate Rating** of a restaurant.")

def user_input_features():
    st.subheader("Enter Restaurant Features")

    restaurant_id = st.number_input('Restaurant ID', min_value=0)
    restaurant_name = st.number_input('Restaurant Name (encoded)', min_value=0)
    country_code = st.number_input('Country Code', min_value=0)
    city = st.number_input('City (encoded)', min_value=0)
    address = st.number_input('Address (encoded)', min_value=0)
    locality = st.number_input('Locality (encoded)', min_value=0)
    locality_verbose = st.number_input('Locality Verbose (encoded)', min_value=0)
    longitude = st.number_input('Longitude')
    latitude = st.number_input('Latitude')
    cuisines = st.number_input('Cuisines (encoded)', min_value=0)
    avg_cost = st.number_input('Average Cost for two', min_value=0)
    currency = st.number_input('Currency (encoded)', min_value=0)
    has_table_booking = st.selectbox('Has Table booking?', ['No', 'Yes'])
    has_online_delivery = st.selectbox('Has Online delivery?', ['No', 'Yes'])
    is_delivering_now = st.selectbox('Is Delivering Now?', ['No', 'Yes'])
    switch_to_order_menu = st.selectbox('Switch to Order Menu?', ['No', 'Yes'])
    price_range = st.slider('Price Range', 1, 4, 2)
    rating_color = st.number_input('Rating Color (encoded)', min_value=0)
    rating_text = st.number_input('Rating Text (encoded)', min_value=0)
    votes = st.number_input('Votes', min_value=0)

    has_table_booking = 1 if has_table_booking == 'Yes' else 0
    has_online_delivery = 1 if has_online_delivery == 'Yes' else 0
    is_delivering_now = 1 if is_delivering_now == 'Yes' else 0
    switch_to_order_menu = 1 if switch_to_order_menu == 'Yes' else 0

    data = {
        'Restaurant ID': [restaurant_id],
        'Restaurant Name': [restaurant_name],
        'Country Code': [country_code],
        'City': [city],
        'Address': [address],
        'Locality': [locality],
        'Locality Verbose': [locality_verbose],
        'Longitude': [longitude],
        'Latitude': [latitude],
        'Cuisines': [cuisines],
        'Average Cost for two': [avg_cost],
        'Currency': [currency],
        'Has Table booking': [has_table_booking],
        'Has Online delivery': [has_online_delivery],
        'Is delivering now': [is_delivering_now],
        'Switch to order menu': [switch_to_order_menu],
        'Price range': [price_range],
        'Rating color': [rating_color],
        'Rating text': [rating_text],
        'Votes': [votes]
    }

    return pd.DataFrame(data)

input_df = user_input_features()

if st.button('Predict Aggregate Rating'):
    try:
        prediction = model.predict(input_df)
        st.success(f"Predicted Aggregate Rating: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
