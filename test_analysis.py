# Test for Task 2F

import numpy as np
import datetime
import matplotlib.dates as mdates
from floodsystem.analysis import polyfit

def test_polyfit():
    """Test the least-squares polynomial fit."""
    
    # Create a perfect straight line
    # Equation: y = 2x + 10 (where x is days)
    # We use 3 data points
    t0 = datetime.datetime(2022, 1, 1)
    t1 = t0 + datetime.timedelta(days=1)
    t2 = t0 + datetime.timedelta(days=2)
    dates = [t0, t1, t2]
    
    # We want levels to increase by 2 each day
    levels = [10.0, 12.0, 14.0]

    # Run the polyfit function (degree 1 for a straight line)
    poly, shift = polyfit(dates, levels, 1)

    # Check the "shift"
    # The shift should be the float value of the first date
    # This prevents the "RankWarning" errors
    expected_shift = mdates.date2num(t0)
    assert np.isclose(shift, expected_shift)

    # Check the polynomial accuracy
    # Since our data is a perfect line, the fit should be exact.
    # We evaluate the polynomial at (date - shift)
    
    # Check t0 (should be 10.0)
    d0 = mdates.date2num(t0) - shift
    assert np.isclose(poly(d0), 10.0)
    
    # Check t2 (should be 14.0)
    d2 = mdates.date2num(t2) - shift
    assert np.isclose(poly(d2), 14.0)

    # Check the coefficients
    # The slope (coefficient of x^1) should be approx 2.0
    # The intercept (coefficient of x^0) should be approx 10.0
    # Note: poly.coeffs returns [slope, intercept] for degree 1
    assert np.isclose(poly.coeffs[0], 2.0)
    assert np.isclose(poly.coeffs[1], 10.0)

    print("Test analysis.polyfit passed!")

if __name__ == "__main__":
    test_polyfit()