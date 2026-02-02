from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data
    update_water_levels(stations)

    # Get stations with relative level over 0.8, sorted descending
    over_08 = stations_level_over_threshold(stations, 0.8)

    # Print each station name and its relative level
    for station, rel_level in over_08:
        print(f"{station.name} {rel_level}")

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()