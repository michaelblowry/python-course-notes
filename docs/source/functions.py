# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:33:25 2020

@author: mlowry
"""
import numpy as np
# The same function as above but with better documentation.
# Use judgment to find the balance between too much documentation and not enough.


def pipe_flow(diameter, depth, slope, roughness_n, units="US"):
    """Calculates flow in a pipe.

    Args:
        diameter: Pipe diameter in inches or cm.
        depth: Depth of water in inches or cm.
        slope: Slope of the pipe in ft/ft or m/m
        roughness_n: Manning's roughness coefficient for pipe material.

    Returns:
        Q: Flow in cfs or m^3/sec

    """
    if units=="US":
        c = 1.49  # Conversion constant.
        D = diameter/12
        d = depth/12
    else:
        c = 1.00
        D = diameter/100
        d = depth/100

    # Rename variables.
    r = D/2
    n = roughness_n
    S = slope

    # Intermediate calculations.
    theta = 2 * np.arccos((r-d)/r)
    A = ((r**2) * (theta - np.sin(theta)))/2  # Water flow area.
    P = theta * r  # Wetted perimeter.
    Rh = A/P  # Hydraulic radius

    # Final calculations.
    v = c/n * Rh**(2/3) * S**0.5
    Q = v * A

    return Q


flow = pipe_flow(36, 8, 0.005, 0.025)
print("The flow is", round(flow, 1), "cfs")



# Example of filling an empty list with a for loop.
s = 10000  # Starting elevation in feet
g = 32.2  # Acceleration due to gravity
distances = []
for t in [2, 4, 6, 8, 10]:
    distance = s - (0.5  *  g * t**2)
    distance = round(distance, 1)
    distances.append(distance)

print(distances)




def rectangle_beam(base, height):
    inertia = (base * height**3)/12
    return inertia


h = 10
inertia_results = []
# Loop over base values 4 through 6.
for b in range(4, 7):
    result = rectangle_beam(b, h)
    inertia_results.append(result)


print(inertia_results)


inertia_results = []
# Loop over base values 4 through 6.
# And loop over height values 10 through 13.5, incremented by 0.5.
for b in range(4, 7):
    for h in np.arange(10, 14, 0.5):
        result = rectangle_beam(b, h)
        inertia_results.append(result)

print(inertia_results)



