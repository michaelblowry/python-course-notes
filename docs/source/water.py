# -*- coding: utf-8 -*-
"""Water engineering module.

Provides functions for water engineering analysis and design.

@Author Mike Lowry.
3/25/2019

"""

import numpy as np

minimum_velocity = 2.5  # Below this velocity plants might begin to grow (ft/s).
maximum_velocity = 6.0  # Above this scouring damage might occur (ft/s).


def pipe(diameter, depth=None):
     """Calculates wetted perimeter and hydraulic radius in a pipe."""
     if depth is None:
         depth = diameter # Pipe flowing full.

     r = diameter/2
     theta = 2 * np.arccos((r-depth)/r)
     A = ((r**2) * (theta - np.sin(theta)))/2  # Water flow area.
     P = theta * r
     Rh = A/P
     return P, Rh


def rectangle_channel(width, depth):
     """Calculates wetted perimeter and hydraulic radius in a rectangle channel."""
     P = 2 * depth + width
     Rh = (depth * width) / (width + 2 * depth)
     return P, Rh


def trapezoid_channel(base, theta_degrees, depth):
     """Calculates wetted perimeter and hydraulic radius in a trapezoid channel."""
     theta_radians = np.radians(theta_degrees)
     P = base + 2 * (depth/np.sin(theta_radians))
     Rh = (base * depth * np.sin(theta_radians) +
           depth**2 * np.cos(theta_radians)) / (base * np.sin(theta_radians) + 2 * depth)
     return P, Rh


def triangle_channel(theta_degrees, depth):
     """Calculates wetted perimeter and hydraulic radius in a triangle channel."""
     theta_radians = np.radians(theta_degrees)
     P = (2 * depth)/np.sin(theta_radians)
     Rh = (depth * np.cos(theta_radians)) / 2
     return P, Rh


def velocity_and_flow(wetted_perimeter, hydraulic_radius, slope, roughness_n, units="US"):
     """Calculates flow and velocity of water in a pipe or open channel.

     Args:
         wetted_perimeter: Wetted perimeter in inches or cm.
         hydraulic_radius: Hydraulic radius in inches or cm.
         slope: Slope of the pipe in ft/ft or m/m
         roughness_n: Manning's roughness coefficient for pipe material.
         units: US or SI. Default is US.

     Returns:
         Q: Flow in cfs or m^3/sec
         v: Velocity in ft/s or m/sec

     """
     if units=="US":
         c = 1.49  # Conversion constant.
         P = wetted_perimeter/12
         Rh = hydraulic_radius/12
     else:
         c = 1.00
         P = wetted_perimeter/100
         Rh = hydraulic_radius/100

     n = roughness_n
     S = slope

     # Calculations.
     A = Rh * P
     v = c/n * Rh**(2/3) * S**0.5
     Q = v * A

     return v, Q




