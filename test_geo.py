# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation


def test_stations_by_distance():
    """Test stations_by_distance function for task 1B"""
    
    # Create test stations with known coordinates
    s1 = MonitoringStation(
        station_id="test-s-1",
        measure_id="test-m-1",
        label="Station 1",
        coord=(52.2053, 0.1218),  # at Camb
        typical_range=(0.0, 1.0),
        river="",
        town=""
    )
    
    s2 = MonitoringStation(
        station_id="test-s-2",
        measure_id="test-m-2",
        label="Station 2",
        coord=(55.0, 0.1218),  # Second from Cambridge
        typical_range=(0.0, 1.0),
        river="",
        town=""
    )
    
    s3 = MonitoringStation(
        station_id="test-s-3",
        measure_id="test-m-3",
        label="Station 3",
        coord=(60.0, 0.1218),  # Thrid distance from Cambridge
        typical_range=(0.0, 1.0),
        river="",
        town=""
    )
    
    stations = [s1, s2, s3]
    p = (52.2053, 0.1218)
    
    result = stations_by_distance(stations, p)
    
    # Check that result is a list
    assert isinstance(result, list)
    
    # Check that each element is a tuple of (station, distance)
    assert len(result) == 3
    for item in result:
        assert isinstance(item, tuple)
        assert len(item) == 2
        assert isinstance(item[0], MonitoringStation) #checking datatype
        assert isinstance(item[1], float)
        assert item[1] >= 0  # Distance should be non-negative
    
    # Verify all stations are in the result
    result_stations = [s for s, _ in result]
    assert s1 in result_stations
    assert s2 in result_stations
    assert s3 in result_stations
    
    # Check ordering: s1 < s2 < s3 from Cambridge
    assert result[0][0] == s1  # Closest
    assert result[1][0] == s2  # Middle
    assert result[2][0] == s3  # Furthest
