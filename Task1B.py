from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1B"""
    stations = build_station_list()
    p = (52.2053, 0.1218)
    print(stations_by_distance(stations, p)[:10])
    print(stations_by_distance(stations, p)[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()