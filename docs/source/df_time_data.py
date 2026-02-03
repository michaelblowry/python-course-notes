# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:00:01 2020

@author: mlowry
"""

Using datetime Data
-------------------
A column can be converted to a ``datetime`` datatype by using the function ``pd.to_datetime(df["ColumnName"])``. 
This may not be necessary if the data was read from Excel, but likely is needed when reading csv files. 
The advantage of specifing a column as a ``datetime`` is that it allows extracting the year, month, etc. 

    >>> # Example using a "datetime" column to create new columns.
    >>> df['Time'] = pd.to_datetime(df['Time'])
    ...
    ...
    >>> def f(row):
    ...     return row['Time'].year
    ...
    ...
    >>> df['Year'] = df.apply(f, axis=1)
    ...
    ...
    >>> def f(row):
    ...     return row['Time'].minute
    ...
    ...
    >>> df['Minute'] = df.apply(f, axis=1)
    ...
    >>> print(df.head())
                     Time     Gas1    Gas2    Gas3     Gas1_C  Year  Minute
    0 2019-01-18 17:00:00  103.764  42.666  59.036  39.868889  2019       0
    1 2019-01-18 17:02:00  118.377  42.595  67.425  47.987222  2019       2
    2 2019-01-18 17:04:00   99.893  53.041  67.499  37.718333  2019       4
    3 2019-01-18 17:06:00  118.005  57.925  74.474  47.780556  2019       6
    4 2019-01-18 17:08:00   97.713  59.223  73.892  36.507222  2019       8


