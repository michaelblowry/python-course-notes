# -*- coding: utf-8 -*-
"""Environmental engineering module.

Provides functions for environmental engineering analysis and design.

"""

__author__ = 'Mike Lowry'
__version__ = 1.0

import numpy as np

def detention_time(influent, height, diameter):
    """Calculates the detention time in a primary clarifier.
    
        Args:
            influent: ft^3/hr
            height: ft
            diameter: ft
                
        Returns:
            detention_time: hours
            
    """
    Q = influent
    Z = height
    D = diameter
    
    A = (np.pi * D**2)/4
    V = A * Z
    detention_time = V/Q
    return detention_time