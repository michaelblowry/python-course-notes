.. _functions:

Defining Functions
==================

This page shows .

Simple
------


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



.. nbplot::

    >>> import networkx as nx
    >>> G = nx.Graph()
    >>> def bob(x, y=5):
    ...     """
    ...     Hello
    ...     """
    ...     y = x + 1
    ...     return y



.. nbplot::

    >>> """A string"""
    >>> # A comment
    >>> class Foo(object):
    ...    def __init__(self):
    ...        bar = 42
    ...        print(bar)





.. code-links::