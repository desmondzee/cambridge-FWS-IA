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
    