..  -*- coding: utf-8 -*-

Python Essentials
=================

Someone fluent in a different computer language or someone learning for the first time needs to answer these
essential questions about Python:

- How do I write comments that won't be executed?
- How do I structure and store data?
- How do I import modules (packages)?
- What is the syntax for math operations?
- How do I control flow with "if statements"?
- How do I repeat procedures with "for loops?


Comments
--------
"Comments", in any computer language, are used to document the program so that you or someone else can understand the
code when reading it later. Comments **do** nothing, i.e. no data is read into the computer and no calculations are
performed; Everything in a comment is ignored when you hit *Run*.

In Python there are two ways to designate something as a comment. First is to use the hash character, ``#``, which
can be placed on its own line or immediately after other code. Everything on the line following ``#`` is a comment.

.. nbplot::

    >>> # This is a comment. It is used to document this code.
    >>> b = 4 # b is the base in centimeters
    >>> h = 8.6 # h is the height in centimeters
    >>> a = b * h # a is the area
    >>> print(a)
    34.4

.. tip::
    To copy code snippets from this website, click ``>>>`` in the upper right corner to Hide the
    prompts and output. Then, highlight the code and hit Ctrl c to copy. Then, in the Console or Editor of Sypder
    place your cursor and hit Ctrl v to paste.

The other way to designate a comment is with three quotes ``"""`` before and after the text. The
quotes can be double quotes ``"""`` or single quotes ``'''``. Every line between the starting triple quotation and
the ending triple quotation is a comment.


.. nbplot::

    >>> """This is a long comment using triple quotation. This comment method is used for long complete sentences
    ... or for commenting out multiple lines of information. Notice that must IDEs, such as Spyder, give a different
    ... color to triple quote comments vs hash character comments."""
    >>> b = 22.2 # b is the base in centimeters
    >>> h = 16 # h is the height in centimeters
    >>> a = b * h # a is the area
    >>> print(a)
    355.2
    >>> '''The triple quotation can be with double quotes or single quotes.'''
    >>> b = 12 # b is the base in centimeters
    >>> h = 1.8 # h is the height in centimeters
    >>> a = b * h # a is the area
    >>> print(a)
    21.6



Data Types
----------

The most basic data types are Integer, Floating Point, and String.

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


Math Operations
---------------


If Statement
------------




For Loop
--------








.. code-links::