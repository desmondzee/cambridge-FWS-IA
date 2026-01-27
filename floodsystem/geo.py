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
    
from math import radians, sin, cos, sqrt, atan2

def haversine(coord1, coord2):
    """
    Calculate the great-circle distance between two coordinates (lat, lon) in kilometres.
    Uses the haversine formula.
    """
    # Unpack coordinates (lat1, lon1), (lat2, lon2)
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Convert to radians
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    # Differences
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    earth_radius_km = 6371.0

    return earth_radius_km * c


def stations_within_radius(stations, centre, r):
    """
    Return a list of MonitoringStation objects that lie within radius r (km)
    of the geographic coordinate centre (lat, lon).
    """
    return [station for station in stations
            if haversine(centre, station.coord) <= r]


from collections import defaultdict


def rivers_by_station_number(stations, N):
    """
    Return a list of (river_name, number_of_stations) tuples for the N rivers
    with the greatest number of monitoring stations, sorted by number of stations
    descending (ties broken alphabetically by river name).

    If there are ties at the Nth position (multiple rivers with the same count
    as the Nth river), include all of them.
    """
    if N <= 0:
        return []

    # Count stations per river
    river_counts = defaultdict(int)
    for station in stations:
        if station.river:  # Skip stations with no river name
            river_counts[station.river] += 1

    if not river_counts:
        return []

    # Sort: descending by count, then ascending by river name
    sorted_rivers = sorted(river_counts.items(), key=lambda x: (-x[1], x[0]))

    # Find the count of the Nth river (or the last if fewer than N)
    if len(sorted_rivers) <= N:
        return sorted_rivers

    nth_count = sorted_rivers[N - 1][1]

    # Collect all rivers with count >= nth_count (preserves sort order)
    result = []
    for river, count in sorted_rivers:
        if count >= nth_count:
            result.append((river, count))
        else:
            break  # Since sorted descending, no need to continue

    return result