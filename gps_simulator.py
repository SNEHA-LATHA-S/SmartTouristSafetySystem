import time
from geo_fencing import check_danger_zone

# Simulated tourist movement
locations = [

    (11.5600, 76.5340),
    (11.5605, 76.5345),
    (11.5610, 76.5350),
    (11.5615, 76.5355)
]

for location in locations:

    lat, lon = location

    print("\nTourist Location:", lat, lon)

    alerts = check_danger_zone(lat, lon)

    if alerts:

        for alert in alerts:

            print("ALERT:", alert["message"])

    else:
        print("Safe Area")

    time.sleep(5)