# Visualising Data with PySide

## Python files
* *Project_main* is the main python file. 
It generates the UI and links to the other python files.
* *csvviewui* creates qtreewidgit and qtreeview using the csv data 
(see set path)
* *treeanalysis* creates a decision tree ML classifier with the 
data set. It also generates a scatter plot to determine the 
correlation between attributes (TOEFL, GRE, class label). 
A visualisation of the decision tree is also provided.

## Set Path

The data set is included in the folder (pyside_project). 
It is named 'Admission_Predict.csv' in the folder 
'graduate-admissions' folder. 

Set the file path in 'DataVisualisationApp' class in the 
'project_main' python file.

## Run

To run the program, go the the main file (Project_main),
set path, and run. 


## UI features
You can select between the type of tree that you want to view 
(treewidget or treeview)

You can also select between the type of visualisation you want 
to view (decision tree and scatter plot)

## Preference
Personally, I prefer the QTreeWidgit for viewing this data set 
because it is much easier to create table rows with list objects.

I believe there are several situations where the StandardModel 
may be a much better choice. For instance, when creating a tree 
with only strings, the StandModel seems to be much simpler.
