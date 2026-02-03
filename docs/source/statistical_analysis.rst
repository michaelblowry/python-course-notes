..  -*- coding: utf-8 -*-

.. _statistical_analysis:

Statistical Analysis
====================
Statistical analysis is done for three reasons:

1. **Descriptive Statistics** - *What does the data tell us?*
2. **Building and Using Models** - *Can the data be used to estimate values or predict the future?*
3. **Hypothesis Testing** - *Are the descriptive statistics and models just coincidence for this sample?*

This page describes how to perform statistical analysis using Python. Since this is a complicated topic, I include more text 
compared to other pages. My intent is to provide basic contextual information, but I do not elaborate on the mathematics which 
can be found in an intermediate statistics textbook.



Descriptive Statistics
----------------------
Descriptive Statistics are calculations used to describe or summarize a collection of data. This is, by far, the most common 
type of statistical analysis that a practicing engineer will ever do (Rarely do engineers build models, besides maybe for their 
MS thesis, and even less frequently do engineers conduct hypothesis tests). Descriptive Statistics are all around us in our every day 
lives--in the news, sporting events, and discussions we have with friends and family. Consequently, engineering students (and everyone) 
should take the time to fully understand Descriptive Statistics. 

A "statistic" is a number. All statistics shown on this page are calculated using ``pandas`` DataFrame *methods*, which means they need to be called by using 
dot and parenthesis ``.()`` (See `Data Types:Class and Object <data_types.html#class-and-object>`_). A few of the methods, like mode, return 
more than one thing. It might be helpful to review the documentation for each method (See `pandas.DataFrame <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html>`_). 

Descriptive Statistics can be grouped into five categories, each seeking to answer a certain question based on the data.

- Amount and Frequency Statistics - *How much and how often?*
- Central Tendency Statistics - *What is typical?*
- Dispersion Statistics - *What is the variation?*
- Time Statistics - *When?*
- Spatial Statistics - *Where?*

The examples below will use data about wage rates for all public employees in the City of Seattle 
(This data is updated every year). 
See `Reading Input and Writing Output: csv files <input_output.html#csv-files>`_     

For an introduction to ``matplotlib`` and ``pandas`` see `Creating Plots <creating_plots.html>`_ and      
`Data Analysis <data-analysis.html>`_, respectively.

.. nbplot::

    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> import pandas as pd
    ...
    >>> input_folder_path = r'C:\Users\mlowry\OneDrive - University of Idaho\Courses\CE215\Data_Files'
    >>> output_folder_path = r'C:\Users\mlowry\OneDrive - University of Idaho\Courses\CE215\Part2_Python\Output' 
    ...
    >>> # The csv file in a folder on your computer.
    >>> csv_file = input_folder_path + r'\City_of_Seattle_Wage_Data.csv'  # Note the backslash to separate the path and file name. 
    ...
    >>> # Example reading a csv file to create a DataFrame called "df".
    >>> df = pd.read_csv(csv_file)
    ...
    >>> # Peek at the data.
    >>> print(df.head())
                     Department     ...      Hourly Rate 
    0  Finance & Admin Services     ...             54.78
    1  Finance & Admin Services     ...             25.54
    2  Finance & Admin Services     ...             28.55
    3  Finance & Admin Services     ...             28.55
    4  Finance & Admin Services     ...             27.49
    ...
    >>> print(df.columns)
    Index(['Department', 'Last Name', 'First Name', 'Job Title', 'Hourly Rate '], dtype='object')
    ...
    >>> print(df.shape)
    (12113, 5)


