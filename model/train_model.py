import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("model/dataset.csv")

# Inputs
X = df[[
    "sleep",
    "study",
    "screen",
    "exercise",
    "stress"
]]

# Outputs
y = df[[
    "focus",
    "energy",
    "productivity",
    "burnout"
]]

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model Trained Successfully!")