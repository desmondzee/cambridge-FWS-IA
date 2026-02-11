# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine # maths function to calculate distance between two points on the Earth

# Task 1B
def stations_within_radius(stations, centre, r):
    """
    Returns a list of all stations within radius r of a geographic coordinate centre.
    """
    within_radius = []
    
    for station in stations:
        # Calculate distance between station coordinate and centre
        distance = haversine(station.coord, centre)
        
        if distance <= r:
            within_radius.append(station)
            
    return within_radius

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



from collections import defaultdict

# Task 1E
def rivers_by_station_number(stations, N):
    """
    Returns a list of the N rivers with the greatest number of monitoring stations.
    Includes additional rivers if there is a tie at the Nth position.
    """
    # Count stations for each river
    river_counts = {}
    for station in stations:
        if station.river in river_counts:
            river_counts[station.river] += 1
        else:
            river_counts[station.river] = 1

    # Convert to list of tuples and sort by count (descending)
    # The lambda x: x[1] tells Python to sort by the count, not the name
    sorted_rivers = sorted(river_counts.items(), key=lambda x: x[1], reverse=True)

    # Handle the 'N' limit and ties
    result = sorted_rivers[:N]
    
    # Check if subsequent rivers have the same count as the Nth river
    if len(sorted_rivers) > N:
        nth_count = result[-1][1]
        for i in range(N, len(sorted_rivers)):
            if sorted_rivers[i][1] == nth_count:
                result.append(sorted_rivers[i])
            else:
                break
                
    return result