Amount and Frequency Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
These statistics answer the question: *"How much or how often?"* 
These statistics include **sum**, **count**, and **percent**. There are others not included on this webpage.

    >>> # Example calculating sum. Note the parenthesis after sum. 
    >>> total = df['Hourly Rate '].sum()  # (Oddly, there is a blank space after Hourly Rate.) 
    >>> # What is approximate annual budget that Seattle pays for wages?
    >>> # The 2019 results shown here.
    >>> annual_wages = total * 52 * 40
    >>> print("$", round(annual_wages, 2))
    $ 1037147587.2
    ...
    >>> # Example calculating a count.
    >>> department_count =  df['Department'].value_counts()
    >>> print(department_count)
    Police Department                 1950
    Seattle City Light                1755
    Parks & Recreation                1509
    Seattle Public Utilities          1367
    Fire Department                   1100
    Seattle Dept of Transportation     964
    Information Technology             692
    Seattle Center                     649
    Finance & Admin Services           570
    Human Services Department          380
    Construction & Inspections         374
    Legislative Department             115
    Seattle Dept of Human Resource     107
    Education & Early Learning          75
    Neighborhoods                       57
    Planning & Comm Development         47
    Office of Economic Development      46
    Arts & Culture                      45
    Office of Housing                   43
    City Budget Office                  42
    Mayor's Office                      36
    Employees' Retirement System        34
    Sustainability & Environment        29
    Office for Civil Rights             28
    Office of Labor Standards           22
    Ethics & Elections Commission       12
    Intergovernment Relations           11
    City Auditor                        11
    Community Police Commission          9
    Civil Service Commissions            9
    Immigrant & Refugee Affairs          9
    Office of Inspector General          7
    Hearing Examiner                     5
    Police Relief & Pension Fund         4
    Name: Department, dtype: int64
    ...
    >>> # Example counting a specific value.
    >>> fire_department_count =  df['Department'].value_counts()['Fire Department']
    >>> print(fire_department_count)
    1100
    ...
    >>> # Example calculating a percent.
    >>> # What percent of jobs are in the fire department?
    >>> fd_percent = fire_department_count / department_count.sum() * 100
    >>> print(round(fd_percent, 0), "%")
    9.0 %


.. comments
    TODO: add crosstab. Also add it to the list of bold items above.
    result = pd.crosstab(df['Department'], df['Job Title'])
    print(result)


Central Tendency Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~
These statistics answer the question: *"What is the variation for a value?"*
These statistics include **mean**, **median**, and **mode**. There are others not included on this webpage.
Central tendency is a weird way to say “what is the general center of the data”. The term orginated in the 1920s.


    >>> # Examples of central tendency statistics.
    >>> # Note print is not included in these examples, 
    >>> # so either paste them into the console or hit F9 for each line.
    >>> df['Hourly Rate '].mean() # Oddly, there is a blank space after Hourly Rate.
    41.971904565343024
    >>> df['Hourly Rate '].median()
    41.65
    >>> df['Hourly Rate '].mode()
    0    16.11
    dtype: float64

.. tip::
    All descriptive statistics shown on this page are performed on a column of a DataFrame. 
    For demonstration these are shown by indexing the column, such as ``df['Hourly Rate '].mean()``. 
    A cleaner approach is to create a new DataFrame and then perform the statistic. For example, like this:
    
    .. code::
        
        >>> # Example of first creating a one column DataFrame (actually called a Series).
        >>> wage = df['Hourly Rate ']
        >>> wage.mean()
        >>> wage.median()
        >>> wage.mode()


Dispersion Statistics
~~~~~~~~~~~~~~~~~~~~~
These statistics answer the question: *"What is the typical, middle, or central value?"*
These statistics include **minimum**, **maximum**, **variance**, **standard deviaion**, **skew**, and **quantile** (also called **percentile**).  There are others not included on this webpage.
Dispersion is also called variation or spread.

    >>> # Examples of dispersion statistics.
    >>> # Note print() is not included in these examples, 
    >>> # so either paste them into the console or hit F9 for each line.
    >>> # (Oddly, there is a blank space after Hourly Rate.)
    >>> df['Hourly Rate '].min() 
    5.53
    >>> df['Hourly Rate '].max()
    162.84
    >>> df['Hourly Rate '].var()
    225.24101469300507
    >>> df['Hourly Rate '].std()
    15.008031672841215
    >>> df['Hourly Rate '].skew()
    0.49389507432581775
    >>> df['Hourly Rate '].quantile(q=0.1)  # The lower 1%.
    23.32
    >>> df['Hourly Rate '].quantile(q=0.99) # The lower 99%, meaning 1% have a higher wage.
    81.6487999999998

