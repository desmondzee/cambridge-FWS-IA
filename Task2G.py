# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.flood import towns_by_flood_risk
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)

    print("*** Task 2G: Flood risk by town ***\n")
    print("Criteria: Risk is based on the current water level relative to the")
    print("station's typical range")
    print("For each town take the highest relative level among all")
    print("stations in that town. Ratings:")
    print("  severe:   relative level >= 2.0")
    print("  high:     relative level >= 1.5")
    print("  moderate: relative level >= 1.0")
    print("  low:      relative level < 1.0\n")

    risk_list = towns_by_flood_risk(stations)[:20]
    print("Towns by flood risk (greatest first):")
    for town, risk in risk_list:
        print(f"  {town}: {risk}")


if __name__ == "__main__":
    run()
