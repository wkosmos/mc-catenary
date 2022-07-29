import numpy as np
def cat_point(a: float = 10, x: float = 1) -> float:
    """Calculate y of catenary given x and sag parameter a.
    
    Params:
        a (float): 'sag' of catenary
        x (float): x value at which to calculate y

    Returns:
        y (float): y value of catenary curve at given x
    
    """
    y = a * np.cosh(x / a)

    return y

def cat_curve(start_x: float = -10, end_x: float = 10, a: float = 10, step: float = 1):
    """."""
    x_range = range(start_x, end_x + 1, step)

    y_values = [cat_point(a, x) for x in x_range]

    return y_values


if __name__ == '__main__':

    test_curve = cat_curve(-20, 20, 40)

    for v in test_curve:
        print('*' * round(v))