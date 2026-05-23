import time
from movement_analysis import analyze_movement

# Simulated tourist movement data
movement_data = [

    {
        "speed": 5,
        "stop_minutes": 0,
        "zone_type": "safe",
        "hour": 14
    },

    {
        "speed": 22,
        "stop_minutes": 0,
        "zone_type": "wildlife",
        "hour": 23
    },

    {
        "speed": 0,
        "stop_minutes": 20,
        "zone_type": "forest",
        "hour": 21
    }
]

for data in movement_data:

    print("\nAnalyzing Tourist Movement...\n")

    alerts = analyze_movement(
        data["speed"],
        data["stop_minutes"],
        data["zone_type"],
        data["hour"]
    )

    if alerts:

        for alert in alerts:

            print("ALERT:", alert["message"])

    else:
        print("Tourist movement normal")

    time.sleep(5)