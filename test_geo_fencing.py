from geo_fencing import check_danger_zone

# Example tourist location
tourist_lat = 11.5610
tourist_lon = 76.5350

alerts = check_danger_zone(
    tourist_lat,
    tourist_lon
)

if alerts:

    print("\nDANGER ALERTS\n")

    for alert in alerts:

        print("Zone:", alert["zone_name"])
        print("Type:", alert["zone_type"])
        print("Distance:", alert["distance_meters"], "meters")
        print("Risk:", alert["risk_level"])
        print("Message:", alert["message"])
        print("----------------------------")

else:
    print("Tourist is in safe area")