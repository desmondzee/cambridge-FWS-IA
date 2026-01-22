# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """Returns a list of stations and distances sorted by distance from a given point.
    
    Args:
        stations: lMonitoringStation objects
        p: tuple of floats (latitude, longitude) for coordinate point
        
    output is (station, distance) tuples by distance from p
    """
    output = []
    for station in stations:
        station_distance = haversine(station.coord, p)
        output.append((station, station_distance))
    return sorted_by_key(output, 1)  # Sort by second entry (distance) in the tuple

def rivers_with_station(stations):
    """Returns a set of river names that have at least one monitoring station.
    
    Args: list of monitoring station objects
    output is set so no duplicates or monitoringstation objects.
    """
    rivers = set()
    for station in stations:
        if station.river is not None:  # Filter out None values
            rivers.add(station.river)
    return rivers

def stations_by_river(stations):
    """returns dictionary of river names and list of stations on that river
    
    Args: list of monitoirngstionat objects
    output is dictionary of river names keyed to list of stations on that river
    """
    rivers = {}
    for station in stations:
        if station.river is not None:  # Filter out None values
            if station.river not in rivers:
                rivers[station.river] = []
            rivers[station.river].append(station)
    return rivers
    