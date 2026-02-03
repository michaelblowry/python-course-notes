# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:01:41 2020

@author: mlowry
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example creating a dataframe called "df".
folder_path = r'C:\Users\mlowry\OneDrive - University of Idaho\Courses\CE215\Data_Files'
my_data_file = folder_path + r'\Temperature_Data.xlsx'
df = pd.read_excel(my_data_file, sheet_name="Sheet1")
# Example printing the first rows (default n=5).
print(df.head())


# Example: Select row 7 and all columns.
df.loc[7]






# Example: Select row 3 for columns Gas1 and Gas2.
df.loc[3, ['Gas1', 'Gas2']]




# Example: Rows 3 and 6. Columns Gas1 and Gas2.
df.loc[[3,6], ['Gas1', 'Gas2']]



# Example reating new columns with simple calculations.
df["Combined"] = df['Gas1'] + df['Gas2']
df["SuperGas"] = df['Gas1'] * 1000
print(df.head(2))




plt.figure(2)
plt.bar(df.index, df["Time_Minutes"])
plt.show()

# Example applying a function to create a new column.
def f(row):
    temp_f = row['Gas1']
    temp_c = (temp_f - 32)*5/9
    return temp_c


df['Gas1_C'] = df.apply(f, axis='columns')
print(df.head(2))



df = pd.read_excel(my_data_file, sheet_name="Gases")
print(df)

pd.set_option('display.max_columns', None)
# Example dataset from a companies project database.
my_data_file = folder_path + r'\Company_Project_Data.xlsx'
df = pd.read_excel(my_data_file, sheet_name='Projects')
df.shape
df.columns
df.head()

# Example 1
d = df.query("ActualCost <= 1000000")
d.shape
(173, 10)

# Example 2
d = df.query("Engineer == 'Woods, Susan'")
d.shape
(48, 10)

# Example 3
d = df.query("EstimatedDays >= 30 and EstimatedDays <= 60")
d.shape
(198, 10)

# Example 4 (Queries on an already queried DataFrames)
d = df.query("CategoryID == 5")
d = d.query("EstimatedDays > 20")
d = d.query("EstimatedCost > 500000") 
d.shape
(77, 10)


d = df.loc[df["ActualCost"] <= 1000000]


d = df.pivot_table(values="ActualDays", index="Engineer", columns="CategoryID", aggfunc="count", fill_value=0)
print(d)


df['dummy'] = 1
d = df.pivot_table(values="ActualDays", index="Engineer", columns="CategoryID", aggfunc="count", fill_value=0)
print(d)

d = df.pivot_table(values="dummy", index="Engineer", columns="CategoryID", aggfunc="count", fill_value=0)

my_data_file = folder_path + r'\Company_Project_Data.xlsx'
df = pd.read_excel(my_data_file, sheet_name='Projects')
df.shape

df["dummy"] = 1
d = df.pivot_table(values="dummy", index="Engineer", columns="CategoryID", aggfunc="count", fill_value=0)
print(d)

#                  dummy
# ManagerName           
# Boyce, Bruce        50
# Colton, Greg        17
# Degas, Josh         36
# Guza, Adina         21
# Jaffe, Jerry        36
# Marlow, Daniel      16
# Murphy, Mary        36
# Pac, Su Li          39
# Rivera, Titus       31
# Steele, Richard     46
# Stone, Jeff         23
# Turnage, Leslie     23
# Weaver, Diane       27
# Wolff, Carolyn      51
# Woods, Susan        48


# Example using .value_counts() to get the count of a column.
d = df["Engineer"].value_counts()
print(d)
# Wolff, Carolyn     51
# Boyce, Bruce       50
# Woods, Susan       48
# Steele, Richard    46
# Pac, Su Li         39
# Degas, Josh        36
# Jaffe, Jerry       36
# Murphy, Mary       36
# Rivera, Titus      31
# Weaver, Diane      27
# Stone, Jeff        23
# Turnage, Leslie    23
# Guza, Adina        21
# Colton, Greg       17
# Marlow, Daniel     16
# Name: ManagerName, dtype: int64



# Example pie chart from a DataFrame column.
# Get the count for each category.
x = df['CategoryID'].value_counts()

plt.figure(2)
plt.pie(x, labels=x.index, autopct='%0.0f%%', shadow=True)
plt.axis("equal")
plt.title("Categories")
plt.show()




# Example horizontal bar chart from a DataFrame column.
# Get the count for each category.
x = df['Engineer'].value_counts()

plt.figure(3)
plt.barh(x.index, x)
plt.xlabel("Number of Projects")
plt.show()