..  -*- coding: utf-8 -*-

.. _gis_analysis:

GIS Analysis
============
This page shows how to create a GIS tool that can be used in ArcGIS Pro. The example can be downloaded here.

Setup and Getting Started
-------------------------
ArcGIS Pro comes with an installation of Python 3.6. The installation includes two packages, one called ``arcpy`` and another called ``arcgis``. However, Spyder will
not be able to see the these packages because the Anaconda installation that is `described on this website <setup_instructions.html#how-do-i-install-python>`_ will set up Spyder to use
the python that comes with Anaconda. Consequently, if you attempt to ``import arcpy`` you will get ``ImportError: No module named arcpy``.

The best solution I have found is to switch the Python interpreter that Spyder is using. To do this follow these steps (this might
require administrator privileges on your computer depending on how ArcGIS was installed):


**Step 1.** Create a clone of the ArcGIS Pro Python environment. 
Every installation of Python and associated packages is called an "environment". Anaconda installs a base environment and ArcGIS Pro installs another environment. 
To avoid screwing up the default ArcGIS Pro environment, you must "clone" it and make changes to the clone. In ArcGIS Pro, go to 
Project/Python/Manage Environments/Clone Default (This will take a long time to complete. If it crashes you might need to find old clones and delete them manually). 
Make a note of the directory (folder) path to the cloned enviroment because you will need it in Step 3.  
Choose (select) the clone env and hit OK. You will need to restart Pro.

.. image:: images/arcgispro-clone.png


**Step 2.** Install python packages into the cloned environment. 
The default ArcGIS Pro python environment (and now the clone) includes a few common packages like numpy and panadas. However, there might be other 
packages that you want to install that are not included by default. 

There is one package that must be installed to be able to use Spyder. It is called ``spyder-kernels``. To install this package 
(and any others that might be desired), open Anaconda Navigator. You should see ``arcgispro-py3-clone`` listed under Environments.
Click on the triangle next to the enviroment and hit Open Terminal. In the terminal write ``conda install spyder-kernels=0.*``. 

Package installation is also described in 
`Additional Topics: Installing and Updating Packages <additional_topics.html#installing-and-updating-packages>`_

**Step 3.** Switch the interpreter that Spyder uses to the cloned environment.
Now you need to switch the interpreter that Spyder uses. Go to Tools/Preferences/Python interpreter and click “Use the following Python interpreter”. 
Browse to the python.exe that was created in Step 1. In my case the path is 
``'C:\\Users\\mlowry\\AppData\\Local\\ESRI\\conda\\envs\\arcgispro-py3-clone\\python.exe'``

Now restart (x out) the Console interpreter kernel.

After the steps above, Spyder is using the python installed with ArcGIS Pro, which does not include all the many packages that are automatically included with Anaconda.
Consequently, you will need to install anything you might need that is not already there. Follow, the procedure described in Step 2 as needed.


**Step 4.** Turn off showing reloaded list.

``arcpy`` will be reloaded everytime you run a script in Spyder. By default the modules of reloaded packages are printed to the Console when you hit *Run*. 
You can turn this off. Go to Tools/Preferences/Python interpreter. Uncheck Show reloaded modules list


Folder Organization
-------------------
There are lots of ways to organize scripts and data. The following is based on suggestions from ESRI and others. 

The outside folder can have any name that desribes this set of tools. For illustration I use the generic name "GIS_Tools". 
*All other folders should have the exact name shown, including the exact capatilization, underscores, and hyphens.*  

.. image:: images/gis-folders-expanded.png

``toolpackage`` will be a Python package just like ``numpy`` or ``panadas``. All the scripts you will write will be located in ``toolpackage``. The script names should be descriptive and in lowercase. This example has scripts ``spatial_census.py`` 
and ``trail_surrounding.py``. ``toolpackage`` also includes files called ``__init__.py`` and ``config.py`` (The folders __pycache__ and .spyproject are made when using Spyder). 
The init file is a strange thing: it is a blank file. Oddly it is needed to tell python to look in this folder to import other scripts. 
The config file does the following (1) specifies any settings that might be desired when running your tools, (2) identifies the path to tool_data,  
(3) tells python to first look in python_packages to import packages, and (4) specifies the scratch folder and gdb to use.

.. image:: images/toolpackage.png

``tool_data`` contains folders needed by the script: ``files`` contains files that the script will read, ``scratch`` is where intermediate files are written, 
``site-packages`` is for python packages that might not be installed (this only works in certain situations, the better approach is to 
install the packages into the clone environment. See `Additional Topics: Installing and Updating Packages <additional_topics.html#installing-and-updating-packages>`_.), and 
``symbology`` contains layer files for applying symbology.

Additionally, create a folder called ExampleData. Then, using ArcGIS Pro create a project in ExampleData called TestProject.      

.. image:: images/arcgispro-TestProject.png

During tool development, output will go into TestProject. The TestProject.gdb will get full of junk feature classes as the tool is run 
over and over again. Consequently, create a separate folder for input.

.. image:: images/exampledata-folder.png


Tool Development Work Flow
--------------------------
This section describes the different stages of development. Each stage can take multiple hours or even days.

Stage 1. Preparation: Create Folders, Set up ArcGIS Pro and Spyder
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
First, create the folder structure and files described above.

Next, Open TestProject in ArcGIS Pro. Right click Folders in Catalog and Add the folders Input and GIS_Tools.

.. image:: images/arcgispro-folder-connections.png

Finally, now you can begin developing your tool in Spyder. Open Spyder and go to Projects/New Projects... Check Existing directory. Browse to the outside folder, i.e. GIS_Tools. Now you can see all relevant files in the Project explorer.

Stage 2. Write a Script as a Sequential Program
+++++++++++++++++++++++++++++++++++++++++++++++
Create a new .py file and begin writing the code as a sequential program. Run it in Spyder and inspect the output. 
Continue to improve the code until it is doing what you want. 

The following is an example of the end of this stage. 
This is after hours of writing, running, and re-writing. 

.. image:: images/gis-sequence.png


Stage 3. Restructure and Document as Function(s) within the Script(s)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Spend time thinking about how to divide the sequence of code into functions. It might make sense to even put some functions in different .py files (modules). 
The modules can be imported using ``from toolpackage import module_name``. Once functions are defined, spend some time writing docstring(s) and comments. 

The next task is kind of strange: At the bottom of the script (below the functions that have been created) write ``if __name__ == '__main__':``. 
Then move the paths for ExampleData and all other paramater assignments to the very bottom. Finally, below this call the function(s) from above. 
Run it in Spyder and inspect the output. Continue to improve the code until it is doing what you want.

The following is an example of the end of this stage. 
This is after hours of writing, running, and re-writing. 

.. image:: images/gis-function.png

Stage 4. Create a Python Toolbox
++++++++++++++++++++++++++++++++
The final stage is to create a Python Toolbox. In ArcGIS Pro, right click on the outside folder (i.e. GIS_Tools) and 
click New/Python Toolbox (Don't worry about naming it at this point).

Go to Spyder and you will see the .pyt in Project explorer. Here (or using File Explorer) rename it.

.. image:: images/gis-toolbox.png


Additional Comments
-------------------
More coming soon.

Messages from ``arcpy.AddMessage()`` will not be printed to the Spyder Console.
If you want to see them, then go to Run/Run configurations per file/Select Execute in an external system terminal.
You will probably also want to check Interact with the PYthon console after exectuion so you can inspect variables and test code still.

