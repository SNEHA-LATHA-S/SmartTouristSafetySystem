from safety_score import calculate_safety_score

danger_alerts = [1]
movement_alerts = [1, 2]

score = calculate_safety_score(
    danger_alerts,
    movement_alerts
)

print("Safety Score:", score)