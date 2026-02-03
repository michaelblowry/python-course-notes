# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:41:45 2020

@author: mlowry
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
from scipy import misc
from scipy import integrate



def f(x):
    return  0.9 * x**4 - 4 * x**3 + 0.5 * x**2 + 11 * x - 4.5



result = misc.derivative(f, 0.7, dx=0.0000001)
print(result)


    import pandas as pd
    
    url = r'https://en.wikipedia.org/wiki/List_of_mountains_by_elevation'
    tables = pd.read_html(url)
    
    df1 = tables[0]
    df2 = tables[1]