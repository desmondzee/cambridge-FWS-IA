from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    """Requirements for Task 1E"""
    # Build list of stations
    stations = build_station_list()

    # Get the top 9 rivers (including ties)
    top_rivers = rivers_by_station_number(stations, 9)

    # Print result
    print(top_rivers)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()