.. _functions:

Defining Functions
==================
Functions are a key concept for most programming languages. In mathematics, a function is an equation like this

.. math::

    f(x) = 12.8x^3 + 5x + 15

If I give a value to the function, such as ``x = 5.6``, then the function will "return" a value, in this case ``2290.8848``

Python can be used to evaluate and analyze mathematical functions. Python can also be used to write elaborate
functions that have many (even hundreds) of equations and sophisticated multi-step data analysis processes. The next section describes
how to write simple mathematical functions. The final section introduces documentation concepts and style that can be used when writing long, complicated functions.

Simple Functions
----------------
Simple functions, such as mathematical functions, can be defined with two lines.

.. nbplot::

    >>> def f(x):
    ...     return 12.8 * x**3 + 5 * x + 15

The first line begins with ``def``, meaning definition. The above function is simply called ``f`` and has one "parameter"
``x`` surrounded by parenthesis. The line ends with a colon ``:`` The second line is indented four spaces, begins with 
``return``, and is the equation. Thus, "calling" or evaluating the function *f(x)* "returns" the equation.

Anywhere after the definition, the function can be called by replacing the parameter with an "argument", which
could be a number or a variable that is referenced to a number (the variable can even have the same name as the parameter).

    >>> # Arguments are given to a function. Here the argument is 5.6.
    >>> f(5.6)
    2290.8847999999994

    >>> # Variables can be referenced to a number and given as the argument.
    >>> x = 6.2
    >>> f(x)
    3096.5984000000008

.. note::
    Like variable declarations, a function definition is overwritten by subsequent functions if the same name is used.
    Spyder gives a warning if a function is being redefined. The warning is a yellow squiggly line under the function and a
    yellow triangle in the left margin. This might not matter depending on the situation (for example a homework assignment
    with various functions that you want to call ``f``). The warning can be avoided by simply using different function names.
    For mathematical functions, simple names are preferred. Here is a list of example functions. Note Pythonic style is to
    leave two blank lines before and after functions.

    .. nbplot::

        >>> import numpy as np
        ...
        >>> def f(x):
        ...     return 12.8 * x**3 + 5 * x + 15
        ...    
        ...
        >>> def f2(theta):
        ...     return np.sin(theta) + np.cos(theta)
        ...
        ...
        >>> def f3(x):
        ...     return 3 * x**2 + 5 * np.sin(x) + 15
        ...
        ...
        >>> def z(x, y):
        ...     return 5 * x**2 + y**3
        ...
        ...
        >>> def d(t, s):
        ...     g = 32.2
        ...     return s - (0.5 * g * t**2)
        ...
        ...
        >>> def A(r):
        ...     return 2 * np.pi * r**2
        ...
        ...
        >>> def rectangle_beam(base, height):
        ...    inertia = (base * height**3)/12
        ...    return inertia
        ...


Collect Values by Appending to a List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Functions can be evaluated over a list using a ``for`` loop.

.. nbplot::

    >>> # Loop over x values and collect results in an empty list y.
    >>> x = [1, 2, 3, 4, 5]
    >>> y = []
    >>> for i in x:
    ...     result = f3(i)
    ...     result = round(result, 2)
    ...     y.append(result)
    ...
    >>> print(y)
    [22.21, 31.55, 42.71, 59.22, 85.21]


Often it is convenient ot loop over a ``range()`` or ``np.arange()``

.. nbplot::

    >>> h = 10
    >>> inertia_results = []
    >>> # Loop over base values 4 through 6.
    >>> for b in range(4, 7):
    ...     result = rectangle_beam(b, h)
    ...     inertia_results.append(result)
    ...
    ...
    >>> print(inertia_results)
    [333.3333333333333, 416.6666666666667, 500.0]

The following is an example of a nested loop. The outer loop uses a ``range()`` and the inner loop uses ``np.arange()``

