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


# Task 2G: town flood risk

_RISK_ORDER = {"severe": 4, "high": 3, "moderate": 2, "low": 1}


def _relative_level_to_risk(rel):
    """Convert relative water level (fraction of typical range) to risk rating."""
    if rel >= 2.0:
        return "severe"
    if rel >= 1.5:
        return "high"
    if rel >= 1.0:
        return "moderate"
    return "low"


def towns_by_flood_risk(stations):
    """Return a list of (town_name, risk_level) for towns with at least one
    station that has valid level data. Risk is the worst (highest) risk among
    all stations in that town. Sorted by risk (severe first, then high,
    moderate, low).
    """
    town_max_rel = {}
    for s in stations:
        rel = s.relative_water_level()
        if rel is None:
            continue
        town = s.town if s.town else "Unknown"
        town_max_rel[town] = max(town_max_rel.get(town, rel), rel)
    result = [(town, _relative_level_to_risk(rel)) for town, rel in town_max_rel.items()]
    result.sort(key=lambda x: _RISK_ORDER[x[1]], reverse=True)
    return result
