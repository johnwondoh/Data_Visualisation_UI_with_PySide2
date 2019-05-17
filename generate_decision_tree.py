
import sys
from PySide2 import QtCore, QtWidgets,QtGui
import pandas as pd
from sklearn import tree
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt

# from IPython.display import Image
# from sklearn.externals.six import StringIO
# import pydotplus

filename = '/Users/johnwondoh/PycharmProjects/untitled1/pyside_project/graduate-admissions/Admission_Predict.csv'
dataset = pd.read_csv(filename, delimiter=',')
df = pd.DataFrame(dataset)

# since the data source only contains numerical values, we don't need to do any tokenization
# Luckily, we don't need to do any data cleaning



col_names = list(df.columns)

# getting our feature set (we eliminate the serial no. since it is not interesting)
features = col_names[1:8]


labels = col_names[8]

# creating the decision tree

X = df[features]
y = pd.cut(df[labels],
       bins=[0, 0.4, 0.5, 0.6, 0.7, 0.8, 1],
       labels=["Very low", "low", "Average", "high", "Very high", "Excellent"])

class_names = y.unique().tolist()
# print(class_names)

# print(y)
clf = tree.DecisionTreeClassifier(max_depth=3)
clf = clf.fit(X, y)


# plotting
# from sklearn.externals.six import StringIO
# dot_data = StringIO()
tree.export_graphviz(clf,
                     out_file='tree.dot',
                     # out_file=dot_data,
                     feature_names=features,
                     class_names=class_names,
                     rounded = True, proportion = False,
                     precision = 2, filled = True
                     )

from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])

# Display in python
# import matplotlib.pyplot as plt
plt.figure(figsize = (14, 18))
plt.imshow(plt.imread('tree.png'))
plt.axis('off')
plt.show()


