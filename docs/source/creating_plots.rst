.. _creating_plots:

Creating Plots
==============

Matplotlib is a powerful and popular package for creating plots and charts. There are many types of plots that can be created. This
webpage covers the most common: 


- ``plot`` 
- ``scatter``
- ``pie``
- ``bar``
- ``barh``


The first two are used for numeric data and the last three are used for categorical data. 
Matplotlib allows very detailed customization and formatting. This webpage only covers key formatting commands.

Plot
----

``plot`` plots y versus x with lines and/or markers (points). ``plot`` is comparable to Excel's *Scatter
with Line Chart* and *Line Chart*. 

The example below plots two series: *y1* verses *x* and *y2* verses *x*. This example demonstrates every command that 
students in my course *CE 215* are required to know. 

.. nbplot::

    >>> import matplotlib.pyplot as plt
    ...
    ...
    >>> # Example Data
    >>> x = [1, 2, 3, 4, 5]
    >>> y1 = [-3, 4.5, 2, 8, 6]
    >>> y2 = [3, 0, 0, 5, -2]
    >>> 
    >>> # Creating a plot
    >>> plt.figure(1)
    >>> plt.plot(x, y1, color='g', marker='o', linestyle='--', markersize=5, linewidth=1.5)
    >>> plt.plot(x, y2, color='r', marker='+', linestyle=':')
    >>> plt.title("Example title")
    >>> plt.xlabel("Example x axis label")
    >>> plt.ylabel("Example y axis label")
    >>> plt.legend(["Example series 1", "Example series 2"], loc='upper left')
    >>> plt.xlim(0, 6)
    >>> plt.ylim(-5, 10)
    >>> plt.axhline(y=2, color='k', linestyle="-.")
    >>> plt.axvline(x=4.5, color='m')
    >>> plt.show() 

The first line defines ``figure 1``. The next two lines add the series to the figure. 
The remaining lines add plot elements. The order of in which the elements are added 
does not matter. Order only matters for the series in order to match the legend order. 
The last line ``plt.show()`` is optional, to specify exactly when Spyder should show the figure. 
If ``plt.show()`` is not written, then Spyder will show the figure at the end of the script.

Each series is formated by using optional keywords, such as ``color``, ``marker``, etc. 
For example, ``color='g'`` makes the line green and ``marker='o'`` plots circles at the *x*, *y* points. 
If a keyword is not provided, then a default value is used. There are many possibilities for each 
keyword and there are additional keywords not shown. It is impossible to remember all the matplotlib commands, 
just as it is impossible to remember all the functions of any of large Python package. 
So the best approach is to become proficient with reading Python documentation. Here is the `documentation for plot <https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html>`_. 


Collect Values by Appending to a List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``plot`` can be used to plot a function. Consider the following `mathematical function <functions.html#mathematical-functions>`_. 
To get a list of "x" values we can use ``np.arange``. One way to get a corresponding list of *y* values is to loop 
over the numpy array and "fill" an empty *y* list.  


.. nbplot::

    >>> def f(x):
    ...     return  0.9 * x**4 - 4 * x**3 + 0.5 * x**2 + 11 * x - 4.5
    ...
    ...
    >>> x = np.arange(-10, 10, 0.1)
    >>> y = []
    >>> for i in x:
    ...     result = f(i)
    ...     y.append(result)
    ...
    >>> plt.figure(2)
    >>> plt.plot(x, y)
    >>> plt.xlim(-3, 5)
    >>> plt.ylim(-15, 10)
    >>> plt.show()


As another example, consider the function for calculating velocity and flow in an open channel that was described in 
`Defining Functions: Making Personal Modules <functions.html#making-personal-modules>`_. The code block below shows how a list 
for *x* (depth_values) and a list for *y* (flow_values) can be collected with each loop.

.. nbplot::

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> from civil import water
    ...
    ...
    >>> # Looping over a function to get x and y values
    >>> depth_values = []
    >>> flow_values = []
    >>> for depth in np.arange(1, 37, 1):
    ...     P, Rh = water.pipe(36, depth)
    ...     v, Q = water.velocity_and_flow(P, Rh, 0.003, 0.025)
    ...     depth_values.append(depth)
    ...     flow_values.append(Q)
    ...
    >>> plt.figure(3)
    >>> plt.plot(depth_values, flow_values)
    >>> plt.title("Flow in 36 inch corrugated metal pipe")
    >>> plt.xlabel("Depth (inches)")
    >>> plt.ylabel("Flow (cfs)")


