import json
from geopy.distance import geodesic

# Load all danger zones from JSON file
with open("danger_zones.json", "r") as file:
    danger_zones = json.load(file)


def check_danger_zone(user_lat, user_lon):

    # Tourist current location
    user_location = (user_lat, user_lon)

    alerts = []

    # Check every danger zone
    for zone in danger_zones:

        zone_location = (
            zone["latitude"],
            zone["longitude"]
        )

        # Calculate distance between tourist and zone
        distance = geodesic(
            user_location,
            zone_location
        ).meters

        # If tourist enters danger radius
        if distance <= zone["radius"]:

            # Risk level calculation
            if zone["type"] == "elephant_zone":
                risk = "HIGH"

            elif zone["type"] == "wildlife":
                risk = "HIGH"

            elif zone["type"] == "landslide":
                risk = "MEDIUM"

            elif zone["type"] == "forest":
                risk = "MEDIUM"

            else:
                risk = "LOW"

            # Generate alert
            alerts.append({
                "zone_name": zone["name"],
                "zone_type": zone["type"],
                "distance_meters": round(distance, 2),
                "risk_level": risk,
                "message": f"You entered {zone['name']}"
            })

    return alerts