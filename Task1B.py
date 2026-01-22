# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1B"""
    stations = build_station_list()
    p = (52.2053, 0.1218)
    
    # Get sorted list of (station, distance) tuples
    sorted_stations = stations_by_distance(stations, p)
    
    # Format as (station name, town, distance) tuples to the task.
    print([(s.name, s.town, d) for s, d in sorted_stations[:10]])
    print([(s.name, s.town, d) for s, d in sorted_stations[-10:]])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()