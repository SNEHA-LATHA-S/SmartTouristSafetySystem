import pandas as pd

from sklearn.ensemble import IsolationForest


# Load tourist movement data
data = pd.read_csv("tourist_movement.csv")


# Select features
features = data[[
    "speed",
    "stop_time",
    "hour"
]]


# Create AI model
model = IsolationForest(
    contamination=0.2,
    random_state=42
)


# Train AI
model.fit(features)


def detect_anomaly(speed,
                   stop_time,
                   hour):

    # New tourist movement data
    new_data = pd.DataFrame([[
        speed,
        stop_time,
        hour
    ]], columns=[
        "speed",
        "stop_time",
        "hour"
    ])

    # AI prediction
    prediction = model.predict(new_data)

    # -1 means anomaly
    if prediction[0] == -1:

        return {
            "status": "ANOMALY",
            "message": "Suspicious tourist behavior detected",
            "risk": "HIGH"
        }

    else:

        return {
            "status": "NORMAL",
            "message": "Tourist behavior normal",
            "risk": "LOW"
        }