from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    """Demonstration for Task 1E: rivers by number of stations."""

    # Build list of all monitoring stations
    stations = build_station_list()

    # Get the top 9 rivers (plus ties)
    N = 9
    rivers = rivers_by_station_number(stations, N)

    # Output
    print(rivers)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***\n")
    run()