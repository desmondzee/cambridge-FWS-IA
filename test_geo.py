# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance, rivers_with_station, stations_by_river
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
        assert item[1] >= 0  #Distance should be non-negative
    
    # Verify all stations are in the result
    result_stations = [s for s, _ in result]
    assert s1 in result_stations
    assert s2 in result_stations
    assert s3 in result_stations
    
    # Check distance to match: s1 < s2 < s3 from Cambridge
    assert result[0][0] == s1  # Closest
    assert result[1][0] == s2  # Second
    assert result[2][0] == s3  # Furthest


def test_rivers_with_station():
    """Test rivers_with_station function for task 1D"""
    
    # Create test stations with different rivers
    s1 = MonitoringStation(
        station_id="test-s-1",
        measure_id="test-m-1",
        label="Station 1",
        coord=(52.0, 0.0),
        typical_range=(0.0, 1.0),
        river="River Aire",
        town=""
    )
    
    s2 = MonitoringStation(
        station_id="test-s-2",
        measure_id="test-m-2",
        label="Station 2",
        coord=(52.1, 0.1),
        typical_range=(0.0, 1.0),
        river="River Cam",
        town=""
    )
    
    s3 = MonitoringStation(
        station_id="test-s-3",
        measure_id="test-m-3",
        label="Station 3",
        coord=(52.2, 0.2),
        typical_range=(0.0, 1.0),
        river="River Aire",  # Same river as s1
        town=""
    )
    
    s4 = MonitoringStation(
        station_id="test-s-4",
        measure_id="test-m-4",
        label="Station 4",
        coord=(52.3, 0.3),
        typical_range=(0.0, 1.0),
        river=None,  # Station with no river
        town=""
    )
    
    stations = [s1, s2, s3, s4]
    result = rivers_with_station(stations)
    
    # Check that result is a set
    assert isinstance(result, set)
    
    # Check that duplicates are removed (River Aire appears twice but should only be in set once)
    assert len(result) >= 2  # At least River Aire and River Cam
    
    # Check that River Aire is in the set (only once despite two stations)
    assert "River Aire" in result
    assert "River Cam" in result
    
    # Check that None is filtered out (stations with no river are excluded)
    assert None not in result


def test_stations_by_river():
    """Test stations_by_river function for task 1D"""
    
    # Create test stations
    s1 = MonitoringStation(
        station_id="test-s-1",
        measure_id="test-m-1",
        label="Station Aire 1",
        coord=(52.0, 0.0),
        typical_range=(0.0, 1.0),
        river="River Aire",
        town=""
    )
    
    s2 = MonitoringStation(
        station_id="test-s-2",
        measure_id="test-m-2",
        label="Station Cam 1",
        coord=(52.1, 0.1),
        typical_range=(0.0, 1.0),
        river="River Cam",
        town=""
    )
    
    s3 = MonitoringStation(
        station_id="test-s-3",
        measure_id="test-m-3",
        label="Station Aire 2",
        coord=(52.2, 0.2),
        typical_range=(0.0, 1.0),
        river="River Aire",  # Same river as s1
        town=""
    )
    
    s4 = MonitoringStation(
        station_id="test-s-4",
        measure_id="test-m-4",
        label="Station None",
        coord=(52.3, 0.3),
        typical_range=(0.0, 1.0),
        river=None,  # Station with no river
        town=""
    )
    
    stations = [s1, s2, s3, s4]
    result = stations_by_river(stations)
    
    # Check result is a dictionary
    assert isinstance(result, dict)
    
    #check River Aire has 2 stations
    assert "River Aire" in result
    assert len(result["River Aire"]) == 2
    assert s1 in result["River Aire"]
    assert s3 in result["River Aire"]
    
    # Check River Cam has 1 station
    assert "River Cam" in result
    assert len(result["River Cam"]) == 1
    assert s2 in result["River Cam"]
    
    # Check all stations in River Aire are MonitoringStation objects
    for station in result["River Aire"]:
        assert isinstance(station, MonitoringStation)
    
    # Check none is not in
    assert None not in result
