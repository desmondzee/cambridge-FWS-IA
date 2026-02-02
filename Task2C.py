# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()
    update_water_levels(stations)

    highest = stations_highest_rel_level(stations, 10)
    for station in highest:
        low, high = station.typical_range[0], station.typical_range[1]
        rel = (station.latest_level - low) / (high - low)
        print(f"{station.name}, {rel}")


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
