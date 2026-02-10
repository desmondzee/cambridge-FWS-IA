# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit tests for the flood module."""

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

# Test for Task 2B
def test_relative_water_level():
    """Test the relative_water_level method in MonitoringStation."""
    
    # Create a station with typical range 10.0 to 20.0
    s = MonitoringStation("s_id", "m_id", "Test Station", (0,0), (10.0, 20.0), "River", "Town")
    
    # Case 1: Level is at typical low (0.0)
    s.latest_level = 10.0
    assert s.relative_water_level() == 0.0
    
    # Case 2: Level is at typical high (1.0)
    s.latest_level = 20.0
    assert s.relative_water_level() == 1.0
    
    # Case 3: Level is exactly in the middle (0.5)
    s.latest_level = 15.0
    assert s.relative_water_level() == 0.5
    
    # Case 4: Level is outside range (e.g., flooding at 2.0)
    s.latest_level = 30.0
    assert s.relative_water_level() == 2.0

    # Case 5: Inconsistent data should return None
    s_bad = MonitoringStation("id", "m", "Bad", (0,0), (20.0, 10.0), "River", "Town")
    assert s_bad.relative_water_level() is None

def test_stations_level_over_threshold():
    """Test the filtering and sorting of stations over a threshold."""
    
    s1 = MonitoringStation("s1", "m1", "Station 1", (0,0), (10, 20), "R", "T")
    s1.latest_level = 19.0 # Rel level 0.9
    
    s2 = MonitoringStation("s2", "m2", "Station 2", (0,0), (10, 20), "R", "T")
    s2.latest_level = 11.0 # Rel level 0.1
    
    s3 = MonitoringStation("s3", "m3", "Station 3", (0,0), (10, 20), "R", "T")
    s3.latest_level = 25.0 # Rel level 1.5
    
    stations = [s1, s2, s3]
    tol = 0.8
    
    # Should return s3 (1.5) then s1 (0.9). s2 is below 0.8.
    result = stations_level_over_threshold(stations, tol)
    
    assert len(result) == 2
    assert result[0][0] == s3
    assert result[1][0] == s1
    assert result[0][1] == 1.5
    assert result[1][1] == 0.9

if __name__ == "__main__":
    test_relative_water_level()
    test_stations_level_over_threshold()
    print("All Task 2B tests passed!")
    

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
