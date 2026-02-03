# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit tests for the flood module."""

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level, towns_by_flood_risk


def test_stations_highest_rel_level_sorted_descending():
    """Stations are sorted by relative level descending."""
    def make(low, high, level):
        st = MonitoringStation("id", "mid", "S", (0, 0), (low, high), "R", "T")
        st.latest_level = level
        return st
    s1 = make(0.0, 2.0, 1.0)   # rel 0.5
    s2 = make(0.0, 1.0, 0.8)   # 0.8
    s3 = make(0.0, 1.0, 0.2)   #  0.2
    result = stations_highest_rel_level([s1, s2, s3], 3)
    assert result[0] is s2
    assert result[1] is s1
    assert result[2] is s3


def test_stations_highest_rel_level_respects_N():
    """At most N stations are returned."""
    def make(level):
        st = MonitoringStation("id", "mid", "S", (0, 0), (0.0, 1.0), "R", "T")
        st.latest_level = level
        return st
    stations = [make(0.1 * i) for i in range(5)]
    result = stations_highest_rel_level(stations, 2)
    assert len(result) == 2


def test_towns_by_flood_risk():
    """Town risk is worst station in town; sorted severe first."""
    def make(town, level, low=0.0, high=1.0):
        st = MonitoringStation("id", "mid", "S", (0, 0), (low, high), "R", town)
        st.latest_level = level
        return st
    # A: 2.1 severe B: 1.2 moderate
    stations = [
        make("Town1", 2.1),   # rel 2.1 -> severe
        make("Town1", 0.5),   # 0.5 low (same town, max wins)
        make("Town2", 1.2),   # 1.2 moderate
    ]
    result = towns_by_flood_risk(stations)
    assert result[0] == ("Town1", "severe")
    assert result[1] == ("Town2", "moderate")
