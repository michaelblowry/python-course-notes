.. _matrix_analysis:

Matrix Analysis
===============
It is often useful to store data in matrices for special mathematical calculations. On this page,
we review matrix notation and calculations (For more information see `Matrix mathematics <https://en.wikipedia
.org/wiki/Matrix_(mathematics)>`_). This page concludes by showing the most common matrix analysis in engineering: *solving a system of equations*.


Matrix Notation in Python
-------------------------
A matrix is organized with rows and columns. Often mathematicians use capital letters to represent a matrix and write the
values or *elements* surrounded by box brackets as shown below. The shape (or dimension) of a matrix is the number of rows and
columns. For example, *A* is a 2x2 matrix (because it has 2 rows by 2 columns). *B* is a 3x5 matrix. *C* is a 1x3 matrix (also called a row matrix). *D* is a 4x1 matrix (also called a column matrix).

.. math::

    \begin{align*}
    & A = \left[\begin{matrix}3&5\\6&4\end{matrix}\right]
    & B = \left[\begin{matrix}5.2&12.1&8.5&12.3&45.1\\8.6&1.3&23.0&50.6&1.0\\0.0&0.0&12.5&15.3&2.1\end{matrix}\right] \\
    & C = \left[\begin{matrix}12&34&15\end{matrix}\right]
    & D = \left[\begin{matrix}4.6\\16.4\\45.0\\3.5\end{matrix}\right] \\
    \end{align*}

In Python, a matrix is defined by adding an extra set of square brackets ``[ ]`` to a numpy array (Numpy also has a specific data structure called "matrix", 
but the documentation recommends avoiding it). Here are matrices defined in Python:

.. nbplot::

    >>> import numpy as np
    ...
    ...
    >>> # Example matrices.
    >>> # A is a 2 by 2 matrix.
    >>> # B is a 3 by 5 matrix.
    >>> # C is a 1 by 3 matrix (also called a row matrix).
    >>> # D is a 4 by 1 matrix (also called a column matrix).
    >>> A = np.array([[3, 5],
    ...               [6, 4]])
    >>> B = np.array([[5.2, 12.1, 8.5, 12.3, 45.1],
    ...               [8.6, 1.3, 23.0, 50.6, 1.0],
    ...               [0.0, 0.0, 12.5, 15.3, 2.1]])
    >>> C = np.array([[12.5, 34.6, 15.8]])
    >>> D = np.array([[4.6],
    ...               [16.4],
    ...               [45.0],
    ...               [3.5]])


The indented alignment for each row is to make it easier to see and most IDE's inlcuding Spyder will do this automatically.

In Python, it is common for variables, including matrices, to be named with full-words and lower-case letters. For example,
you might see variables such as `data`, `values`, or `measurements`.

    >>> data = np.array([[2, 12],
    ...                  [6, 1],
    ...                  [4, 31]])


Indexing and Slicing
~~~~~~~~~~~~~~~~~~~~

The elements of a matrix can be referenced according to the row *i* and column *j*. In Python the number of rows are
counted (indexed) starting at zero. In other words, *i* = 0, 1, 2, ..., *m*. Likewise, the columns begin at at zero, *j* = 0, 1, 2, ..., *n*. To return
the whole row or column use a colon ``:``

    >>> # Example indexing and slicing of matrices (Note indexing begins at 0 in Python).
    >>> B.shape # Returns the dimensions.
    (3, 5)
    >>> B.size # Returns the number of elements.
    15
    >>> B[1, 3] # Returns row 1, column 3.
    50.6
    >>> B[2, :] # Returns row 2, all columns.
    array([ 0. ,  0. , 12.5, 15.3,  2.1])
    >>> B[:, 2] # Returns all rows of column 2.
    array([ 8.5, 23. , 12.5])

A submatrix can be sliced from a larger matrix using the form ``row_start:row_stop, col_start:col_stop`` This can be confusing; first
because the colons here have different meaning than the indexing above and second because the stop needs to
be one index past the row or column that you want (and third because you need to get used to Python indexing starting at zero).

    >>> # Slicing a submatrix (Note indexing begins at 0 and goes one step past the desired location).
    >>> submatrix_B = B[1:3, 2:4]
    >>> print(submatrix_B)
    [[23.  50.6]
     [12.5 15.3]]


Matrix Operations and Calculations
----------------------------------
The following are the most common operations and calculations. They will be demonstrated on matrices x, y, and z.

