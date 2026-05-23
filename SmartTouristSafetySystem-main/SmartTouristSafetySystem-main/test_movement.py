from movement_analysis import analyze_movement

# Example tourist movement data
speed = 25
stop_minutes = 0
zone_type = "wildlife"
current_hour = 23

alerts = analyze_movement(
    speed,
    stop_minutes,
    zone_type,
    current_hour
)

print("\nMOVEMENT ANALYSIS ALERTS\n")

for alert in alerts:

    print("Type:", alert["type"])
    print("Risk:", alert["risk"])
    print("Message:", alert["message"])
    print("-----------------------")