# -*- coding: utf-8 -*-
"""
Python Assignment 1.1

CE 215
Created on Wed Feb 27 12:53:27 2019
@author: Mike Lowry
"""

import numpy as np


# =============================================================================
# Problem 1. Analysis of an open channel pipe
# =============================================================================

# Input
diameter = 36  # Diameter in inches.
depth = 8  # Depth in inches.
n = 0.015  # Mannings n for material.
S = 0.005  # Slope in ft/ft
c = 1.49  # US units conversion constant

# Convert input to feet.
D = diameter/12
d = depth/12

# Intermediate calculations.
r = D/2
theta = 2 * np.arccos((r-d)/r)
A = ((r**2) * (theta - np.sin(theta)))/2  # Water flow area.
P = theta * r  # Wetted perimeter.
Rh = A/P  # Hydraulic radius.

# Final calculations.
v = c/n * Rh**(2/3) * S**0.5
Q = v * A

print(" ")
print("Velocity =", round(v, 1), "ft/s")
print("Flow =", round(Q, 1), "cfs")


# =============================================================================
# Problem 2 Cantilever Beam Analysis
# =============================================================================

# Input
b = 10  # Base in inches.
h = 12  # Height in inches.
E = 27000000  # Modulus of elasticity.
q = 3  # Uniform load in lb/in.
length = 30  # Length in feet.
cost_rate = 0.45  # Cost per cubic ft.

# Intermediate calculations
L = length * 12
inertia = (b * h**3)/12 
y = h/2
M = (q * L**2)/2

# Final calculations.
delta = (q * L**4)/(8 * E * inertia)
sigma = M*y/inertia
cost = L * b * h * cost_rate

print(" ")
print("Deflection =", round(delta, 1), "in")
print("Stress =", round(sigma, 1), "psi")
print("Cost =", round(cost, 2))


# =============================================================================
# Problem 3 Retaining Wall Analysis
# =============================================================================

# Input
L = 50  # Wall length.
B = 2  # Wall base width.
H = 7  # Wall height.
phi = 30 # Soil friction angle.
gamma_soil = 100  # Specific weight of soil.
gamma_wall = 130  # Specific weight of wall material.
mu = 0.7  # Soil friction.
q = 25  # Additional load on soil behind the wall.
cost_rate = 2.20  # Material cost.

# Intermediate calculations.
phi = np.deg2rad(phi)
W = B * H * gamma_wall
Ka = (1 - np.sin(phi))/(1 + np.sin(phi))
Pa = 1/2 * Ka * gamma_soil * H**2 + q * H
FR = W * mu
M_OT = Pa * H/3
M_R = W * B/2

# Final calculations.
SFOS = FR/Pa
OFOS = M_R/M_OT 
cost = (B * H * L) * cost_rate

print(" ")
print("SFOS =", round(SFOS, 2))
print("OFOS =", round(OFOS, 2))
print("Cost =", round(cost, 2))
