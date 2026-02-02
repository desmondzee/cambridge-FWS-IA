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