.. math::

    \begin{align*}
    & x = \left[\begin{matrix}2&3&4\\1&1&3\\3&1&5\end{matrix}\right]
    & y = \left[\begin{matrix}1&6&2\\1&6&2\\3&2&5\end{matrix}\right]
    & z = \left[\begin{matrix}3&2\\3&1\\2&4\end{matrix}\right]
    \end{align*}

.. nbplot::

    >>> # Matrices used in the examples below.
    >>> x = np.array([[2, 3, 4],
    ...               [1, 1, 3],
    ...               [3, 1, 5]])
    >>> y = np.array([[1, 6, 2],
    ...               [1, 6, 2],
    ...               [3, 2, 5]])
    >>> z = np.array([[3, 2],
    ...               [3, 1],
    ...               [2, 4]])


.. tip::
    Sometimes a quick way to define matrices is with ``.reshape(rows, columns)`` on a numpy array. For example, the matrices 
    above could be defined like this:
    
    .. nbplot::

        >>> # Matrices defined using .reshape(rows, columns)
        >>> x = np.array([2, 3, 4, 1, 1, 3, 3, 1, 5]).reshape(3, 3)
        >>> y = np.array([1, 6, 2, 1, 6, 2, 3, 2, 5]).reshape(3, 3)
        >>> z = np.array([3, 2, 3, 1, 2, 4]).reshape(3, 2)
     

Transpose
~~~~~~~~~
Rotates the matrix, so that rows become columns, and vice versa. 
There are two ways to transpose a matrix. It can be done using a function call ``np.transpose(Matrix)`` or a method call 
on the matrix object ``Matrix.transpose()``. 

    >>> # Example calling a function for transpose.
    >>> np.transpose(x)
    array([[2, 1, 3],
           [3, 1, 1],
           [4, 3, 5]])
    >>> np.transpose(z)
    array([[3, 3, 2],
           [2, 1, 4]])
    ...
    >>> # Example calling a method on the matrix object to transpose.
    >>> x.transpose()
    array([[2, 1, 3],
           [3, 1, 1],
           [4, 3, 5]])
    >>> z.transpose()
    array([[3, 3, 2],
           [2, 1, 4]])


Addition and Subtraction
~~~~~~~~~~~~~~~~~~~~~~~~
Addition and subtraction occurs on matching *i*, *j* elements, consequently addition and subtraction can only be done for matrices that are the same shape.

    >>> # x and y can not be added or subtracted with z because they are not the same shape.
    >>> # But, x and y can be added or subtracted to each other
    >>> x + y
    array([[ 3,  9,  6],
           [ 2,  7,  5],
           [ 6,  3, 10]])
    >>> x - y
    array([[ 1, -3,  2],
           [ 0, -5,  1],
           [ 0, -1,  0]])

Multiplication
~~~~~~~~~~~~~~
There are four types of multiplication.

Scalar Multiplication
+++++++++++++++++++++
This multiplies a number (called a scalar) with each element.

    >>> 10 * x
    [[20 30 40]
     [10 10 30]
     [30 10 50]]

Element Multiplication
++++++++++++++++++++++
This multiples matching *i*, *j* elements, consequently element multiplication can only be done for matrices that are the same shape.

    >>> # x and y can not be element multiplied with z because they are not the same shape.
    >>> # But, x and y can be element multiplied to each other.
    >>> x * y
    array([[ 2, 18,  8],
           [ 1,  6,  6],
           [ 9,  2, 25]])

Matrix Multiplication (Dot Product or Inner Product)
++++++++++++++++++++++++++++++++++++++++++++++++++++
The "inside" dimensions must be equal, i.e. the number of columns of the first matrix must equal the number of rows of the second matrix.
For example, you could dot multiply a 2x3 with a 3x10. Mathematicians write matrix multiplication with a symbol that looks like a dot.

.. math::

    x \bullet y

.. nbplot::

    >>> np.dot(x, y)
    [[17 38 30]
     [11 18 19]
     [19 34 33]]
    >>> np.dot(x, z)
    array([[23, 23],
           [12, 15],
           [22, 27]])

Cross Product (Outer Product)
+++++++++++++++++++++++++++++
Both matrices (vectors) must be 1x3 or 3x1. Mathematicians write the cross product with a symbol that looks like a cross.

.. math::

    x \times y


.. nbplot::

    >>> # The first row of x and y, since dimensions must be 1x3 or 3x1.
    >>> np.cross(x[0,:], y[0,:])
    array([-18,   0,   9])
    ...
    >>> # If all rows are given, then the cross product is performed for each row.
    >>> np.cross(x, y)
    array([[-18,   0,   9],
           [-16,   1,   5],
           [ -5,   0,   3]])


