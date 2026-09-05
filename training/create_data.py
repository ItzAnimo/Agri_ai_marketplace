import pandas as pd
import numpy as np

np.random.seed(42)

N = 5000

crops = ["Tomato", "Onion", "Potato", "Wheat", "Rice"]
locations = ["Nashik", "Pune", "Mumbai", "Ahmednagar", "Nagpur"]
vehicles = ["Mini Truck", "Truck", "Tempo"]

data = {
    "temperature": np.random.uniform(20, 40, N),
    "rainfall": np.random.uniform(0, 100, N),
    "humidity": np.random.uniform(30, 95, N),

    "previous_demand": np.random.uniform(
        500, 5000, N
    ),

    "supply": np.random.uniform(
        500, 6000, N
    ),

    "base_price": np.random.uniform(
        15, 80, N
    ),

    "distance_km": np.random.uniform(
        5, 300, N
    ),

    "traffic_level": np.random.randint(
        1, 6, N
    ),

    "load_kg": np.random.uniform(
        100, 5000, N
    ),

    "road_quality": np.random.randint(
        1, 6, N
    ),

    "pickup_delay_min": np.random.uniform(
        0, 60, N
    ),

    "time_of_day": np.random.randint(
        0, 24, N
    ),

    "driver_experience": np.random.randint(
        1, 11, N
    ),

    "crop": np.random.choice(
        crops, N
    ),

    "location": np.random.choice(
        locations, N
    ),

    "vehicle_type": np.random.choice(
        vehicles, N
    )
}

df = pd.DataFrame(data)

# -------------------------
# Generate demand
# -------------------------

df["demand"] = (
    df["previous_demand"] * 0.65
    + df["supply"] * 0.15
    - df["base_price"] * 12
    + df["rainfall"] * 2
    + np.random.normal(0, 150, N)
)

df["demand"] = df["demand"].clip(
    lower=100
)


# -------------------------
# Generate price
# -------------------------

df["price"] = (
    df["base_price"]
    + (df["demand"] / df["supply"]) * 15
    + np.random.normal(0, 3, N)
)

df["price"] = df["price"].clip(
    lower=5
)


# -------------------------
# Generate delivery time
# -------------------------

df["delivery_time_min"] = (
    df["distance_km"] * 1.5
    + df["traffic_level"] * 12
    + df["rainfall"] * 0.15
    + df["load_kg"] * 0.003
    + df["pickup_delay_min"]
    - df["road_quality"] * 5
    - df["driver_experience"] * 2
    + np.random.normal(0, 10, N)
)

df["delivery_time_min"] = df[
    "delivery_time_min"
].clip(lower=10)


# Save

df.to_csv(
    "data/agriculture_data.csv",
    index=False
)

print("Dataset created successfully!")
print(df.head())
print("\nShape:", df.shape)