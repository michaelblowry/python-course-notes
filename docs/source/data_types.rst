..  -*- coding: utf-8 -*-

.. _data_types:

Data Types
==========
All computer languages have a way to structure and store data. The data types in 
Python are similar to other languages. You can determine the data type of anything with the built-in function ``type()``.

.. nbplot::

    >>> x = 4
    >>> type(x)
    int
    ...
    >>> y = [1, 5, 6, 22]
    >>> type(y)
    list

In my course *CE 215* students use the 10 most common data types:

- Integer
- Floating point
- String
- List
- Tuple
- Set
- NumPy array
- Dictionary
- NumPy matrix
- Pandas DataFrame


The code block below shows all 10 of the most common data types. The subsequent 
sections provide more information for each. The final section explains the concept of ``class`` and ``object``, because each data type is, in fact, a ``class``.

.. nbplot::

    >>> import numpy as np
    >>> import pandas as pd
    ...
    >>> # The following are examples of data types commonly used 
    >>> # for engineering, science, and data analysis.
    ...
    >>> # Basic data types
    >>> x1 = 5  # Integer.
    >>> x2 = 5.3  # Floating point.
    >>> x3 = "Hello World"  # String.
    ...
    >>> # Sequence data types
    >>> x4 = [12, 5, 8]  # List.
    >>> x5 = (12, 5, 8) # Tuple.
    >>> x6 = {12, 5, 8, 8, 8} # Set.
    >>> x7 = np.array([12, 5, 8]) # NumPy array.
    ...
    >>> # Lookup, Rectangular, and Spreadsheet-like data types.
    >>> x8 = {"plastic": 0.009, "steel": 0.012, "concrete": 0.015}  # Dictionary.
    >>> x9 = np.array([[12, 5, 8],  # NumPy matrix.
    ...               [5, 2, 6]])
    >>> url_csv_file = "https://www.webpages.uidaho.edu/~mlowry/ExampleData/alcohol_data.csv"
    >>> x10 = pd.read_csv(url_csv_file) # Pandas DataFrame.

.. tip::
    All of the above data types, except ``set``, can be viewed in Sypder's Variable explorer. 
    To view the example, write ``x6`` in the console, the output will be ``{5, 8, 12}``.


Integer, Float, and String
--------------------------
The most **basic data types** are *Integer*, *Floating Point*, and *String*. The names for these data types might seem odd, 
but they have a long history in computer programming. The first two are simply numbers.

Integer and Floating Point
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. nbplot::

    >>> diameter = 4  # This is an integer.
    >>> type(diameter)
    int

    >>> depth = 8.6  # This is a floating point (because it has a decimal point).
    >>> velocity = 5.0  # This is also a floating point.
    >>> type(velocity)
    float

    >>> # If at least one float is included anywhere in a math operation,
    >>> # then the result will be a float.
    >>> bearing_stress = 4 * (12 + 3.5)
    62.0


For someone new to computer programming it might seem strange to distinguish between an ``int`` and ``float``. There 
are many reasons why this distinction is important, one reason is that in computer programming we often repeat 
things for a certain number of times. For example you might want to do a calculation for ``n = 5`` times, but it 
doesn't make sense to do something for ``n = 6.2`` times. For the latter, if you tell Python to repeat ``n`` times it will throw an error.


String
~~~~~~
*String* is computer-speak for text, i.e. words. A string is defined by using single-quotes or double-quotes. 
This is not to be confused with comments and docstrings which the computer ignores when you *Run* your program. 
In Spyder docstrings and strings are given the same color green so they appear similar. However, they are very different. 
A docstring provides information to someone reading the script and has no purpose when the script is *Run*. On the other hand, 
a string is actually used or analyzed when the script is *Run*. For example, you might want the script to print messages.

