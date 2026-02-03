# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:06:31 2019

@author: mlowry
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from civil import water

from scipy import optimize
from scipy import integrate
from scipy import misc




def f(x):
#    return  0.9 * x**4 - 4 * x**3 + .5 * x**2 + 11 * x - 4.5 # Website example on mathematical page
#    return 12.8 * x**3 + 5 * x + 15 # Website example on functions page
#    return 3 * x**2 + 5 * np.sin(x) + 15 # Website example on functions page
    return -0.4*x**4 + 3 * x**3 + 0.9 * x**2 - 12 * x + 12 # Lab example
#    return x**4 - 4.9 * x**3 + 5.1 * x**2 + 5.4 * x - 6 # Assignment problem
#    return 100*np.exp(-0.2*x)
#    return x*3*-12*x**2+x
#    return -(x-6)**2 + 0.6*x +50
#    return 5 * x**3 + 2 * x**2 - 3 * x


# Website code
x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x))
plt.axis([-3, 5, -15, 10])
#plt.axhline(y=0, color='k') 


## Problem 1
#left = -10
#right = 10
#x = np.arange(left, right, 0.1)
#plt.plot(x, f(x))


#plt.axhline(y=0, color='k')
#plt.axis([-10, 10, -10, 10]) # Use this for lab and assignment
#plt.axis([left, right, -15, 10])

#result = optimize.root(f, -2)
#print(result)
#
#
result = optimize.root(f, [-2, 0.5, 2, 3.0])
print(result.x)
result = optimize.root(f, (-2, 0.5, 2, 30))
print(result.x)
result = optimize.root(f, np.array([-2, 0.5, 2, 30]))
print(result.x)
#result = optimize.root(f, 2)
#print(result.x)
result = optimize.root(f, 3)
print(result.x)


result = optimize.minimize(f, -1)
print(result)

result = optimize.minimize(f, 3)
print("Minimum = ", result.fun)
print("at x location ", result.x)

result = optimize.minimize(f, 3)

plt.axhline(y=7, color='r')


def f2(x):
    return f(x) - 7


result = optimize.minimize(f, -1.5)
min_location = result.x[0]
slope = misc.derivative(f, min_location, dx=0.0000001)
print(slope)

