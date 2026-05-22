from flask import Flask, request, jsonify

from geo_fencing import check_danger_zone
from movement_analysis import analyze_movement
from ai_anomaly_detection import detect_anomaly
from safety_score import calculate_safety_score

app = Flask(__name__)


@app.route('/analyze', methods=['POST'])

def analyze_tourist():

    # Receive tourist data
    data = request.json

    latitude = data['latitude']
    longitude = data['longitude']

    speed = data['speed']
    stop_time = data['stop_time']
    hour = data['hour']

    # 1. Geo-fencing
    danger_alerts = check_danger_zone(
        latitude,
        longitude
    )

    # Zone type
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

    # Final response
    return jsonify({

        "geo_fencing_alerts": danger_alerts,

        "movement_alerts": movement_alerts,

        "ai_detection": ai_result,

        "safety_score": score
    })


if __name__ == '__main__':
    app.run(debug=True)