Standard deviation is the square root of variance. Often standard deviation is more useful to calculate than variance because one can think of the 
68-95-99 rule which says that roughly 68% of the data is within 1 standard deviation of the mean, 
95% of the data is within 2 standard deviation of the mean, 
and 99% of the data is within 3 standard deviation of the mean.

Histogram
~~~~~~~~~
A histogram is chart depicting the ditribution of numerical data. Hitograms are super useful because they can tell 
*amount*, *central tendency*, and *dispersion* all in one chart! 

Pandas has a method for creating a histogram ``df.hist()``.

.. nbplot::

    >>> # Example creating a historgram.
    >>> input_folder_path = r'C:\Users\mlowry\OneDrive - University of Idaho\Courses\CE215\Data_Files'
    >>> output_folder_path = r'C:\Users\mlowry\OneDrive - University of Idaho\Courses\CE215\Part2_Python\Output' 
    ...
    >>> # The csv file in a folder on your computer.
    >>> csv_file = input_folder_path + r'\City_of_Seattle_Wage_Data.csv'  # Note the backslash to separate the path and file name.
    >>> df = pd.read_csv(csv_file)
    >>> wage = df['Hourly Rate ']
    ...
    >>> plt.figure(1)
    >>> wage.hist(bins=50, color='c')
    >>> plt.xlim(10, 150)
    >>> plt.xlabel("Wage")
    >>> plt.ylabel("Frequency")
    >>> plt.show() 

The documentation `pandas.DataFrame.hist <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.hist.html>`_ 
says that this method is actually calling a function from ``matplotlib``. So alternatively, you could use ``matplotlib`` directly, in which case 
the DataFrame is an argument to the function ``plt.hist(x)``. Either way there is a keyword parameter ``bins`` that lets you 
control the number of bins. The default is 10. There are also various algorithms available for finding the best number of bins, such as 
``bins='auto'``. Also, note that some histograms are so skewed that plotting every bin produces a historgram that looks empty. 
This is not the case for the example data above, but even still I include ``.xlim(10, 150)`` to demonstrate how to limit the range of bins to be plotted.
    

Time Statistics
~~~~~~~~~~~~~~~
These statistics answer the question: *"When has something occured?"*
These statistics are the same as those above, but catergorized with a time variable, such as the day of the week or month. 

Spatial Statistics
~~~~~~~~~~~~~~~~~~
These statistics answer the question: *"Where has something occured?"*
These statistics are the same as those above, but catergorized with a spatial variable, such as state or county boundaries. 

Building and Using Models
-------------------------
Mathematical models are representations of real-world phenomena and are used to estimate values or predict the future. 
Models can be devised based on basic principles and theory, such as the relationship between the volume and temperature of a gas, :math:`PV = nRT`.

*Statistical models* are built based on data. In fact, *Descriptive Statistics* are statistical models. For example, 
suppose I want to estimate (or predict) the walking speed of a person (Something a transportation engineer needs to do 
when deciding how long to show the walk signal at an intersection). I can collect a sample of walking speeds and 
use the average speed as my "model". Or perhaps I would prefer the median speed as my model. Review the section above on 
*Descriptive Statistics* and you will see how every statistic can be construed as a "model". 

The walking speed model might be improved by separating the mean speed for males and females. Further improvement is 
possible by also including age in the model. How about additionally distinguishing between tourists and people walking to work? 
Or including whether they are in a big city or a small town? Now we have a sophisticated model: you tell me a person's 
sex, age, if they are a tourist or not, and if they are in a big city or small town; and I will estimate their walking speed.
There might be yet additional *explanatory variables* that could improve the model further. The point is that models can be 
improved (but not necessarily) with more explanatory variables. 