In the next example, we will evaluate two functions and therefore 
fill two *y* lists. For each passing loop, a new result is appended to *y1* and *y2*. These 


.. nbplot::

    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    ...
    ...
    >>> def f(x):
    ...     return x**3 + 5 * x**2 
    ...
    ...
    >>> def g(x):
    ...     return 2 * (x+4)**2 - 12
    ...
    ...
    >>> # Create a numpy array of x values.
    >>> x = np.arange(-50, 50, 0.5)
    ...
    >>> # Define empty lists and loop over x to fill the lists.
    >>> y1 = []
    >>> y2 = []
    >>> for i in x:
    ...     result1 = f(i)
    ...     y1.append(result1)
    ...     result2 = g(i)
    ...     y2.append(result2)
    ...
    >>> # Plotting.
    >>> plt.figure(4)
    >>> plt.plot(x, y1)
    >>> plt.plot(x, y2)
    >>> plt.xlabel("x values")
    >>> plt.ylabel("y output")
    >>> plt.legend(["The first function f(x)", "The second function g(x)"], loc='upper right')
    >>> plt.xlim(-8, 4)
    >>> plt.ylim(-20, 40)


If certain conditions are met, then simple  `mathematical functions <functions.html#mathematical-functions>`_ can be plotted very easily *without* having to use a for loop. 
The conditions are:  (1) the function has only one argument, (2) the argument given is a a numpy array, and 
(3) the function only uses numpy operators, such as ``np.sin(x)`` instead of other package operators like ``math.sin(x)``.

    >>> # For certain conditions, numpy avoids the need for looping.
    >>> # Through what seems like magic, an internal loop occurs over x.
    >>> x = np.arange(-50, 50, 0.5)
    >>> y1 = f(x)
    >>> y2 = g(x)
    ... 
    >>> # Plotting mathematical functions with numpy arrays.
    >>> plt.figure(5)
    >>> plt.plot(x, y1)
    >>> plt.plot(x, y2)
    >>> plt.xlabel("x values")
    >>> plt.ylabel("y output")
    >>> plt.legend(["The first function f(x)", "The second function g(x)"], loc='upper right')
    >>> plt.xlim(-5, 10)
    >>> plt.ylim(-20, 40)


There is a short cut method for formatting a series. The syntax is color, marker, linestyle in quotes all together without spaces or commas. 
This string is given immediately after x and y. Here are some example short cut strings:


.. code::

    >>> # Example formatting short cut strings.
    >>> 'b:'    # blue, no markers, dotted line 
    >>> 'ro--'  # red, circle markers, dashed line
    >>> 'k^-.'  # black, triangle markers, dash-dot line
    >>> '+'     # default color, plus markers, no line

.. nbplot::

    >>> # Example using formatting short cut strings.
    >>> plt.figure(5)
    >>> plt.plot(x, y1, 'ro--')
    >>> plt.xlim(-5, 2)
    >>> plt.ylim(-5, 20)

.. _popup-tip:

.. tip::
    Spyder outputs plots into the console by default. This is called an Inline plot. 
    The alternative is to output each figure to a popup window. 
    Inline plots are convenient when you have multiple figures and don´t want to clutter your computer screen with popup windows. 
    
    To switch to popup windows, do the following:

    - Go to *Tools/Preferences/IPython console/Graphics*
    - Change *Graphic backend* to Automatic
    - Close (x out) the Console to restart the Kernel (Python brains)

    To switch back to Inline, do the above but change *Graphic backend* to Inline.
    
    Plots in a popup window are convenient because you can interact with the plot, like zooming in/out, panning the
    view, and changing the formatting colors and sizes.

    **Zooming in/out** is especially helpful when trying to visually identify
    locations on a curve, such as roots, minima, and maxima. Click the magnifying glass icon. Draw a rectangle with
    the left mouse button to zoom in. Draw a rectangle with
    the right mouse button to zoom out.

    **Zooming by panning** is more tricky. Click the icon that looks like a cross with arrows. The left mouse button is
    for panning. The right mouse button is for zooming. Press the right mouse button and move your mouse right or left
    to zoom in or out on the x-axis, respectively. Press the right mouse button and move your mouse up or down to
    zoom in or out on the y-axis, respectively.


