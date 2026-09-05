import pandas as pd
import joblib

from lightgbm import LGBMRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score


df = pd.read_csv(
    "data/agriculture_data.csv"
)


features = [
    "temperature",
    "rainfall",
    "humidity",
    "previous_demand",
    "supply",
    "base_price",
    "crop",
    "location"
]


X = df[features].copy()
y = df["price"]


X["crop"] = X["crop"].astype("category")
X["location"] = X["location"].astype("category")


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = LGBMRegressor(
    n_estimators=300,
    learning_rate=0.05,
    num_leaves=31,
    max_depth=8,
    random_state=42
)


model.fit(
    X_train,
    y_train,
    categorical_feature=[
        "crop",
        "location"
    ]
)


prediction = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    prediction
)

r2 = r2_score(
    y_test,
    prediction
)


print("Price Model")
print("MAE:", mae)
print("R2:", r2)


joblib.dump(
    model,
    "models/price_model.pkl"
)

print("Price model saved!")