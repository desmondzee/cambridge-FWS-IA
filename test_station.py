# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_inconsistent_typical_range_stations():
    """Test inconsistent_typical_range_stations function for task 1F"""
    
    #None typical_range
    s1 = MonitoringStation(
        station_id="test-s-1",
        measure_id="test-m-1",
        label="Station None",
        coord=(52.0, 0.0),
        typical_range=None,
        river="River Test",
        town=""
    )
    
    #low >= high
    s2 = MonitoringStation(
        station_id="test-s-2",
        measure_id="test-m-2",
        label="Station Inconsistent",
        coord=(52.1, 0.1),
        typical_range=(5.0, 3.0),
        river="River Test",
        town=""
    )
    
    #low == high
    s3 = MonitoringStation(
        station_id="test-s-3",
        measure_id="test-m-3",
        label="Station Equal",
        coord=(52.2, 0.2),
        typical_range=(4.0, 4.0),  #should be inconsistent
        river="River Test",
        town=""
    )
    
    #consistent range
    s4 = MonitoringStation(
        station_id="test-s-4",
        measure_id="test-m-4",
        label="Station Consistent",
        coord=(52.3, 0.3),
        typical_range=(2.0, 5.0),
        river="River Test",
        town=""
    )
    
    stations = [s1, s2, s3, s4]
    result = inconsistent_typical_range_stations(stations)
    
    # is a list???
    assert isinstance(result, list)
    
    # inconsistent stationt are inclouded 
    assert s1 in result
    assert s2 in result
    assert s3 in result 
    
    #check inconsistent is not in
    assert s4 not in result
    
    #correct datatypes???
    for station in result:
        assert isinstance(station, MonitoringStation)
