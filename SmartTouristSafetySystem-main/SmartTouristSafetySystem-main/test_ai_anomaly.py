from ai_anomaly_detection import detect_anomaly


# Example suspicious tourist movement
result = detect_anomaly(
    speed=4,
    stop_time=1,
    hour=15
)

print("\nAI ANALYSIS RESULT\n")

print("Status:", result["status"])
print("Risk:", result["risk"])
print("Message:", result["message"])