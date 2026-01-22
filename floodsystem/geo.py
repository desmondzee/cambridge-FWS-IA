# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """Returns a list of stations and distances sorted by distance from a given point."""
    ouput = []
    for station in stations:
        station_distance = haversine(station.coord, p)
        ouput.append((station, station_distance))
    return sorted(ouput, key=lambda x: x[1]) #using lambda function to sort second entry in the tuple
    
def new f1():
    return True
