import sys
from PySide2 import QtCore, QtWidgets, QtGui
import pandas as pd
import matplotlib.pyplot as plt

import csv


class TreeWidgit(QtWidgets.QWidget):
    def __init__(self, filename, parent=None):
        super(TreeWidgit, self).__init__(parent)
        self.filename = filename

    def put_data_in_ranges(self, p_ranges, data):
        n = len(data[1]) - 1
        range_dict = {}
        for r in p_ranges:
            range_dict[r] = [row for row in data if r[0] <= row[n] < r[1]]
        return range_dict

    def create_tree_and_subtrees(self, tr, tree_dic):
        for key in tree_dic:
            root_elem = ['', '', '', '', '', '', '', '']
            range_string = str(key[0]) + ' - ' + str(key[1])
            root_elem.append(range_string)
            root = QtWidgets.QTreeWidgetItem(tr, root_elem)
            for sub_tree_list in tree_dic[key]:
                sub_tree_list_str = [str(e) for e in sub_tree_list]
                QtWidgets.QTreeWidgetItem(root, sub_tree_list_str)

    def get_tree_widgit(self):
        layout = QtWidgets.QVBoxLayout()

        dataset = pd.read_csv(self.filename, delimiter=',')
        df = pd.DataFrame(dataset)

        header_labels = df.columns.tolist()
        data_list = df.values.tolist()

        tree = QtWidgets.QTreeWidget()
        tree.setHeaderLabels(header_labels)
        tree.setAlternatingRowColors(True)

        ranges = [(0, 0.4),
                  (0.4, 0.5),
                  (0.6, 0.7),
                  (0.7, 0.8),
                  (0.8, 0.9),
                  (0.9, 1)
                  ]

        tree_range = self.put_data_in_ranges(ranges, data_list)
        self.create_tree_and_subtrees(tree, tree_range)
        layout.addWidget(tree)

        group = QtWidgets.QGroupBox("View CSV with QTreeWidget")
        group.setLayout(layout)
        return group

    def view_img(self):
        # window = QtWidgets.QWidget()
        img_layout = QtWidgets.QVBoxLayout()

        pixmap = QtGui.QPixmap('tree.png')
        # pixmap = pixmap.scaledToWidth(500)
        label = QtWidgets.QLabel()
        label.setPixmap(pixmap)

        img_layout.addWidget(label)
        img_group = QtWidgets.QGroupBox("Visualise Decision Tree")
        img_group.setLayout(img_layout)
        # img_group.setMaximumHeight(200)
        return img_group

    def view_img2(self):
        # img_layout = QtWidgets.QVBoxLayout()
        pixmap = QtGui.QPixmap('scatter_graph.png')
        label = QtWidgets.QLabel()
        label.setPixmap(pixmap)

        # img_layout.addWidget(label)

        # img_group = QtWidgets.QGroupBox("Visualise Decision Tree")
        # img_group.setLayout(img_layout)
        # img_group.setMaximumHeight(200)
        # return img_group
        return label




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(window)

    f = filepath = '/Users/johnwondoh/PycharmProjects/untitled1/pyside_project/graduate-admissions/Admission_Predict.csv'
    tw = TreeWidgit(f)
    layout.addWidget(tw.get_tree_widgit())
    window.show()
    sys.exit(app.exec_())
