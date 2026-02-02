#task 2B 

def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples, each containing a station where the latest relative water level is over tol,
    and the relative water level itself. The list is sorted by the relative level in descending order.
    Only considers stations with consistent typical low/high data.
    """
    over_threshold = []
    for station in stations:
        rel_level = station.relative_water_level()
        if rel_level is not None and rel_level > tol:
            over_threshold.append((station, rel_level))
    over_threshold.sort(key=lambda x: x[1], reverse=True)
    return over_threshold