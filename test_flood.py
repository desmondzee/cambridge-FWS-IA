# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit tests for the flood module."""

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level


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
