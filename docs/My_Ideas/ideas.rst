








For a function with two parameters, then ``np.meshgrid`` can be used to create arguments for every combination of the parameters
(for example, to plot a 3d surface).


    >>> import matplotlib.pyplot as plt
    >>> from mpl_toolkits.mplot3d import Axes3D
    ...
    ...
    >>> def f(x1, x2):
    >>>     return np.sin(x1) * np.cos(x2)
    ...
    ...
    >>> x1 = np.arange(-5, 5, 0.25)
    >>> x2 = np.arange(-5, 5, 0.25)
    >>> x1, x2 = np.meshgrid(x1, x2)
    ...
    >>> ax = plt.gca(projection='3d')
    >>> ax.plot_surface(x1, x2, f(x1, x2))
    >>> ax.set_xlabel('x1')
    >>> ax.set_ylabel('x2')



It is impossible to remember all the formatting commands. So the best approach is to become proficient with reading Python
documentation. Luckily, Python programmers are fastidious about following documentation uniformity (i.e. Pythonic Style),
so whether you are reading about a function from matplotlib or any other package, the documentation looks very similar.
Here is the documentation for `plot <https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html>`_.