import pandas as pd
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ============================================================
# Load Dataset
# ============================================================

df = pd.read_csv("data/agriculture_data.csv")


# ============================================================
# Evaluation Function
# ============================================================

def evaluate_model(model_path, target, features, categorical_features):

    print("\n" + "=" * 60)
    print(f"Evaluating: {target.upper()}")
    print("=" * 60)

    # Select features
    X = df[features].copy()
    y = df[target]

    # Convert categorical columns exactly like training
    for column in categorical_features:
        X[column] = X[column].astype("category")

    # Same train-test split as training
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Load trained model
    model = joblib.load(model_path)

    # Prediction
    predictions = model.predict(X_test)

    # Metrics
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print(f"MAE  : {mae:.2f}")
    print(f"RMSE : {rmse:.2f}")
    print(f"R²   : {r2:.4f}")

    # Sample predictions
    results = pd.DataFrame({
        "Actual": y_test.values,
        "Predicted": predictions
    })

    print("\nSample Predictions:")
    print(results.head(10).to_string(index=False))


# ============================================================
# 1. DEMAND MODEL
# ============================================================

demand_features = [
    "temperature",
    "rainfall",
    "humidity",
    "previous_demand",
    "supply",
    "base_price",
    "crop",
    "location"
]

evaluate_model(
    "models/demand_model.pkl",
    "demand",
    demand_features,
    ["crop", "location"]
)


# ============================================================
# 2. PRICE MODEL
# ============================================================

price_features = [
    "temperature",
    "rainfall",
    "humidity",
    "previous_demand",
    "supply",
    "base_price",
    "crop",
    "location"
]

evaluate_model(
    "models/price_model.pkl",
    "price",
    price_features,
    ["crop", "location"]
)


# ============================================================
# 3. LOGISTICS MODEL
# ============================================================

logistics_features = [
    "distance_km",
    "traffic_level",
    "temperature",
    "rainfall",
    "load_kg",
    "road_quality",
    "pickup_delay_min",
    "time_of_day",
    "driver_experience",
    "vehicle_type"
]

evaluate_model(
    "models/logistics_model.pkl",
    "delivery_time_min",
    logistics_features,
    ["vehicle_type"]
)