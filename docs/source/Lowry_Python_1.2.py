# -*- coding: utf-8 -*-
"""
Mike Lowry
Python Assignment 1.2

"""

import numpy as np


# =============================================================================
# Problem 1. Analysis of an open channel pipe
# =============================================================================

# Input
diameter = 36  # Diameter in inches
n = 0.015  # Mannings n for material.
S = 0.005  # Slope in ft/ft
c = 1.49  # US units conversion constant
D = diameter/12
r = D/2

for depth in np.arange(1, 37, 1):
    d = depth/12
    theta = 2 * np.arccos((r-d)/r)
    A = ((r**2) * (theta - np.sin(theta)))/2  # Water flow area.
    P = theta * r  # Wetted perimeter.
    Rh = A/P  # Hydraulic radius
    
    # Final calculations.
    v = c/n * Rh**(2/3) * S**0.5
    Q = v * A
    
    print(" ")
    print("Depth is", depth, "inches and velocity is", round(v, 1), "ft/s")
    
    if v < 2.5:
        print("Warning: Velocity too slow")
    elif v > 6:
        print("Danger: Velocity too high")
    else:
        print("Acceptable velocity")















# =============================================================================
# Problem 2 Cantilever Beam Analysis
# =============================================================================
print(" ")

# Input
allowable = 20000  # Allowable stress.
E = 27000000  # Modulus of elasticity.
cost_rate = 0.62  # Cost per cubic ft.
q = 3  # Uniform load in lb/in
length = 30  # Length in feet
L = length * 12


for b in np.arange(4, 8, 1):
    for h in np.arange(12, 20, 1):
        
        # Intermediate calculations
        inertia = (b * h**3)/12 
        y = h/2
        M = (q * L**2)/2
        
        # Final calculations.
        delta = (q * L**4)/(8 * E * inertia)
        sigma = M*y/inertia
        cost = L * b * h * cost_rate
        
        print(" ")
        print(b, "x", h, "inches")
        print(cost, "Dollars")
        if sigma > allowable:
            print("Stress Danger", round(sigma, 1), "psi.")
        else:
            print("Stress OK", round(sigma, 1), "psi.")
        
        if delta > 0.5:
            print("Deflection Danger", round(delta, 1), "inches.")
        else:
            print("Deflection OK", round(delta, 1), "inches.")
            
            
 

           
            
            
            
            
            
            
            
            
            
            

# =============================================================================
# Problem 3 Retaining Wall Analysis
# =============================================================================
print(" ")
# Note to grader: 
# This solution includes printing material name and cost, which were not required.
# I will use this script in lecture to demonstrate how to use an index. i = i + 1

# Input
materials = ["Plastic", "Brick", "Concrete"]

L = 50  # Wall length.
phi = 30 # Soil friction angle.
phi = np.deg2rad(phi)  # This overwrite must be outside the loop.
gamma_soil = 100  # Specific weight of soil.
mu = 0.7  # Soil friction.
q = 25  # Additional load on soil behind the wall.

# Initialize
best_material = "initial"
best_B = 4
best_H = 12
best_cost = 99999999

for material in materials:
    if material == "Plastic":
        gamma_wall = 74
        cost_rate = 2.20
    elif material == "Brick":
        gamma_wall = 130
        cost_rate = 10.15
    elif material == "Concrete":
        gamma_wall = 150
        cost_rate = 6.45
    
    for B in np.arange(1, 4.5, 0.5):
        for H in np.arange(6, 12.5, 0.5):

            # Intermediate calculations.
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
            
            if SFOS >= 1.5 and OFOS >= 1.5:
                if cost < best_cost:
                    best_material = material
                    best_B = B
                    best_H = H
                    best_cost = cost
                    best_SFOS = SFOS
                    best_OFOS = OFOS
                    
            
print(" ")
print("Best Design is", best_material)
print(best_B, "x", best_H, "feet")
print("Cost = ", round(best_cost, 2))
print("SFOS = ", round(best_SFOS, 2))
print("OFOS = ", round(best_OFOS, 2))

     
