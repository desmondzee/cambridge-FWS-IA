# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides plotting functions for water level data."""

# Task 2F
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from .analysis import polyfit

def plot_water_level_with_fit(station, dates, levels, p):
    """
    Plots the water level data and the best-fit polynomial.
    """
    # Calculate the polynomial and the shift using your analysis module
    poly, shift = polyfit(dates, levels, p)

    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot original data points
    plt.plot(dates, levels, '.', label="Measured Data")

    # Create a smooth line for the polynomial
    # Use the same dates range but generate the polynomial values and apply the same time shift when evaluating the polynomial
    dates_num = mdates.date2num(dates)
    plt.plot(dates, poly(dates_num - shift), label=f"Polynomial Fit (deg {p})")

    # Plot typical range (Low and High)
    low, high = station.typical_range
    plt.axhline(low, color='r', linestyle='--', label="Typical Low")
    plt.axhline(high, color='g', linestyle='--', label="Typical High")

    # Formatting
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title(f"{station.name}: Water Level & Fit")
    plt.legend()
    plt.tight_layout()

    # Display plot
    plt.show()
    

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