.. nbplot::

    >>> # The strings below are used to print a message.
    >>> allowable_stress = 50
    >>> success_message = "The bearing stress is below the limit."
    >>> fail_message = "Warning: The bearing stress exceeds the limit."
    >>> if bearing_stress >= allowable_stress:
    ...     print(fail_message)
    >>> else:
    ...     print(success_message)
    'Warning: The bearing stress exceeds the limit.'


The use of double-quotes or single-quotes does not matter. For example, ``material = "concrete"`` 
and ``material = 'concrete'`` are identical as far as Python is concerned. Most style guides make no preference. 
Some people like to use single-quotes for short strings and double-quotes for long sentences. I tend to use double quotes for everything.

As you do more and more programming you will find that string manipulation is a common task. There are lots of things that can be done to strings, such as the following:

    >>> message = "The pipe material: plastic"
    ...
    >>> message = message.replace("plastic", "concrete")
    ...
    >>> print(message)
    'The pipe material: concrete'
    ...
    >>> parts = message.split(" ")  # Creates a list with space as the deliminator.
    ...
    >>> print(parts)
    ['The', 'pipe', 'material:', 'concrete']
    ...
    >>> parts = message.split(":")  # Creates a list with colon as the deliminator.
    ['The pipe material', ' concrete']

The characters of a string can be accessed as follows. This can be confusing and takes trial and error to master.

    >>> caption = "The program started 18/01/1977"
    >>> letter = caption[4]  # The fourth character from the left starting with 0.
    'm'
    >>> start_date = caption[-10:]  # Keep from the right 10 characters.
    '18/01/1977'
    >>> day_month = start_date[:5]  # Keep from the left 5 characters.
    '18/01'
    >>> month = int(day_month[3:])  # Remove from the left 3 characters.
    1


List, Tuple, Set, and Numpy Array
---------------------------------
List, Tuple, Set, and Numpy Array are **sequence data types** (also called "collection" or "compound" data types).


List
~~~~
As the name implies, a ``list`` contains a list of integers, floats, or strings. 
The items in a list are separated by commas and a list is defined with square brackets ``[ ]``.

    >>> # An example of a list.
    >>> x = [12, 4, 56, 34, 11, 11, 62]

The items of a list can be accessed by putting the desired index in brackets. **In Python indexing starts at zero** and this is often a challenge for beginners to remember.

    >>> # Example of accessing an item with its index.
    >>> # The first item is accessed with index 0.
    >>> x[0]
    12
    >>> # The second item is accessed with index 1.
    >>> x[1]
    4
    >>> # A list can be "sliced" to get a subset of the items.
    >>> # Items are sliced with a colon : between indices.
    >>> # The slice is from the start index until but not including the end index.
    >>> x[2:5]
    [56, 34, 11]

Lists can be combined.

    >>> # Example of combining lists.
    >>> y = [44, 5, 66]
    >>> z = x + y
    >>> print(z)
    [12, 4, 56, 34, 11, 11, 62, 44, 5, 66]

You can add new items at the end of a list by using the ``append()`` method.

    >>> # Example of appending a new item to the end of a list.
    >>> k = [12, 55, 12, 45]
    >>> k.append(77)
    >>> print(k)
    [12, 55, 12, 45, 77]

Various functions can be used to explore a list. Here are a few ways to explore a list.

    >>> # Determine the length or number of items.
    >>> len(x)
    7
    >>> # Determine the maximum value (for numeric lists).
    >>> max(x)
    62
    >>> # Determine the minimum value (for numeric lists).
    >>> min(x)
    4
    >>> # Calculate the sum (for numeric lists).
    >>> sum(x)
    190

.. note::
    A function is used by putting the list between the parentheses, such as ``len(x)``. 
    A method is used by putting a dot after the list and then writing parentheses with the argument (if an argument is needed), such as ``x.append(77)``.
    

There are other methods for a list. Here are a few other methods.