.. nbplot::

    >>> inertia_results = []
    >>> # Loop over base values 4 through 6.
    >>> # And loop over height values 10 through 13.5, incremented by 0.5.
    >>> for b in range(4, 7):
    ...     for h in np.arange(10, 14, 0.5):
    ...         result = rectangle_beam(b, h)
    ...         inertia_results.append(result)
    ...
    >>> print(inertia_results)
    [333.3333333333333, 385.875, 443.6666666666667, 506.9583333333333, 576.0, 651.0416666666666, 732.3333333333334, 820.125, 416.6666666666667, 482.34375, 554.5833333333334, 633.6979166666666, 720.0, 813.8020833333334, 915.4166666666666, 1025.15625, 500.0, 578.8125, 665.5, 760.4375, 864.0, 976.5625, 1098.5, 1230.1875]

.. tip::
    If certain conditions are met, then a simple mathematical function can be evaluated over many values *without* having to use a for loop. 
    The conditions are:  (1) the function has only one argument, (2) the argument given is a a numpy array, and 
    (3) the function only uses numpy operators, such as ``np.sin(x)`` instead of other package operators like ``math.sin(x)``.
    
    .. code::
    
        >>> x = np.arange(1, 5, 1)
        >>> y = f3(x)
        >>> print(y)
        array([22.20735492, 31.54648713, 42.70560004, 59.21598752, 85.20537863])
        
    This is an amazing shortcut achieved by using a numpy array for input! Essentially, the for loop is built into the array,
    or in other words, the numpy programmers figured out a way to force a for loop to wrap around their array. 
    The result is also a numpy array, so you can do even more 
    numpy magic and round all the values in the array at the same time using ``np.round``.
       
    .. code::
    
        >>> y = np.round(f3(x), 2)
        >>> print(y)
        array([22.21, 31.55, 42.71, 59.22, 85.21])
    


Elaborate Functions
-------------------
Python can be used to write elaborate functions that have many (even hundreds) of equations and and sophisticated multi-step data analysis processes.
For example, the function below is elaborate because it has multiple input parameters, multiple lines of code, and multiple return values. For 
these reasons, it is helpful to provide a function docstring. This template for the docstring will be created automatically by Spyder.

The first line of a function docstring is a one line descriptive sentence. If more description is needed, then there should be one blank line and then the longer description.
If even more description is needed, the docstring can include Args: and Returns: with indention as shown.

.. nbplot::

    >>> def horizontal_curve(speed, grade, radius, t=2.5, a=11.5):
    ...     """
    ...     Calculates stopping sight distance and clearance offset.
    ... 
    ...     This function can be used when designing a highway to ensure safet stopping distances.
    ...     The default values for reaction time and deceleration are from the Federal Highway Administration.
    ...
    ...     Args:
    ...         speed (int): The speed of the road in mph.
    ...         grade (float): The slope of the road.
    ...         radius (float): Curve radius in feet.
    ...         t (float, optional): The reaction time in seconds. Defaults to 2.5.
    ...         a (float, optional): Acceleration or deceleration. Defaults to 11.5.
    ... 
    ...     Returns:
    ...         stopping (float): The stopping distance in feet.
    ...         offset (float): The offset cleance in feet.
    ... 
    ...     """
    ...     reaction = 1.47 * speed * t
    ...     braking = speed**2 / (30 *((a/32.2) +  grade))
    ...     stopping = reaction + braking
    ...     offset = radius * (1 - np.cos(28.65 *stopping/radius))
    ...     
    ...     return stopping, offset
    ... 


Since this function returns a tuple with two values, the results need to be "unpacked". The results could be unpacked by indexing the tuple that is returned or by unpacking directly when the function is called.

.. nbplot::

    >>> # Unpacking the tuple that is returned with indexing. 
    >>> result = horizontal_curve(65, 0, 1500)
    >>> ssd = result[0]
    >>> hso = result[1]
    ...
    >>> # Alternatively, unpacking the tuple directly when calling the function.
    >>> ssd, hso =  horizontal_curve(65, 0, 1500)
    ... 


