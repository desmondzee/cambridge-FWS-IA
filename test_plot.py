# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit tests for the plot module."""

import datetime

import matplotlib

from floodsystem.plot import plot_water_levels
from floodsystem.station import MonitoringStation


def test_plot_water_levels_returns_axes():
    """plot_water_levels returns the axes it drew on."""
    station = MonitoringStation(
        "id", "mid", "Test Station", (0, 0), (0.5, 1.5), "River", "Town"
    )
    dates = [datetime.datetime(2024, 1, 1), datetime.datetime(2024, 1, 2)]
    levels = [0.8, 1.0]
    ax = plot_water_levels(station, dates, levels)
    assert ax.get_title() == "Test Station"
    assert ax.get_xlabel() == "date"
    assert ax.get_ylabel() == "water level (m)"
