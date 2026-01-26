from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Demonstration for Task 1C: stations within radius."""

    # Build list of all monitoring stations
    stations = build_station_list()

    # Cambridge city centre coordinate (lat, lon)
    centre = (52.2053, 0.1218)

    # Radius in km
    r = 10

    # Get the stations within the radius
    stations_in_radius = stations_within_radius(stations, centre, r)

    # Extract and sort the station names alphabetically
    station_names = sorted(station.name for station in stations_in_radius)

    # Output
    print(station_names)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***\n")
    run()