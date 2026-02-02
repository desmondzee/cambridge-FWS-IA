# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime

import matplotlib.pyplot as plt

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)

    top5 = stations_highest_rel_level(stations, 5)
    dt = datetime.timedelta(days=10) #last10 days

    for station in (top5):
        dates, levels = fetch_measure_levels(station.measure_id, dt=dt)
        plot_water_levels(station, dates, levels)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
