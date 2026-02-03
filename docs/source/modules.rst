.. _modules:

Making a Module or Package
==========================
A procedure (i.e. a block of code) that will be used in more than one script should be defined as a function and 
moved to a *module* so it can be imported. A collection of modules is a *package*. Modules and Packages are never "run" on their own, i.e. they are 
not used for calculations per se. Instead, they are imported into a **different** script and used by calling their functions and attributes. 
Good Pythonic style dictates that modules and packages are imported in alphabetical order at the top of the script in which they are used.

When developing code, follow these rules to decide if the code should be a.) procedure, b.) function in a script, c.) module, or d.) package:

- a.) If the code will be used only once, then there is no reason to define it as a function, so just keep it as a simple **procedure**.
- b.) If the code will be used more than once in the same script, then it should be defined as a **function** at the top of the script.
- c.) If the code will be used across multiple scripts, then it should be defined in a separate script (i.e. a **module**) to be imported.
- d.) If the code is very complex, then it should be organized across multiple scripts and placed in a folder (i.e. a **package**) to be imported. 


Modules
-------
A module is a script with functions (and classes) that can be imported and used in other scripts. 

For illustration, the module below is saved as ``water.py``. It begins with a docstring. 
The first line of the docstring should be a short name for the module, followed by a blank line. 
The next few lines of the docstring are a description of the module. Next, are any imports needed for this module (in alphabetical order). 
Next, are "attributes" or constants that can be called and used in other scripts. 
And then finally, the various functions are listed, separated by two blank lines. The module itself is never *run*,
but rather imported into other scripts.

This example module is the next stage in the development of the function shown in `Defining Functions: Python Functions <functions.html#python-functions>`_. 
The function was improved by splitting and enhancing the code for better versatility. 

The functions in this module can be used to calculate the velocity (ft/s) and flow (ft^3/s) of water through pipes and open channels. The first four  
functions return two values: wetted perimeter and hydraulic radius for different cross section types and dimensions.   

.. image:: images/open-channel-cross-sections.png

The final 
function returns two values: velocity and flow. Note this is an improvement to what is shown in `Defining Functions <functions.html#python-functions>`_ 
because (1) it allows for different cross sections and (2) can return more information.

.. nbplot::

    >>> # -*- coding: utf-8 -*-
    >>> """Water engineering module. 
    ... 
    >>> Provides functions for water engineering analysis and design.
    ... 
    >>> @Author Mike Lowry.
    >>> 3/25/2019
    ... 
    >>> """
    ... 
    >>> import numpy as np
    ... 
    >>> minimum_velocity = 2.5  # Below this velocity plants might begin to grow (ft/s). 
    >>> maximum_velocity = 6.0  # Above this scouring damage might occur (ft/s). 
    ... 
    ... 
    >>> def pipe(diameter, depth=None):
    ...      """Calculates wetted perimeter and hydraulic radius in a pipe."""  
    ...      if depth is None:  
    ...          depth = diameter # Pipe flowing full.
    ...          
    ...      r = diameter/2
    ...      theta = 2 * np.arccos((r-depth)/r)
    ...      A = ((r**2) * (theta - np.sin(theta)))/2  # Water flow area.
    ...      P = theta * r  
    ...      Rh = A/P  
    ...      return P, Rh
    ...
    ...    
    >>> def rectangle_channel(width, depth):
    ...      """Calculates wetted perimeter and hydraulic radius in a rectangle channel."""
    ...      P = 2 * depth + width  
    ...      Rh = (depth * width) / (width + 2 * depth)  
    ...      return P, Rh
    ...
    ...
    >>> def trapezoid_channel(base, theta_degrees, depth):
    ...      """Calculates wetted perimeter and hydraulic radius in a trapezoid channel."""
    ...      theta_radians = np.radians(theta_degrees)
    ...      P = base + 2 * (depth/np.sin(theta_radians))  
    ...      Rh = (base * depth * np.sin(theta_radians) + 
    ...            depth**2 * np.cos(theta_radians)) / (base * np.sin(theta_radians) + 2 * depth)
    ...      return P, Rh
    ...
    ...
    >>> def triangle_channel(theta_degrees, depth):
    ...      """Calculates wetted perimeter and hydraulic radius in a triangle channel."""
    ...      theta_radians = np.radians(theta_degrees)
    ...      P = (2 * depth)/np.sin(theta_radians)  
    ...      Rh = (depth * np.cos(theta_radians)) / 2
    ...      return P, Rh
    ...
    ...
    >>> def velocity_and_flow(wetted_perimeter, hydraulic_radius, slope, roughness_n, units="US"):
    ...      """Calculates flow and velocity of water in a pipe or open channel.
    ...
    ...      Args:
    ...          wetted_perimeter: Wetted perimeter in inches or cm.
    ...          hydraulic_radius: Hydraulic radius in inches or cm.
    ...          slope: Slope of the pipe in ft/ft or m/m
    ...          roughness_n: Manning's roughness coefficient for pipe material.
    ...          units: US or SI. Default is US.
    ...
    ...      Returns:
    ...          Q: Flow in cfs or m^3/sec
    ...          v: Velocity in ft/s or m/sec
    ...
    ...      """
    ...      if units=="US":
    ...          c = 1.49  # Conversion constant.
    ...          P = wetted_perimeter/12
    ...          Rh = hydraulic_radius/12
    ...      else:
    ...          c = 1.00
    ...          P = wetted_perimeter/100
    ...          Rh = hydraulic_radius/100
    ...
    ...      n = roughness_n
    ...      S = slope
    ...        
    ...      # Calculations.
    ...      A = Rh * P
    ...      v = c/n * Rh**(2/3) * S**0.5
    ...      Q = v * A
    ...
    ...      return v, Q
    ...
    ...




