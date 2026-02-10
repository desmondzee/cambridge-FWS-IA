# Task 2F

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.plot import plot_water_level_with_fit

def run():
    # Build stations and update levels
    stations = build_station_list()
    update_water_levels(stations)

    # Get top 5 stations with highest relative water level
    # We can reuse the function from Task 2B, getting all stations above a low threshold (-100)
    # and then slicing the top 5.
    stations_sorted = stations_level_over_threshold(stations, -100.0)
    top_5_stations = [s[0] for s in stations_sorted[:5]]

    # Process each station
    dt = 2 # Number of days
    for station in top_5_stations:
        print(f"Plotting data for: {station.name}")
        
        # Fetch history for the last 2 days
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        
        # Plot if data exists
        if dates and levels:
            plot_water_level_with_fit(station, dates, levels, 4)
        else:
            print(f"No history data for {station.name}")

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()