Determinant
~~~~~~~~~~~
The determinant can only be calculated for a square matrix. A zero determinant means the matrix is "singular" and cannot be inverted.
Mathematicians write the determinant with two straight bars.

.. math::

    |x|

.. nbplot::

    >>> np.linalg.det(x)
    8.000000000000002
    >>> np.linalg.det(y)
    0.0


Inverse
~~~~~~~
The inverse can only can be calculated for a square matrix that is "nonsingular", i.e. the determinant :math:`|x| \neq 0`. 
Mathematicians write inverse as an exponent of -1.

.. math::

    x^{-1}

.. nbplot::

    >>> np.linalg.inv(x)
    array([[ 0.25 , -1.375,  0.625],
           [ 0.5  , -0.25 , -0.25 ],
           [-0.25 ,  0.875, -0.125]])


The determinant and inverse functions are in the numpy linear algebra module ``linalg``.

Solving System of Linear Equations
----------------------------------
A common application of matrix analysis is solving a `system of linear equations <https://en.wikipedia.org/wiki/System_of_linear_equations>`_ (also called simultaneous equations).
In engineering this situation often arises when trying to *balance* different equations so that each equation is true.
Consider for example the following equations:

.. math::

    2q  - r + 5s + t = -3\\
    3q  + 2r + 2s - 6t = -32\\
    q  + 3r + 3s - t = -47\\
    5q  - 2r + 3s + 3t = 49\\

Notice that there are four equations and four unknowns. The question is what values of *q*, *r*, *s*, and *t* will make all the equations correct (balanced)?
This problem could be solved using a series of substitutions. A quicker approach is to use matrix analysis. The first step is to
re-write the equations as matrices. Often mathematicians use the variable names *A*, *x*, and *b*.

.. math::

    \begin{align*}
    & A = \left[\begin{matrix}2&-1&5&1\\3&2&2&-6\\1&3&3&-1\\5&-2&-3&3\end{matrix}\right]
    & x = \left[\begin{matrix}q\\r\\s\\t\end{matrix}\right]
    & b = \left[\begin{matrix}-3\\-32\\-47\\49\end{matrix}\right]
    \end{align*}

Thus, the system equation is

.. math::

    A \bullet x = b

Where *x* is the column matrix of unknowns. We can solve for *x* algebraically as follows

.. math::

    x = A^{-1} \bullet b

In Python this calculation is done as follows

.. nbplot::

    >>> A = np.array([2, -1, 5, 1, 3, 2, 2, -6, 1, 3, 3, -1, 5, -2, -3, 3]).reshape(4, 4)
    >>> b = np.array([-3, -32, -47, 49]).reshape(4, 1)
    ...
    >>> x = np.dot(np.linalg.inv(A), b)
    >>> print(x)
    [[  2.]
     [-12.]
     [ -4.]
     [  1.]]

Since this is such a common calculation, there is a function in the linear algebra module that does the dot product and inverse all in one, it is ``np.linalg.solve()``

    >>> x = np.linalg.solve(A, b)
    >>> print(x)
    [[  2.]
     [-12.]
     [ -4.]
     [  1.]]
    

The resulting elements of ``x`` are the values for the unknowns, in this case, *q*, *r*, *s*, and *t*. In deed, they are the only values
that will make all the equations valid simultaneously (i.e. the only ones that can balance the equations). 
For clarity we can create a list of the variables in the same order x and then loop over the indexes of x to print each value like this:

    >>> variables = ['q', 'r', 's', 't']
    >>> for i in range(0, len(x)):
    ...     value = x[i]
    ...     print(variables[i], '=', value)
    q = [2.]
    r = [-12.]
    s = [-4.]
    t = [1.]

Often the most difficult step in solving a system of equations is to figure out how to re-write the equations as matrices.

.. comments
    TODO: add the truss problem
    TODO: Add the following:
    Note solving a system of equations requires the ability to calculate the inverse of A.
    Thus, this approach is not possible if A is non-singular, either because it is not square or the determinate is equal to zero.
    well-determined, i.e., full rank, linear matrix equation
    If A is not square, then either there are more unknowns than equations or more equations than unknowns.
    If the determinate is equal to zero, then there is not one solution to the problem (i.e. more than one set of variables can balance the equations).
    Consider this example,
    The way this is written, it might remind you of solving a multiple regression problem. In deed, when
    from numpy: Computes the “exact” solution, x, of the well-determined, i.e., full rank, linear matrix equation ax = b.
    So show OLS method