There are a few reasons why you should find a balance between having too few and too many explanatory variables in a statistical model. 
First, is that some "explanatory" variables might not actually *explain* the 
phenomena very well (For example, adding a person's weight to the walking speed model is probably not going to produce a *significant* improvement. Likewise, adding
hair color probably has no contribution to improving the model). Second, more 
explanatory variables requires greater detail during data collection, which is already typically time consuming and expensive anyway 
(For example, when collecting walking speeds, now you would have to stop people and ask their age, etc.). Third, more explanatory variables 
can make models unnecessarily complicated for practical use (For example, transportation engineers don't need to be thinking of all these additional things 
when deciding the signal timing of an intersection. At most, they want to know the average waking speed and then slightly increase 
or decrease the value based on rough information about whether there are high numbers of children or elderly expected). 
Fourth, too many explanatory variables can cause "overfitting". This is the situation where a model is really good for 
describing the sample data, but not very good when transfered to other datasets. In summary, the "best" model has the fewest number of 
explanatory variables, but with the greatest explanatory power -- this is called *parsimony*.

There are many ways to build statistical models. The most common approach is called regression, of which there many variants. This page 
shows linear regression and negative binomial regression. These are the most common regression methods used by engineers 
(In reality, practicing engineers don't *build* models very often, if ever, during their career, but they might *use* models so it 
is good to know how regression models are built).

Introduction to StatsModels
~~~~~~~~~~~~~~~~~~~~~~~~~~~          
StatsModels is a powerful and popular package for statistical analysis.There are two ways (styles) to do regression using StatsModels. The first 
style uses matrix-like variables *y* and *X*. The second style involves writing a "formula".  
The choice of which style to use depends on personal preference. The first style requires ``import statsmodels.api as sm`` and the second style 
requires ``import statsmodels.formula.api as smf``. Pandas DataFrames can be used with both styles. Likewise, statsmodels works well 
with matplotlib and numpy. For an introduction to matplotlib and pandas see `Creating Plots <creating_plots.html>`_ and      
`Data Analysis <data-analysis.html>`_, respectively. 

    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> import pandas as pd
    >>> import statsmodels.api as sm
    >>> import statsmodels.formula.api as smf

The first statsmodels import is for the *y* and *X* style method. The second statsmodels import is for the formula style method. 

Linear Regression
~~~~~~~~~~~~~~~~~
Consider for example a dataset of house sales. 

.. nbplot::

    >>> # Read in example data.
    >>> folder_path = r'C:\Users\mlowry\OneDrive - University of Idaho\Courses\CE215\Data_Files'
    >>> excel_file = folder_path + r'\House_Sales_Data.xlsx'
    >>> sheet = "House_Data"
    >>> df = pd.read_excel(excel_file, sheet_name=sheet)
    ...
    >>> # Peek at the data.
    >>> print(df.head())
    >>> print(df.columns)
    >>> print(df.shape)
       case  sold_price  bedrooms  bathrooms  square_feet  lot_acres  \
    0     1    402742.0         2        2.0         1895       0.25   
    1     2    506299.0         3        1.0         1693       0.50   
    2     3    451800.0         2        2.5         2188       0.50   
    3     4    764500.0         5        2.5         3285       0.50   
    4     5    713900.0         4        2.5         2624       0.25   
       beach_distance  fireplace  garage  view  hottub  
    0             4.4          1       1     0       0  
    1             0.6          0       1     1       0  
    2             8.4          0       1     0       1  
    3             7.8          1       1     0       0  
    4             0.2          1       1     1       0  
    Index(['case', 'sold_price', 'bedrooms', 'bathrooms', 'square_feet',
           'lot_acres', 'beach_distance', 'fireplace', 'garage', 'view', 'hottub'],
          dtype='object')
    (78, 11)
    
The last four attributes are indicator variables where 0 = 'no' and 1 = 'yes'.