From Procedure to Function
~~~~~~~~~~~~~~~~~~~~~~~~~~
This section shows the process of turning code into a function. The example is a function to calculate the flow of water *Q* through a partially full (open channel) pipe, such as a city storm sewer.
The parameters for the function are pipe diameter *D*, water depth *d*, slope *S*, and the roughness of the pipe *n*
(If *d* = *D*, then the pipe is full. This is called a pressurized pipe, like a city's pipes for drinking water, and
the equations are the same).


.. image:: images/open-channel-flow.png

The procedure to calculate flow is:

.. nbplot::

    >>> # An example procedure we would like to turn into a function.
    >>> D = 36
    >>> d = 8
    >>> S = 0.005
    >>> n = 0.025  
    >>> c = 1.49
    >>> D = D/12
    >>> r = D/2
    >>> d = d/12
    >>> theta = 2 * np.arccos((r-d)/r)
    >>> A = ((r**2) * (theta - np.sin(theta)))/2
    >>> P = theta * r
    >>> Rh = A/P
    >>> v = c/n * Rh**(2/3) * S**0.5
    >>> Q = v * A
    ...
    >>> print("The flow is", round(Q, 1), "cfs")
    "The flow is 2.7 cfs"

Here is the process to turn a procedure into a function:

- **Stage 1:** Write the code as a procedure.
- **Stage 2:** Test and re-test to make sure the results are correct.
- **Stage 3:** Decide what variables should be parameters (arguments).
- **Stage 4:** Indent the code and add the ``def`` line (i.e. function name and parameters).
- **Stage 5:** Determine the ``return`` value(s).
- **Stage 6:** Decide if any parameters should be given default values (must be at end of def line).
- **Stage 7:** Write a simple docstring that is a one-line descriptive sentence.
- **Stage 8:** Optionally, write a more elaborate docstring with *Args:* and *Returns:* and add other comments. 
- **Stage 9:** Change parameter names to be descriptive and then reassign their values in the function.


For the example procedure, it makes sense to have *D*, *d*, *S*, *n* be parameters 
and have the function return *Q*. Here is a first attempt for the function:

    >>> # This example function works, but a better version is shown further down.
    >>> def f(D, d, S, n):
    ...     c = 1.49
    ...     D = D/12
    ...     r = D/2
    ...     d = d/12
    ...     theta = 2 * np.arccos((r-d)/r)
    ...     A = ((r**2) * (theta - np.sin(theta)))/2
    ...     P = theta * r
    ...     Rh = A/P
    ...     v = c/n * Rh**(2/3) * S**0.5
    ...     Q = v * A
    ...     return Q
    ...
    ...
    >>> result = f(36, 8, 0.005, 0.025)
    >>> print("The flow is", round(result, 1), "cfs")


Although the function above works, it might be hard to read by someone else. Python is one of the
most popular languages in the world because it can be (and is usually) written in a way that other people can share code
very easily. The creators of Python laid out a few suggestions for writing code to make programs easy to read.
Over the years more and more suggestions have been added to create what people call *Pythonic Style*. A key idea for
good code is to use variable names that are full words and to include inline comments when a variable is first defined.  

Better code style, more comments, and better variable names can make a function easier to read by others (and by you in the
future). Below is the pipe flow function written in a more readable way. Often function names are verbs. Often people use get_something for function names.

    >>> # The same function as above but with better documentation.
    >>> # Use judgment to find the balance between too much documentation and not enough.
    ...
    ...
    >>> def get_flow(diameter, depth, slope, roughness_n=0.025):
    ...     """Calculates flow in a pipe.
    ...
    ...     Args:
    ...         diameter: Pipe diameter in inches or cm.
    ...         depth: Depth of water in inches or cm.
    ...         slope: Slope of the pipe in ft/ft or m/m
    ...         roughness_n: Manning's roughness, default corrugated metal pipe
    ...
    ...     Returns:
    ...         Q: Flow in cfs or m^3/sec
    ...
    ...     """
    ...
    ...     # Assign variables.
    ...     c = 1.49
    ...     D = diameter/12
    ...     d = depth/12
    ...     r = D/2
    ...     n = roughness_n
    ...     S = slope
    ...
    ...     # Intermediate calculations.
    ...     theta = 2 * np.arccos((r-d)/r)
    ...     A = ((r**2) * (theta - np.sin(theta)))/2  # Water flow area.
    ...     P = theta * r  # Wetted perimeter.
    ...     Rh = A/P  # Hydraulic radius
    ...
    ...     # Final calculations.
    ...     v = c/n * Rh**(2/3) * S**0.5
    ...     Q = v * A
    ...
    ...     return Q
    ...
    ...
    >>> flow = get_flow(36, 8, 0.005, 0.025)
    >>> print("The flow is", round(flow, 1), "cfs")
    The flow is 2.7 cfs

