..  -*- coding: utf-8 -*-

Python Essentials
=================

Someone fluent in a different computer language or someone learning for the first time needs to answer these
essential questions about Python:

- `How do I write comments that won't be executed? <#comments>`_
- `How do I structure and store data? <#data-types>`_
- `How do I import modules (packages)? <#import-modules>`_
- `What is the syntax for basic math? <#basic-math>`_
- `How do I control flow with "if statements"? <#if-statement>`_
- `How do I repeat procedures with "for loops"? <#for-loop>`_


Comments
--------
In any computer language "comments" are used to document the program so that you or someone else can understand the
code when reading it later. Comments *do* nothing, i.e. no data is read into the computer and no calculations are
performed; Everything in a comment is ignored when you hit *Run*.

In Python there are two ways to designate something as a comment. First is to use the hash character, ``#``, which
can be placed on its own line or immediately after other code. Everything on the line following ``#`` is a comment.

.. nbplot::

    >>> # This is a comment. It is used to document this code.
    >>> b = 4 # b is the base in inches
    >>> h = 8.6 # h is the height in inches
    >>> a = b * h # a is the cross section area of the concrete beam.
    >>> print(a)
    34.4

.. tip::
    To copy code snippets from this website, click ``>>>`` in the upper right corner to Hide the
    prompts and output. Then, highlight the code and hit Ctrl c to copy. Then, in the Spyder Console or Editor
    place your cursor and hit Ctrl v to paste. If you are pasting into the Editor and running the code as a script,
    then you may need to add ``print()`` if it is not already in the code snippet.