.. nbplot::

    >>> x = [12, 4, 56, 34, 11, 11, 62]
    >>> # Sort the items of the list.
    >>> x.sort()
    >>> print(x)
    [4, 11, 11, 12, 34, 56, 62]
     >>> # Reverse the items of the list.
    >>> x.reverse()
    >>> print(x)
    [62, 56, 34, 12, 11, 11, 4]
    >>> # Count the number of times an item appears in the list.
    >>> x.count(11)
    2

The items of a list can be any data type, such as integer, float, strings, etc.

    >>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

.. tip::
    Sequence data types such as ``list`` are often given plural variable names for good Pythonic style, 
    like ``values = [12, 34, 66]`` or ``measurements = [1.2, 5.1, 4.4, 1.7]``.


Often we want to loop over a list.  Python’s ``for`` statement iterates over the items of any sequence (list, tuple, etc), 
in the order that they appear in the sequence (See `Controlling Flow: For Loop <if_statement_for_loop.html#for-loop>`_).

.. nbplot::

    >>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    >>> # Example looping over a list.
    >>> for fruit in fruits:
    ...     print(fruit)
    orange
    apple
    pear
    banana
    kiwi
    apple
    banana
    ...
    >>> # Example of looping over a list and filling a new list with append.
    >>> measurements_inches = [12, 4, 56, 34, 11, 11, 62]
    >>> measurements_cms = []  # This is an empty list that will be filled with append.
    >>> for m in measurements_inches:
    ...     measurements_cms.append(m * 2.5)
    ...
    >>> print(measurements_cms)
    [30.0, 10.0, 140.0, 85.0, 27.5, 27.5, 155.0]


Tuple
~~~~~
A ``tuple`` is very similar to a list. In fact, you may never notice the difference. For someone who is a beginner 
programmer the only difference is that a tuple is defined with curved parentheses or with no braces at all.

    >>> # Example of defining a tuple.
    >>> x = (12, 34, 56)
    (12, 34, 56)
    >>> # Tuples can also be defined without parentheses.
    >>> # The ouput in the console will show the parentheses.
    >>> y = 22, 45, 99
    (22, 45, 99)

Functions that return more than one item often use tuples. For example, ``divmod(a, b)`` returns 
a tuple consisting of the quotient and remainder of ``a`` divided by ``b``.

    >>> # Example of a function that returns a tuple.
    ...
    >>> # The result can be "unpacked" using indexing.
    >>> result = divmod(10, 3)
    >>> print(result)
    (3, 1)
    ...
    >>> q = result[0]
    >>> r = result[1]
    >>> print("quotient =", q, "and remainder =", r)
    quotient = 3 and remainder = 1
    ...
    >>> # Alternatively, the tuple can be "unpacked" directly when calling the function.
    >>> q, r = divmod(10, 3)
    >>> print("quotient =", q, "and remainder =", r)
    quotient = 3 and remainder = 1


Set
~~~

A ``set`` is like a list but with unique values (no duplicates). It is defined with curly braces or 
by using the ``set()`` function on a list. Either way, duplicates are removed.

    >>> # Example of defining a set.
    >>> x = {22, 45, 8, 8, 64}
    {8, 22, 45, 64}
    >>> # Sets can also be defined using the set function on a list.
    >>> y = set(['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'])
    {'apple', 'banana', 'kiwi', 'orange', 'pear'}


NumPy Array
~~~~~~~~~~~
A numpy array is another sequence data type that is very similar to a ``list``. Numpy arrays are faster 
than lists and have some extra functionality. Consequently, for mathematical and statistical analysis, a 
numpy array is preferred. To define a numpy array you must import the ``numpy`` 
package (See `Python Essentials: Import Modules <python_essentials.html#import-modules>`_).

    >>> import numpy as np
    ...
    >>> # Example numpy array.
    >>> x = np.array([12, 55, 6, 33])
    >>> print(x)
    array([12, 55,  6, 33])

