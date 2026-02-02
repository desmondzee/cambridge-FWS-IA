#task 2F
import numpy as np
import matplotlib.dates as mdates

def polyfit(dates, levels, p):
    """
    Computes a least-squares fit of a polynomial of degree p to water level data.
    Returns a tuple: (numpy.poly1d polynomial object, float shift of the date axis).
    """
    # Convert dates to floats (days since Gregorian origin)
    x = mdates.date2num(dates)
    
    if len(x) == 0:
        raise ValueError("No date data provided.")
    
    # Shift the x-axis to the first date to avoid large numbers and improve conditioning
    d0 = x[0]
    x_shifted = x - d0
    
    # Perform the fit
    p_coeff = np.polyfit(x_shifted, levels, p)
    
    # Create the polynomial object
    poly = np.poly1d(p_coeff)
    
    return poly, d0