If you hire a real estate agent to sell your home, 
they might use the recent sold price from nearby sales to help determine the best listing price for your home. 
A simple "model" would be to list your home based on the mean or median price of recent sales. A better model will incorporate 
attributes of your home. For example, the size in square feet. The plot below illustrates that as square footage increases so does sold price.  

.. nbplot::

    >>> # Calculate average sold price.
    >>> print(df.sold_price.mean())
    558132.1024992522
    >>> print(df.sold_price.median())
    558250.0
    ... 
    >>> # Plot price vs. square feet.
    >>> plt.figure(2)
    >>> plt.scatter(df.square_feet, df.sold_price)
    >>> plt.xlabel("Square Feet")
    >>> plt.ylabel("Sold Price")
    >>> plt.show()
  
An even better model will incorporate additional attributes of your house (i.e. explantory variables) to *explain* the value of your house.

*y* and *X* Style
+++++++++++++++++
This style involves (1) defining *y* and *X*, (2) adding a constant to *X*, (3) creating the model object, (4) fitting 
the model, and (5) printing the results.

    >>> import statsmodels.api as sm
    ...
    >>> # Example linear regression.
    >>> y = df.sold_price
    >>> X = df[['bedrooms', 'bathrooms', 'square_feet','lot_acres', 'beach_distance', 
    ...         'fireplace', 'garage', 'view', 'hottub']]
    >>> X = sm.add_constant(X)
    >>> model = sm.OLS(y, X)
    >>> results = model.fit()
    >>> print(results.summary())
                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:             sold_price   R-squared:                       0.947
    Model:                            OLS   Adj. R-squared:                  0.940
    Method:                 Least Squares   F-statistic:                     134.0
    Date:                Tue, 23 Apr 2019   Prob (F-statistic):           1.09e-39
    Time:                        09:54:13   Log-Likelihood:                -912.96
    No. Observations:                  78   AIC:                             1846.
    Df Residuals:                      68   BIC:                             1869.
    Df Model:                           9                                         
    Covariance Type:            nonrobust                                         
    ==================================================================================
                         coef    std err          t      P>|t|      [0.025      0.975]
    ----------------------------------------------------------------------------------
    const           6.958e+04   1.97e+04      3.524      0.001    3.02e+04    1.09e+05
    bedrooms         5.43e+04   2945.973     18.433      0.000    4.84e+04    6.02e+04
    bathrooms       2.072e+04   4547.543      4.557      0.000    1.16e+04    2.98e+04
    square_feet       94.3759      5.500     17.159      0.000      83.401     105.351
    lot_acres       3.856e+04   3702.981     10.412      0.000    3.12e+04    4.59e+04
    beach_distance -5809.7007   1502.376     -3.867      0.000   -8807.644   -2811.757
    fireplace       1.328e+04   7432.380      1.787      0.078   -1549.120    2.81e+04
    garage          2.327e+04   8003.158      2.908      0.005    7302.271    3.92e+04
    view            4.106e+04   8455.003      4.856      0.000    2.42e+04    5.79e+04
    hottub          4899.3342   7729.584      0.634      0.528   -1.05e+04    2.03e+04
    ==============================================================================

The adjused R-squared is very good at 0.94. Two explanatory variables have p-values above 0.05, indicating that they might not 
provide any statistical significance to the prediction and could be removed from the model. The documentation for `statsmodels.regression.linear_model.RegressionResults <https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.html>`_
says the "RegressionResults" object has various attributes that can be accessed individually, such as ``results.params``, ``results.rsquared``, and ``results.resid``. 

    >>> # Reduced model.
    >>> y = df.sold_price
    >>> X = df[['bedrooms', 'bathrooms', 'square_feet','lot_acres', 'beach_distance', 
    ...         'garage', 'view']]
    >>> X = sm.add_constant(X)
    >>> model = sm.OLS(y, X)
    >>> results = model.fit()

