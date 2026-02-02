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
