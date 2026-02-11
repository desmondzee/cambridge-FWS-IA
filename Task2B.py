from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    # Build stations and update latest water level data
    stations = build_station_list()
    update_water_levels(stations)

    # Get stations with relative level over 0.8
    high_risk_stations = stations_level_over_threshold(stations, 0.8)

    # Print results in the required format: Name RelativeLevel
    for station, level in high_risk_stations:
        print(f"{station.name} {level}")

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()