.. note::
    Python uses “positional” rules for function parameters and return output. It doesn’t matter what variable names are used when calling 
    a function, nor does it matter what variable names are used for the return results. The following are identical:
    
    .. code::
    
        >>> # The following function calls are identical.
        >>> # All that matters is the 1st, 2nd, 3rd, and 4th parameters are in the correct position.
        ...
        >>> # Example function call 1
        >>> flow = get_flow(36, 8, 0.005, 0.025)
        ...
        >>> # Example function call 2
        >>> D = 36
        >>> d = 8
        >>> S = 0.005
        >>> n = 0.025 
        >>> y = get_flow(D, d, S, n)
        ...
        >>> # Example function call 3
        >>> diameter = 36
        >>> depth = 8
        >>> slope = 0.005
        >>> roughness_n = 0.025 
        >>> Q = get_flow(diameter, depth, slope, roughness_n)       
    

The above documentation formatting is based on `Google's Python Style Guide <https://google.github.io/styleguide/pyguide.html>`_. Another
popular style is `NumPy <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/index.html#google-vs-numpy>`_.

Python style guides are long documents that discuss many items to consider. A few key items are:

- Names for functions, parameters, and variables should be (as much as possible) descriptive, full words, all lower case, and with underscores separating words.
- Funcation names should be verbs (as much as possible)
- Parameters that have default values are placed at the end of the parameter list with no space before or after ``=``.
- Blank lines within a function should be used sparingly to separate code blocks.
- Block comments should be used for complicated code blocks.
- Inline comments should be used sparingly for non-obvious descriptions.
- Inline comments should have two spaces before the ``#`` and one space afterward.
- Functions should be located together at the top of a script below the imports or in a separate module.
- Two blank lines should be placed before and after functions.
- Complicated functions should have a docstring that begins and ends with three double-quotes.
- The first line of a function docstring immediately follows the opening quotes. The closing quotes are on their own line.
- The first line of a function docstring is a **one line** descriptive sentence. If more description is needed, then there should be one blank line and then the longer description.
- Optionally for even more description, the docstring can include ``Args:`` and ``Returns:`` with indention as shown above.
- Tuples should be used to return more than one item.

See `Pythonic Style <python_essentials.html#pythonic-style>`_ for more.

.. tip::
    Better code style, more comments, and better variable names could also be used for mathematical functions. For example
    this simple function that was shown earlier

    .. nbplot::

        >>> def d(t, s):
        ...     g = 32.2
        ...     return s - (0.5 * g * t**2)
        ...
        ...

    could be defined with more clarity like this

        >>> def fall_distance(time, s=0, g=32.2):
        ...     """Calculates the travel distance of a falling object after a specified time.
        ...
        ...     Args:
        ...         time: The elapsed time in seconds.
        ...         s: Starting elevation. ft or meters to match g. Default s=0.
        ...         g: Gravitational constant on earth. Default g=32.2 ft/s^2. For metric units use g=9.8
        ...
        ...     Returns:
        ...         distance: Units depend on g.
        ...     """
        ...     distance = s - (0.5 * g * time**2)
        ...
        ...     return distance
        ...
        ...