Scatter Plot
------------
``scatter`` plots y versus x with markers (points). There are two reasons you would use ``scatter`` instead of ``plot``. 1. Because the x values
are not in consecutive order, like with observed data used for regression modeling or 2. Because you want the points to vary
in size or color (sometimes called bubbled chart).

.. nbplot::

    >>> # Example Data
    >>> x = [0.83, 1.09, 1.41, 0.99, 2.5, 2.4, 0.64, 0.75, 2.71]
    >>> y = [38, 36, 28, 58, 35, 22, 56, 43, 27]
    ... 
    >>> # Creating a scatter plot.
    >>> plt.figure(6)
    >>> plt.scatter(x, y, color='r', marker='+')
    >>> plt.title("Example Scatter Plot")
    >>> plt.xlabel("Example x axis label")
    >>> plt.ylabel("Example y axis label")
    >>> plt.show()






Pie Chart
---------
``pie`` plots x as wedges of a pie. The size of each wedge is based on the value of x. Wedge size = x/sum(x).

Think of x as the value for each category.

.. nbplot::

    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    ... 
    >>> x = [20500, 8500, 7500, 2000, 3000, 3500, 5000]  # Expenditure amount.
    ... 
    >>> # The basic pie chart is simply each wedge size determined from a list of values. 
    >>> plt.figure(7)
    >>> plt.pie(x)
    >>> plt.show()

There are various optional keyword arguments that can enhance a pie chart. Two commonly used optional arguments are ``labels``, which needs to be in the 
exact same order as the pie wedge values, and ``autopct='%0.0f%%'``.

.. nbplot::

    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    ... 
    >>> categories = ["Housing", "Car", "Food", "Savings", "Entertainment", "Medical", "Other"]
    >>> x = [20500, 8500, 7500, 2000, 3000, 3500, 5000]  # Expenditure amount.
    ... 
    >>> plt.figure(8)
    >>> plt.pie(x, labels=categories, autopct='%0.0f%%')
    >>> plt.show()

Alternatively, the categories could be defined in a legend and then use ``labels=x`` to place the values on the wedges. 
The following is a pie chart with various visual enhancements.

.. nbplot::

    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    ... 
    >>> categories = ["Housing", "Car", "Food", "Savings", "Entertainment", "Medical", "Other"]
    >>> x = [20500, 8500, 7500, 2000, 3000, 3500, 5000]  # Expenditure amount.
    ... 
    >>> plt.figure(9)
    >>> e = [0, 0.1, 0, 0, 0, 0, 0.2]
    >>> plt.pie(x, labels=x, explode=e, autopct='%0.0f%%', shadow=True)
    >>> plt.axis("equal")
    >>> plt.legend(categories, bbox_to_anchor=(1, 0.8))
    >>> plt.title("Budget")
    >>> plt.show()


Bar Chart
---------
``bar`` creates a vertical bar chart. (This is called a Column Chart in Excel). 

Each bar is a category along the x axis with a height on the y axis. In other words, we plot bar height=y for each category x.  (This notation is different than matplotlib, see the note below.) 
So, in the example below, we rename categories to be called x and the values are y. **The order for x and y must match**.

.. nbplot::

    >>> # Example bar chart with errorbars showing the range.
    >>> categories = ["Housing", "Car", "Food", "Savings", "Entertainment", "Medical", "Other"]
    >>> x = categories
    >>> y = [20500, 8500, 7500, 2000, 3000, 3500, 5000]  # Expenditure amount.
    ... 
    >>> plt.figure(10)
    >>> plt.bar(x, height=y, color='r')
    >>> plt.xticks(rotation=30)
    >>> plt.title("Budget")
    >>> plt.xlabel("Category")
    >>> plt.ylabel("Dollars")
    >>> plt.ylim(1500, 25000)    
    >>> plt.show()


We might want to add error marks to each bar tip. These will be applied against the y values, with the keyword ``yerr`` 
and their size is determined by ``capsize``. 

.. nbplot::

    >>> plt.figure(11)
    >>> error = [200, 600, 500, 150, 800, 600, 1000]
    >>> plt.bar(x, y, color='r', yerr=error, capsize=5)
    >>> plt.show()



Horizontal Bar Chart
--------------------

Use ``barh`` to create a horizontal bar chart.  

Each bar is a category along the y axis with a width on the x axis.  In other words, we plot bar width=x for each category y. (This notation is different than matplotlib, see the note below.) 
So, in the example below, we rename categories to be called y and the values are x. **The order for x and y must match**.


