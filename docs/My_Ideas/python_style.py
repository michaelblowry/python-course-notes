
import numpy as np


def f(D, d, S, n):
    c = 1.49
    D = D/12
    r = D/2
    d = d/12
    theta = 2 * np.arccos((r-d)/r)
    A = ((r**2) * (theta - np.sin(theta)))/2
    P = theta * r
    Rh = A/P
    v = c/n * Rh**(2/3) * S**0.5
    Q = v * A
    return Q, v


result = f(36, 8, 0.005, 0.025)
print(result)


def pipe_flow(diameter, depth, slope, roughness_n):
    """Calculates flow and velocity in a pipe.

    Args:
        diameter: Pipe diameter in inches.
        depth: Depth of water in inches.
        slope: Slope of the pipe in ft/ft.
        roughness_n: Manning's roughness coefficient for pipe material.

    Returns:
        Q: Flow in cfs.
        v: Velocity in ft/s

    """
    c = 1.49  # Conversion constant.
    S = slope
    n = roughness_n
    D = diameter/12
    r = D/2
    d = depth/12

    theta = 2 * np.arccos((r-d)/r)
    A = ((r**2) * (theta - np.sin(theta)))/2  # Water flow area.
    P = theta * r  # Wetted perimeter.
    Rh = A/P  # Hydraulic radius

    v = c/n * Rh**(2/3) * S**0.5
    Q = v * A

    return Q, v


print(pipe_flow(36, 8, 0.005, 0.025))
