
import pandas as pd
from sklearn import tree
from subprocess import call


class DecisionTreeClassifier():
    def __init__(self, filename):
        self.filename = filename
        self.dataset = pd.read_csv(self.filename, delimiter=',')
        self.df = pd.DataFrame(self.dataset)
        # since the data source only contains numerical values, we don't need to do any tokenization
        # Luckily, we don't need to do any data cleaning
        self.col_names = list(self.df.columns)
        # getting our feature set (we eliminate the serial no. since it is not interesting)
        self.features = self.col_names[1:8]
        self.labels = self.col_names[8]

    # creating the decision tree
    def decision_tree(self):
        # classifier
        X = self.df[self.features]
        y = pd.cut(self.df[self.labels],
               bins=[0, 0.4, 0.5, 0.6, 0.7, 0.8, 1],
               labels=["Very low", "low", "Average", "high", "Very high", "Excellent"])

        class_names = y.unique().tolist()
        clf = tree.DecisionTreeClassifier(max_depth=3)
        clf = clf.fit(X, y)

        # plotting
        tree.export_graphviz(clf,
                             out_file='tree.dot',
                             # out_file=dot_data,
                             feature_names=self.features,
                             class_names=class_names,
                             rounded = True, proportion = False,
                             precision = 2, filled = True
                             )
        call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=50'])

        # plt.figure(figsize = (10, 10))
        # plt.imshow(plt.imread('tree.png'))
        # plt.axis('off')
        # plt.show()


# filepath = '/Users/johnwondoh/PycharmProjects/untitled1/pyside_project/graduate-admissions/Admission_Predict.csv'
# DecisionTreeClassifier(filepath).decision_tree()