The model results can be used to predict a sales price. For example, suppose we want to determine the best listing price for a house 
that has these attributes: 3 bedroom, 1 bathroom, 1,700 square feet, ¾ acre, 4 miles to beach, fireplace, garage, no view, no hottub. 
The first step is to construct a Python ``list`` for this specific house. The indices of the list must correspond to the indices of 
the model. Furthermore, the list must begin with a 1 for the constant.


    >>> # This is the data that will be used for a prediction.
    >>> # It is a list in the same order as the X defintion.
    >>> # Must include 1 at the beginning for the constant.
    >>> # Could be a list of lists, for multiple preditions.
    >>> house = [1, 3, 1, 1700, 0.75, 4, 1, 0]
    ... 
    >>> # Prediction is a numpy array for every list provided.
    >>> # In this case only one list is provided so the answer is at index [0].
    >>> prediction = results.predict(house)
    >>> print("Estimated house sale price is", round(prediction[0], 2))
    Estimated house sale price is 452594.03
 

Formula Style
+++++++++++++
This is an alternative style. This example is identical to the one above. This style involves (1) writing a formula, 
(2) creating the model object, (3) fitting 
the model, and (4) printing the results.


.. nbplot::

    >>> import statsmodels.formula.api as smf
    ...
    >>> # Example linear regression.
    >>> formula = 'sold_price ~ bedrooms + bathrooms + square_feet + lot_acres + beach_distance + fireplace + garage + view + hottub'
    >>> model = smf.ols(formula, data=df)  # Note this is the smf import. Also note that ols is lowercase for this style.
    >>> results = model.fit()
    >>> print(results.summary())

As was described in the example above, we might want to reduce the model by removing the explanatory variables with p-values 
above 0.05. We will can then use the model to estimate the expected selling price of a particular house. This time, however, 
the prediction requires creating a pandas DataFrame or dictionary.  

    >>> # Reduced model.
    >>> formula = 'sold_price ~ bedrooms + bathrooms + square_feet + lot_acres + beach_distance + garage + view'
    >>> model = smf.ols(formula, data=df)  
    >>> results = model.fit()
    >>> print(results.summary())
    ...    
    >>> # This is the data that will be used for a prediction.
    >>> # It can be a pandas DataFrame or a dictionary
    >>> # The column names or dictionary keys must correspond to the formula.
    >>> # Order does not matter and additional items will be ignored.
    >>> # The prediction will only use the columns or keys that are specified in the model.
    >>> house = {'bedrooms':3, 'bathrooms':1, 'square_feet':1700, 'lot_acres':0.75, 'beach_distance':4, 'fireplace':1, 'garage':1, 'view':0, 'hottub':0}
    ...
    >>> # Prediction is a numpy array for every set of values provided.
    >>> # In this case only one set of values is provided so the answer is at index [0].   
    >>> prediction = results.predict(house)
    >>> print("Estimated house sale price is", round(prediction[0], 2))



Negative Binomial Regression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Negative binomial regression should be used when the dependent variable is a positive integer--for example, anything that 
involves predicting *counts*, such as predicting the number of crashes on a roadway (it is not logical to predict negative crashes or partial crashes).

Coming soon.



Hypothesis Testing
------------------
Hypothesis tests are calculation to determine if Descriptive Statistics and Statistical Models are just coincidence for the data sample. 
For example, suppose I want to know the difference in average height for male and female college students. 
I can collect a sample of data and compare the mean values. But is my result the *true difference* or is it 
just a coincidence of the sample that I happened to observe? In other words, if I were to collect more data might I get a different result? 
Amazingly, brilliant statiticians have devised a way to calculate the probability of wheter the observed 
descriptive statistic or model is merely a coincidence. However, there is one important caveat: the hypothesis calculation 
is based on the data sample itself, so hypothesis conclusions must be qualified with nuanced words of probablity, such as *maybe*, *likely*, and *probably*. 

More coming soon.
  
t-Test
~~~~~~
Coming soon.


Chi-squared Test
~~~~~~~~~~~~~~~~
Coming soon.


Linear Regression Test
~~~~~~~~~~~~~~~~~~~~~~
Coming soon.


