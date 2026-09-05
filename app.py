import streamlit as st
import pandas as pd
import joblib


# --------------------------
# Load models
# --------------------------

demand_model = joblib.load(
    "models/demand_model.pkl"
)

price_model = joblib.load(
    "models/price_model.pkl"
)

logistics_model = joblib.load(
    "models/logistics_model.pkl"
)


# --------------------------
# Page
# --------------------------

st.set_page_config(
    page_title="Agri AI",
    page_icon="🌾",
    layout="wide"
)


st.title("🌾 Agri AI Marketplace")
st.write(
    "AI-powered demand, price and logistics prediction"
)


# --------------------------
# User input
# --------------------------

st.sidebar.header("Farm / Market Information")


crop = st.sidebar.selectbox(
    "Crop",
    [
        "Tomato",
        "Onion",
        "Potato",
        "Wheat",
        "Rice"
    ]
)


location = st.sidebar.selectbox(
    "Location",
    [
        "Nashik",
        "Pune",
        "Mumbai",
        "Ahmednagar",
        "Nagpur"
    ]
)


temperature = st.sidebar.number_input(
    "Temperature °C",
    value=30.0
)


rainfall = st.sidebar.number_input(
    "Rainfall mm",
    value=10.0
)


humidity = st.sidebar.number_input(
    "Humidity %",
    value=70.0
)


previous_demand = st.sidebar.number_input(
    "Previous Demand (kg)",
    value=1500.0
)


supply = st.sidebar.number_input(
    "Available Supply (kg)",
    value=2000.0
)


base_price = st.sidebar.number_input(
    "Current Price ₹/kg",
    value=30.0
)


# Logistics

distance = st.sidebar.number_input(
    "Distance km",
    value=50.0
)


traffic = st.sidebar.slider(
    "Traffic Level",
    1,
    5,
    3
)


load = st.sidebar.number_input(
    "Load kg",
    value=1000.0
)


road_quality = st.sidebar.slider(
    "Road Quality",
    1,
    5,
    3
)


pickup_delay = st.sidebar.number_input(
    "Pickup Delay (minutes)",
    value=10.0
)


time_of_day = st.sidebar.slider(
    "Time of Day",
    0,
    23,
    12
)


driver_experience = st.sidebar.slider(
    "Driver Experience",
    1,
    10,
    5
)


vehicle_type = st.sidebar.selectbox(
    "Vehicle",
    [
        "Mini Truck",
        "Truck",
        "Tempo"
    ]
)


# --------------------------
# Prediction button
# --------------------------

if st.button("🚀 Generate AI Prediction"):

    # ----------------------
    # Demand
    # ----------------------

    demand_input = pd.DataFrame([{
        "temperature": temperature,
        "rainfall": rainfall,
        "humidity": humidity,
        "previous_demand": previous_demand,
        "supply": supply,
        "base_price": base_price,
        "crop": crop,
        "location": location
    }])

    demand_input["crop"] = (
        demand_input["crop"].astype("category")
    )

    demand_input["location"] = (
        demand_input["location"].astype("category")
    )


    predicted_demand = (
        demand_model.predict(
            demand_input
        )[0]
    )


    # ----------------------
    # Price
    # ----------------------

    price_input = pd.DataFrame([{
        "temperature": temperature,
        "rainfall": rainfall,
        "humidity": humidity,
        "previous_demand": previous_demand,
        "supply": supply,
        "base_price": base_price,
        "crop": crop,
        "location": location
    }])

    price_input["crop"] = (
        price_input["crop"].astype("category")
    )

    price_input["location"] = (
        price_input["location"].astype("category")
    )


    predicted_price = (
        price_model.predict(
            price_input
        )[0]
    )


    # ----------------------
    # Logistics
    # ----------------------

    logistics_input = pd.DataFrame([{
        "distance_km": distance,
        "traffic_level": traffic,
        "temperature": temperature,
        "rainfall": rainfall,
        "load_kg": load,
        "road_quality": road_quality,
        "pickup_delay_min": pickup_delay,
        "time_of_day": time_of_day,
        "driver_experience": driver_experience,
        "vehicle_type": vehicle_type
    }])


    logistics_input["vehicle_type"] = (
        logistics_input[
            "vehicle_type"
        ].astype("category")
    )


    predicted_time = (
        logistics_model.predict(
            logistics_input
        )[0]
    )


    # ----------------------
    # Revenue
    # ----------------------

    recommended_quantity = min(
        supply,
        predicted_demand
    )

    revenue = (
        recommended_quantity
        * predicted_price
    )


    # ----------------------
    # Display
    # ----------------------

    st.subheader("📊 AI Prediction")


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "Predicted Demand",
        f"{predicted_demand:.0f} kg"
    )


    col2.metric(
        "Expected Price",
        f"₹{predicted_price:.2f}/kg"
    )


    col3.metric(
        "Delivery Time",
        f"{predicted_time:.0f} min"
    )


    col4.metric(
        "Estimated Revenue",
        f"₹{revenue:,.0f}"
    )


    # ----------------------
    # Recommendation
    # ----------------------

    st.subheader("🤖 AI Recommendation")


    if predicted_demand > supply:

        st.success(
            "High demand expected. "
            "Consider supplying the available "
            "quantity to this market."
        )

    elif predicted_price > base_price:

        st.info(
            "Expected price is higher than "
            "the current price."
        )

    else:

        st.warning(
            "Demand/price conditions are "
            "not particularly favorable."
        )