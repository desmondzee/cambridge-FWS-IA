<<<<<<< HEAD
#task 2B 

def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples, each containing a station where the latest relative water level is over tol,
    and the relative water level itself. The list is sorted by the relative level in descending order.
    Only considers stations with consistent typical low/high data.
    """
    over_threshold = []
    for station in stations:
        rel_level = station.relative_water_level()
        if rel_level is not None and rel_level > tol:
            over_threshold.append((station, rel_level))
    over_threshold.sort(key=lambda x: x[1], reverse=True)
    return over_threshold
=======
# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains flood risk analysis functions."""


def stations_highest_rel_level(stations, N):
    """Return a list of N stations for highest rel water level.
    """
    low, high = 0, 1
    with_level = []
    for s in stations:
        if not s.typical_range_consistent() or s.latest_level is None:
            continue
        rel = (s.latest_level - s.typical_range[low]) / (
            s.typical_range[high] - s.typical_range[low]
        )
        with_level.append((rel, s))
    with_level.sort(key=lambda x: x[0], reverse=True)
    return [s for _, s in with_level[:N]]
>>>>>>> e385394 (feat: completed ex 2c and 2e with unit testing)
