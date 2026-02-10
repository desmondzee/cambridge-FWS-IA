# Task 2F
import matplotlib.dates as mdates
import numpy as np

def polyfit(dates, levels, p):
    """
    Computes a least-squares fit of a polynomial of degree p to water level data.
    Returns a tuple (polynomial object, shift).
    """
    # Convert list of dates into floating point numbers
    x = mdates.date2num(dates)
    y = np.array(levels)

    # Shift the x-axis to avoid floating point errors (RankWarning)
    # The fit is performed on (t - t0), not t.
    shift = x[0]
    x_shifted = x - shift

    # Find coefficients of best-fit polynomial p(x)
    p_coeff = np.polyfit(x_shifted, y, p)

    # Convert coefficient into a polynomial object
    poly = np.poly1d(p_coeff)

    return poly, shift