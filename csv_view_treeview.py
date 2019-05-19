import sys
from PySide2 import QtCore, QtWidgets,QtGui
import pandas as pd
import matplotlib.pyplot as plt

filename = '/Users/johnwondoh/PycharmProjects/untitled1/pyside_project/graduate-admissions/Admission_Predict.csv'
dataset = pd.read_csv(filename, delimiter=',')
df = pd.DataFrame(dataset)

app = QtWidgets.QApplication(sys.argv)

model = QtGui.QStandardItemModel()
# parentItem = model.invisibleRootItem()

header_labels = df.columns.tolist()
data_list = df.values.tolist()

# tree = QtWidgets.QTreeWidget()
model.setHorizontalHeaderLabels(header_labels)
# model.insertRow([str(e) for e in data_list[2]])
# model.


for col_index, col_name in enumerate(header_labels):
    for row_index, name in enumerate(df[col_name].values.tolist()):
        item = QtGui.QStandardItem(str(name))
        model.setItem(row_index, col_index, item)

    # print(index, col_name)

# for row in data_list:
#     row_str = [str(elem) for elem in row ]
#     # item = QtGui.QStandardItem.appendRow('row_str')
#     # QtGui.QStandardItem.insertRow(item)
#     # item = QtGui.QStandardItem('row_str')
#     item = QtGui.QStandardItem()
#     item.setData(TitleType.DATETIME, TTPL_COL_EXTRA_DATA)
#     parentItem.appendRow(item)
#     # parentItem = item


tree_view = QtWidgets.QTreeView()
tree_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
tree_view.setModel(model)
tree_view.setUniformRowHeights(True)
tree_view.setAlternatingRowColors(True)


tree_view.show()
sys.exit(app.exec_())



if __name__ == '__main__':
    main()