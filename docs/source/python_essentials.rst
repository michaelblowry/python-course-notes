.. _python_essentials:

Python Essentials
=================

This page includes the essentials for python.

Data Types
----------

Integer
~~~~~~~

integers are cool


Float
~~~~~~~


String
~~~~~~~


List
~~~~~~~

Dictionary
~~~~~~~~~~

NumPy Array
~~~~~~~~~~~


Pandas Dataframe
~~~~~~~~~~~~~~~~


If Statement
------------




For Loop
--------





Functions
---------



.. nbplot::

    >>> import math
    >>>
    >>> def pipe_flow(D, d, S, n):
    ...     """Calculates velocity and flow for a given depth."""
    ...     c = 1.49 # Manning conversion constant
    ...     S = slope
    ...
    ...     D = diameter_inches/12 # Diameter in ft
    ...     r = D/2 # radius
    ...
    ...     d = depth_inches/12 # Depth in ft
    ...
    ...     theta = 2 * math.acos((r-d)/r)
    ...     A = ((r**2) * (theta - math.sin(theta)))/2
    ...     Rh = (r/2) * (1 - math.sin(theta)/theta)
    ...
    ...     v = c/n * Rh**(2/3) * S**0.5
    ...
    ...     Q = v * A
    ...
    ...     return v, Q






.. code-links::