The module can be imported into a **different** python file. The functions are 
called by writing the name of the module ``.`` the name of the function. In the example 
below, the pipe function is called. It returns two values: the wetted perimeter and hydraulic radius. 
Next, those values are used in the call for the function that returns velocity and flow.

    >>> # Example import and calculation in a different script.
    >>> import water
    ...
    ...
    >>> wp, hr = water.pipe(36, 8)
    >>> vel, f = water.velocity_and_flow(wp, hr, 0.005, 0.025)
    >>> print("Velocity", round(vel, 1), "ft/s and Flow", round(f, 1), "cfs")
    Velocity 2.3 ft/s and Flow 2.7 cfs

.. note::
    Functions can return any data type, including lists and tuples. Coincidentally, all the functions in the 
    example module return two items. Often, tuples are used to return more than one item. A tuple is 
    a sequence with every item separated by a comma. The output tuple can be "unpacked" by indexing or directly when calling the function.
    
        >>> # There are two ways to "unpack" functions that return more than one item.
        ...    
        >>> # One way is to use indexing.
        >>> result = water.pipe(36, 8)
        >>> wp = result[0]
        >>> hr = result[1]        
        >>> result = water.velocity_and_flow(wp, hr, 0.005, 0.025)
        >>> velocity = result[0]
        >>> flow = result[1]
        >>> print("Velocity", round(velocity, 1), "ft/s and Flow", round(flow, 1), "cfs")
        Velocity 2.3 ft/s and Flow 2.7 cfs
        ...
        >>> # The other way is to unpack the tuple directly when calling the function.
        >>> wp, hr = water.pipe(36, 8)
        >>> vel, f = water.velocity_and_flow(wp, hr, 0.005, 0.025)
        >>> print("Velocity", round(vel, 1), "ft/s and Flow", round(f, 1), "cfs")



The module needs to be in Spyder's working directory, which by default is the same as the script's directory.

The moment you type the dot ``.`` after the module name, Spyder will pop up a window listing all the attributes and functions that are in the module 
(Some versions of Spyder require hitting Tab after the dot).

.. image:: images/civil-module.png

Likewise, when you type the open parenthesis ``(`` for a function, Spyder will pop up a window listing the function arguments.

.. image:: images/civil-module-function.png

Once a module has been imported, you can access module and function level doctrings with the built-in ``help`` function.


.. code::

    >>> import water
    ...    
    >>> help(water)
    >>> help(water.pipe)


All modules can be imported with an alias. For example, ``import water as we`` (for water engineering).   

Packages
--------
A package is a collection of modules in a folder. 

For example, the module ``water.py`` could be put in a folder called ``civil`` with other modules, such as ``environmental.py``, 
``structures.py``, ``geotech.py``, etc. Each module can then be imported using the dot format ``import civil.water`` or the  
``from ... import ...`` format (See `Python Essentials: Import Modules <python_essentials.html#import-modules>`_). 

The package folder must be in the working directory. Module and package names should be one word, all lowercase letters.

    >>> # Example import from a package of civil engineering modules.
    ...
    >>> from civil import environmental as ee
    >>> from civil import geotech
    >>> from civil import structures as se
    >>> from civil import water


.. tip::
    **Code Development:**
    Code often evolves over time. A block of code might begin as a simple sequential procedure and eventually become
    a sophisticated package with hundreds of lines of code across multiple sub-modules. The "developer" or team of developers might spend months or years, slowly building and expanding the code.

    - **Stage 1:** Write the code as a procedure.
    - **Stage 2:** Test and re-test to make sure the results are correct.
    - **Stage 3:** Decide what variables should be parameters (arguments).
    - **Stage 4:** Indent the code and add the ``def`` line (i.e. function name and parameters).
    - **Stage 5:** Determine the ``return`` value(s).
    - **Stage 6:** Decide if any parameters should be given default values (must be at end of def line).
    - **Stage 7:** Optionally, use words for parameters and reassign their values to letters within the function.
    - **Stage 8:** Write a simple docstring that is a one-line descriptive sentence.
    - **Stage 9:** Optionally, write a more elaborate docstring with *Args:* and *Returns:* and add other comments. 
    - **Stage 10:** Move the function to a module (a python file named with one word all lowercase)
    - **Stage 11:** Write docstring for the module.
    - **Stage 12:** Expand and split the function to improve module versatility.
    - **Stage 13:** Create a package by putting modules in a folder (and sub-modules in sub-folders). The folder name should be one word all lowercase. 
    - **Stage 14:** Continue to improve the functions, modules, and package.


