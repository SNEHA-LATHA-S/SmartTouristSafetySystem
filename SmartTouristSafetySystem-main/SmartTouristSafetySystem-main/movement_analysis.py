from datetime import datetime


def analyze_movement(speed,
                     stop_minutes,
                     zone_type,
                     current_hour):

    alerts = []

    # 1. Panic movement detection
    if speed > 20:

        alerts.append({
            "type": "panic_movement",
            "risk": "HIGH",
            "message": "Tourist moving unusually fast"
        })

    # 2. No movement detection
    if stop_minutes >= 15:

        alerts.append({
            "type": "no_movement",
            "risk": "HIGH",
            "message": "Tourist inactive for long duration"
        })

    # 3. Tourist immobile
    if speed == 0 and stop_minutes >= 30:

        alerts.append({
            "type": "immobile",
            "risk": "CRITICAL",
            "message": "Possible injury or unconscious condition"
        })

    # 4. Night movement in forest/wildlife zones
    if current_hour >= 22 or current_hour <= 5:

        if zone_type in [
            "forest",
            "wildlife",
            "elephant_zone"
        ]:

            alerts.append({
                "type": "night_risk",
                "risk": "HIGH",
                "message": "Unsafe movement in danger zone during night"
            })

    # 5. Landslide risk
    if zone_type == "landslide" and speed > 10:

        alerts.append({
            "type": "landslide_risk",
            "risk": "MEDIUM",
            "message": "Fast movement in landslide-prone region"
        })

    return alerts