Numpy arrays can also be created using the functions ``np.arange()`` and ``np.linspace()``.

    >>> # Example numpy array created using the arange() function.
    >>> # The arguments are start, stop-but-not-including, and the increment size.
    >>> # This example creates a numpy array from 0 to 2 by 0.3 increments.
    >>> y = np.arange(0, 2, 0.3)
    >>> print(y)
    array([0.0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
    ...
    >>> # Example numpy array created using the linspace() function.
    >>> # The arguments are start, stop-but-not-including, and the number of desired elements.
    >>> # This example creates a numpy array from 0 to 2 with exactly 9 elements.
    >>> z = np.linspace(0, 2, 9)
    >>> print(z)
    array([0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0])

If you know the spacing you want between items, then use ``np.arange()``. On the other hand, if you 
know how many items you want, then use ``np.linspace()``.


Often we want to loop over ``np.arange()`` (See `For Loop <if_statement_for_loop.html#for-loop>`_).


Dictionary
----------
A dictionary is a powerful Python lookup data type not covered in this course.


NumPy Matrix
------------
A matrix is a rectangular array (i.e. with rows and columns). It is defined by adding an extra set of square brackets ``[ ]`` 
to a numpy array (See `Matrix Analysis <matrix_analysis.html>`_ for more information).


Pandas DataFrame
----------------
A pandas DataFrame stores tabular data (i.e. with rows and columns) and is created by reading an Excel spreadsheet or csv file 
(See `Data Analysis <data_analysis.html>`_ for more information).


Class and Object
----------------
Writing a "class" for "object oriented programming" is an advanced topic that we will not cover in this course. All
you need to know is the basic concept that a ``class`` is a kind of thing and an ``object`` is a specific
instance of that thing. A ``class`` (and its objects) can have attributes and functionality (which in computer-speak
we call *methods*). For an analogy, a *dog* is a class and my dog *Simon* is an object of that class. All dogs,
including my dog, have certain *attributes* and can do certain things (*methods*).

We use objects often. For example, a numpy array is a class. And if I create ``x = np.array([12, 55, 6, 33])``
then ``x`` is a numpy array object.

Now I can *reference* the attributes or *call* the methods associated with the numpy array object.

    >>> # An attribute is referenced by placing a dot "." between 
    >>> # the object and the desired attribute. 
    >>> #
    >>> # object.attribute
    >>> #
    >>> # For example, the size attribute for a numpy array a can be referenced like this:
    >>> x.size
    4
    ...
    >>> # A method is called by placing a dot "." between 
    >>> # the object and the method with parenthesis. 
    >>> #
    >>> # object.method()
    >>> #
    >>> # For example, the sort method for a numpy array a can be called and used like this:
    >>> x.sort()
    >>> print(x)
    array([ 6, 12, 33, 55])
    ...
    >>> # Some methods can alternatively be called like a function from the imported module.
    >>> #  
    >>> # module.method(object)
    >>> #
    >>> # For example, the sort method can also be called and used like a function:
    >>> np.sort(x)
    array([ 6, 12, 33, 55])

A numpy array (actually called a n dimensional array) has many attributes and methods. You can see the list 
by scrolling down the page here: `numpy.ndarray <https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.ndarray.html#numpy.ndarray>`_

A pandas dataframe is a class with various attributes and methods. You can see the list 
by scrolling down the page here: `pandas.DataFrame <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html>`_


Spyder shows the attributes and methods when you type a dot after an object. If you type ``x.`` and pause this window 
will pop up. The orange *f* indicates a method (also called a function) and pink *a* indicates an attribute.

Pandas dataframe is another example of a ``class`` and in the example above ``my_data`` is an object. 
In fact all data types (``int``, ``float``, etc.) are examples of a ``class`` and ``object``. 
And there are attributes and methods associated with 
each ``class``. For example, ``split`` is one of the methods associated with a ``string``. ``append`` is one of 
the methods associated with a ``list``.


