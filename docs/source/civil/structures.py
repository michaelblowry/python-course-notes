# -*- coding: utf-8 -*-
"""Structural engineering module.

Provides functions for structural engineering analysis and design.

By Mike Lowry.
3/25/2019

"""
import numpy as np


def rectangle_beam(base, height):
    """Calculates moment of inertia for a rectangular beam."""
    inertia = (base * height**3)/12
    y = height/2
    return inertia, y


def rod_beam(diameter):
    """Calculates moment of inertia for a rod beam."""
    inertia = (np.pi * diameter**4)/64
    y = diameter/2
    return inertia, y


def pipe_beam(diameter, inside_diameter):
    """Calculates moment of inertia for a pipe beam."""
    inertia = np.pi * (diameter**4 - inside_diameter**4)/64
    y = diameter
    return inertia, y


def eye_beam(base, height, depth, thickness):
    """Calculates moment of inertia for an I beam."""
    inertia = 1/12 * (base * depth**3 -(base - thickness)*height**3)
    y = depth/2
    return inertia, y


def uniform_loaded_cantilever_beam(length, inertia, centroid_y, modulus_E, load):
    """Calculates maximum deflection and stress for cantilever beam.
    
    Args:
        length: Beam length in inches.
        inertia: inches^4.
        centroid_y: inches
        modulus_E: psi.
        load: lbf-in.

    Returns:
        delta: maximum deflection in inches
        sigma: maximum stress
    
    """
    L = length
    y = centroid_y
    E = modulus_E
    q = load
   
    M = (q * L**2)/2    
    
    delta = (q * L**4)/(8 * E * inertia)
    sigma = M*y/inertia
    return delta, sigma




