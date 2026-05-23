def calculate_safety_score(
        danger_alerts,
        movement_alerts):

    score = 100

    # Reduce score for geo-fencing alerts
    score -= len(danger_alerts) * 20

    # Reduce score for movement alerts
    score -= len(movement_alerts) * 15

    # Minimum score
    if score < 0:
        score = 0

    return score