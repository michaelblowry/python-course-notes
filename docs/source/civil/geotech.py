# -*- coding: utf-8 -*-
"""Geotechinical engineering module.

Provides functions for geotechnical engineering analysis and design.

By Mike Lowry.
3/25/2019

"""
import numpy as np


def gravity_retaining_wall(base, height, gamma_soil, gamma_wall, phi, mu, load):
    """Calculates SFOS, OFOS."""
    # TODO: Add better documentation.
    
    B = base
    H = height
    q = load
    W = B * H * gamma_wall
    Ka = (1 - np.sin(phi))/(1 + np.sin(phi))
    Pa = 1/2 * Ka * gamma_soil * H**2 + q * H
    FR = W * mu
    M_OT = Pa * H/3
    M_R = W * B/2
    
    # Final calculations.
    SFOS = FR/Pa
    OFOS = M_R/M_OT
    
    return SFOS, OFOS



