#task 2F

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from .analysis import polyfit  # Assuming analysis is in the same package

def plot_water_level_with_fit(station, dates, levels, p):
    """
    Plots the water level data vs. dates, the best-fit polynomial of degree p,
    and horizontal lines for the typical low/high range.
    """
    if not station.typical_range_consistent() or len(dates) == 0:
        print(f"Skipping plot for {station.name}: Inconsistent data or no levels available.")
        return
    
    # Prepare the plot
    plt.figure(figsize=(10, 6))
    
    # Plot observed data points
    plt.plot(dates, levels, '.', label='Observed levels', markersize=8)
    
    # Get the polynomial fit
    poly, d0 = polyfit(dates, levels, p)
    
    # Generate a smooth curve for the fit
    x = mdates.date2num(dates)
    x_smooth = np.linspace(x.min(), x.max(), 200)
    dates_smooth = mdates.num2date(x_smooth)
    levels_fit = poly(x_smooth - d0)
    plt.plot(dates_smooth, levels_fit, '-', label=f'Best-fit polynomial (degree {p})')
    
    # Plot typical range
    low, high = station.typical_range
    plt.axhline(y=low, color='green', linestyle='--', label='Typical low')
    plt.axhline(y=high, color='red', linestyle='--', label='Typical high')
    
    # Formatting
    plt.title(f"Water Level at {station.name}")
    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides plotting functions for water level data."""

import matplotlib.pyplot as plt


def plot_water_levels(station, dates, levels):
    """Display plot water level against time for a station
    """
    fig, ax = plt.subplots()
    ax.plot(dates, levels, label="Water level")
    if station.typical_range_consistent():
        low, high = station.typical_range[0], station.typical_range[1]
        ax.axhline(low, color="gray", linestyle="--", label="Typical low")
        ax.axhline(high, color="gray", linestyle="--", label="Typical high")
    ax.set_xlabel("date")
    ax.set_ylabel("water level (m)")
    ax.set_title(station.name)
    ax.tick_params(axis="x", rotation=45)
    ax.legend()
    return ax
