# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    print(len(rivers))
    print(sorted(rivers)[:10])
    rivers_dict = stations_by_river(stations)
    print(f"River Aire: {list(sorted(station.name for station in rivers_dict['River Aire']))} \n")
    print(f"River Cam: {list(sorted(station.name for station in rivers_dict['River Cam']))} \n")
    print(f"River Thames: {list(sorted(station.name for station in rivers_dict['River Thames']))}")
    
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()