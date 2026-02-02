#task 2F

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime

def run():
    # Build and update stations
    stations = build_station_list()
    update_water_levels(stations)
    
    # Get all stations with relative level > 0, sorted descending (effectively top by level)
    ranked_stations = stations_level_over_threshold(stations, 0)
    
    # Take top 5
    top_5 = ranked_stations[:5]
    
    if len(top_5) < 5:
        print("Fewer than 5 stations with valid data.")
    
    for station, _ in top_5:
        # Fetch water level data for past 2 days
        dt = datetime.timedelta(days=2)
        dates, levels = fetch_measure_levels(station.measure_id, dt=dt)
        
        if len(dates) > 0:
            plot_water_level_with_fit(station, dates, levels, 4)
        else:
            print(f"No data available for {station.name} over the past 2 days.")

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()