The other way to designate a comment is with three quotes ``"""`` before and after the text. The
quotes can be double quotes ``"""`` or single quotes ``'''``. Every line between the starting triple quotation and
the ending triple quotation is a comment.


.. nbplot::

    >>> """This is a long comment using triple quotation. This kind of comment is used for long complete
    ... sentences or for commenting out multiple lines of information. Notice that most IDEs, such as
    ... Spyder, give a different color to triple quote comments vs hash character comments."""
    >>> b = 22.2 # b is the base in inches
    >>> h = 16 # h is the height in inches
    >>> a = b * h # a is the cross section area of the concrete beam.
    >>> print(a)
    355.2
    >>> '''The triple quotation can be with double quotes or single quotes.'''
    >>> b = 12 # b is the base in inches
    >>> h = 18 # h is the height in inches
    >>> a = b * h # a is the cross section area of the concrete beam.
    >>> print(a)
    216


.. note::
    Python programmers try to write code that is very easy to read. Consequently, "Pythonic" style uses full words
    as much as possible. For example rather than using ``b`` and ``h`` you could use ``base`` and ``height``. For
    long scripts this is especially nice because you might forget what ``h`` stands for later in the code. Pythonic
    style uses all lowercase with multi-word variables separated with an underscore.

    .. nbplot::

        >>> """Using full words can be (1) easier to read and (2) require less typing."""
        >>> base = 12
        >>> height = 18
        >>> cross_area = base * height
        >>> print(cross_area)



Data Types
----------
All computer languages must have a way to structure and store data. The data types in Python are similar to other
languages. You can determine the data type of something with the built-in function ``type()``.

.. nbplot::

    >>> x = 4
    >>> type(x)
    int

    >>> y = [1, 5, 6, 22]
    >>> type(y)
    list


Integer, Float, and String
~~~~~~~~~~~~~~~~~~~~~~~~~~

The most basic data types are Integer, Floating Point, and String. These names might be new for you, but have been
around for a long time in computer programming. The first two are simply numbers and a String is computer-speak for
text.

.. nbplot::

    >>> diameter = 4 # This is an integer.
    >>> type(diameter)
    int

    >>> depth = 8.6 # This is a floating point (because it has a decimal point).
    >>> velocity = 5.0 # This is also a floating point.
    >>> type(velocity)
    float

    >>> """If a float is included anywhere in a math operation, then the result will be a float."""
    >>> bearing_stress = 4 * (12 + 3.5)
    62.0


For someone new to computer programming it might seem strange to distinguish between an ``int`` and ``float``. There
are many reasons why this distinction is important, one reason is that in computer programming we often repeat
things for a certain number of times. For example you might want to do a calculation for ``n = 5`` times, but it
doesn't make sense to do something for ``n = 6.2`` times. For the latter, Python will throw an error.


A string is text inside single quotes or double quotes. This is not to be confused with a comment which is ignored by
when you *Run* your program. A string is intended to be used or analyzed. For example you might want to print the
following messages.

.. nbplot::

    >>> allowable_stress = 50
    >>> success_message = "The bearing stress is below the limit."
    >>> fail_message = "Warning: The bearing stress exceeds the limit."
    >>> if bearing_stress >= allowable_stress:
    ...     print(fail_message)
    >>> else:
    ...     print(success_message)
    Warning: The bearing stress exceeds the limit.



The use of double quotes or single quotes does not matter. For example, ``material = "concrete"`` and ``material =
"concrete"`` are identical as far as Python is concerned. I tend to use double quotes.

There are lots of things you can do with strings. For example,

.. nbplot::

    >>> message = "The pipe was ."



List
~~~~

Dictionary
~~~~~~~~~~

NumPy Array
~~~~~~~~~~~
As mentioned earlier a Python ``list`` is similar to what other languages call an array. However, there are a few
subtle differences related to speed and functionality. You can import a module called ``numpy`` to
create a "numpy array" (See `Import Modules <#import-modules>`_).

Numpy arrays are faster than lists and have some extra functionality, but for most assignments in this
course a normal Python ``list`` will be adequate. In fact, I only include the numpy array because it is
frequently mentioned in online help and discussion boards related to data analysis.

.. nbplot::

    >>> import numpy as np
    >>> a = np.array([12, 55, 6, 33]) # One way to create a numpy array. This has 4 elements.
    >>> a
    array([12, 55,  6, 33])

    >>> b = np.arange(0, 2, 0.3)  # This creates a numpy array from 0 to 2 by 0.3 increments.
    >>> b
    array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])

    >>> c = np.linspace(0, 2, 9)  # This creates a numpy array from 0 to 2 with exactly 9 elements.
    >>> c
    array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])


Pandas Dataframe
~~~~~~~~~~~~~~~~



Class and Object
~~~~~~~~~~~~~~~~
``class`` and ``object`` are advanced computer programming topics that we will not cover in detail in this course. All
you need to know is the basic concept that a ``class`` is a kind of thing and an ``object`` is a specific
instance of that thing. A ``class`` (and its objects) can have attributes and functionality (which in computer-speak
we call *methods*). For analogy, a *dog* is a class and my dog *Simon* is an object of that class. Dogs,
including my dog, have certain *attributes* and can do certain things (*methods*).

We will use objects often. For example, a numpy array is a class. And if I create ``a = np.array([12, 55, 6, 33])``
then ``a`` is a numpy array object.

Now I can *reference* the attributes and *call* the methods associated with the numpy array object.

.. nbplot::

    >>> """An attribute is referenced by its name using dotted expressions. object.attribute
    ... For example, the size attribute for the numpy array a can be referenced like this:"""
    >>> a.size
    4

    >>> """A method is called by its name using a dotted expression with parenthesis. object.method()
    ... For example, the sort method for the numpy array a can be called like this:"""
    >>> a.sort()
    >>> a
    array([ 6, 12, 33, 55])

    >>> """Sometimes methods can also be called using the imported module. module.method(object)
    ... For example, the sort can also be called like this:"""
    >>> np.sort(a)
    array([ 6, 12, 33, 55])

The numpy array (actually called a multidimensional ndarray) has many attributes and methods. You can see the list
by scrollin down the page here: `numpy.ndarray <https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy
.ndarray.html#numpy.ndarray>`_

Spyder shows the attributes and methods when you type a dot after an object. If you type ``a.`` and pause this window
will pop up. The orange *f* indicates a method (also called a function) and pink *a* indicates an attribute.

In fact all data types are examples of a ``class`` and ``object``. A Python ``list`` is a ``class`` and ``append`` is
one of its methods.

Pandas dataframe is another example of a ``class`` and in the example above ``my_data`` is an object.

Import Modules
--------------

.. nbplot::

    >>> import networkx
    >>>
    >>> city = networkx.Graph() # Creates a networkx graph object.
    >>> street_list = [(1, 3), (3, 4), (4, 5), (5, 2), (3, 6), (4, 7),(5, 8), (6, 7),
    ...                (7, 8), (6, 9), (7, 10), (8, 11), (9, 10), (10, 11), (9, 12), (11, 13)]
    >>> city.add_edges_from(street_list) # Adds each street to the networkx object.
    >>> networkx.draw(city, with_labels=True) # Draws the networkx object.



Basic Math
----------

** not carrot

https://docs.python.org/3.7/library/stdtypes.html#numeric-types-int-float-complex

If Statement
------------




For Loop
--------








.. code-links::