.. nbplot::

    >>> plt.figure(12)
    >>> categories = ["Housing", "Car", "Food", "Savings", "Entertainment", "Medical", "Other"]
    >>> y = categories
    >>> x = [20500, 8500, 7500, 2000, 3000, 3500, 5000]  # Expenditure amount.
    >>> error = [200, 600, 500, 150, 800, 600, 1000]
    >>> plt.barh(y, width=x, xerr=error, capsize=10)
    >>> plt.title("Horizontal Bar Chart")
    >>> plt.ylabel("Category")
    >>> plt.xlabel("Dollars")
    >>> plt.xlim(1000, 25000)  
    >>> plt.show()


The errorbars for a horizontal bar chart are in the x direction so the keyword is ``xerr``.
 
For ``bar`` and ``barh`` the error could be a low and high value, i.e. a non uniform range. In this case, 
the error keyword should be given a list of two lists.  

.. nbplot::

    >>> plt.figure(13)
    >>> categories = ["Housing", "Car", "Food", "Savings", "Entertainment", "Medical", "Other"]
    >>> y = categories
    >>> x = [20500, 8500, 7500, 2000, 3000, 3500, 5000]  # Expenditure amount.
    >>> low_error = [200, 5000, 200, 10, 800, 600, 100]
    >>> high_error = [300, 5000, 200, 150, 0, 50, 8000]
    >>> error = [low_error, high_error]
    >>> plt.barh(y, width=x, xerr=error, capsize=10)
    >>> plt.title("Horizontal Bar Chart with Non Uniform Error Marks")
    >>> plt.ylabel("Category")
    >>> plt.xlabel("Dollars")
    >>> plt.xlim(1000, 25000)  
    >>> plt.show()

    
.. note::  
    Pay careful attention to the order of *x* and *y* when using ``matplotlib``. The documentation and parameter order can be confusing.
    
    Typically we refer to a plot as *y* **vs** *x* (vertical axis **vs** horizontal axis). However, note the parameter order for ``plot`` and ``scatter`` is written as ``(x, y)``. 
    
    For categorical data we think of *categories* and *values*. 
    - For ``pie`` the parameter order is ``(values, categories)``. 
    - For a vertical bar chart, we can think of y = values and x = categories. For ``bar`` the parameter order is ``(categories, values)``. 
    - For a horizontal bar chart, we can think of y = categories and x = values. Yet, for ``barh`` the parameter order is still ``(categories, values)``
     


Stacked Bar Chart
-----------------
Stacked bar charts can be done with ``bar`` and ``barh``. 
To create a "stacked bar chart", simply plot the taller series first and the smaller series second.

For example, suppose there was an increase in the annual expenditures and we want to plot the new values stacked ontop of the 
original values. The increase for each category is: [12000, 4000, 2500, 300, 1600, 800, 1900].

We will need to first create a new list for the new total expenditures by adding the increase to the original values.     
We use ``range(0, len(sequence))`` to loop over the indices of the values and fill a new list using append 
(there is an easier way with numpy arrays, but the goal here is to demonstrate ``range(0, len(sequence))``, 
which is an important ``for`` loop concept. See `For Loop <if_statement_for_loop.html#for-loop>`_).

.. nbplot::

    >>> # Example of looping over the indices of a sequence.
    >>> categories = ["Housing", "Car", "Food", "Savings", "Entertainment", "Medical", "Other"]
    >>> x = categories
    >>> y = [20500, 8500, 7500, 2000, 3000, 3500, 5000]  # Expenditure amount.
    >>> y_increase = [12000, 4000, 2500, 300, 1600, 800, 1900] 
    >>> new_y = []
    >>> for i in range(0, len(y)):
    ...     increase = y[i] + y_increase[i]
    ...     new_y.append(increase)
    ...
    >>> # Example of a stacked bar chart.
    >>> plt.figure(14)
    >>> plt.bar(x, height=new_y, color='k')  # The taller bars first, in back.
    >>> plt.bar(x, height=y, color='r')  # The shorter bars second, in front.
    >>> plt.xticks(rotation=30)
    >>> plt.title("Stacked Bar Chart")
    >>> plt.xlabel("Category")
    >>> plt.ylabel("Dollars")
    >>> plt.legend(["Increase", "Original"], bbox_to_anchor=(1, 0.8))
    >>> plt.show()




