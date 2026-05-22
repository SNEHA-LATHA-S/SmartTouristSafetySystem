from geo_fencing import check_danger_zone

from movement_analysis import analyze_movement

from ai_anomaly_detection import detect_anomaly

from safety_score import calculate_safety_score


# Example tourist data
latitude = 11.5610
longitude = 76.5350

speed = 28
stop_time = 15
hour = 23


# 1. Geo-fencing alerts
danger_alerts = check_danger_zone(
    latitude,
    longitude
)


# Get zone type
if danger_alerts:
    zone_type = danger_alerts[0]["zone_type"]
else:
    zone_type = "safe"


# 2. Movement analysis
movement_alerts = analyze_movement(
    speed,
    stop_time,
    zone_type,
    hour
)


# 3. AI anomaly detection
ai_result = detect_anomaly(
    speed,
    stop_time,
    hour
)


# 4. Safety score
score = calculate_safety_score(
    danger_alerts,
    movement_alerts
)


# FINAL OUTPUT
print("\nSMART TOURIST SAFETY REPORT\n")

print("Geo-Fencing Alerts:")
print(danger_alerts)

print("\nMovement Alerts:")
print(movement_alerts)

print("\nAI Detection:")
print(ai_result)

print("\nSafety Score:", score)