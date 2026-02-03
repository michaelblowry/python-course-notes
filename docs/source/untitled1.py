# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:18:02 2020

@author: mlowry
"""


    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> import pandas as pd
    ...
    >>> pd.set_option('display.max_columns', None)
    ...
    >>> folder_path = r'C:\Users\mlowry\OneDrive - University of Idaho\Courses\CE215\Data_Files'
    >>> ouput_folder_path = r'C:\Users\mlowry\OneDrive - University of Idaho\Courses\CE215\Output'
    ...
    ...
    >>> my_data_file = folder_path + r'\Temperature_Data.xlsx'
    ...
    >>> # Example plotting columns of a DataFrame.
    >>> df = pd.read_excel(my_data_file, sheet_name="Sheet1")
    ...
    >>> plt.figure(1)
    >>> plt.plot(df['Time_Minutes'], df['Gas1'])
    >>> plt.xlabel("Time")
    >>> plt.ylabel("Gas 1 Temperature (F)")
    >>> plt.xticks(rotation=90)
    >>> plt.show()