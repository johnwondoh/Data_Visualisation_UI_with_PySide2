
import sys

# from PyQt5.QtWidgets import (QApplication, QGridLayout, QGroupBox,
#                              QPushButton, QRadioButton, QVBoxLayout, QWidget)
from PySide2 import QtCore, QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtGui import *

from csvviewui import TreeWidgit
from image_viewer import Viewer


class DataVisualisationApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DataVisualisationApp, self).__init__(parent)

        self.filepath = \
            '/Users/johnwondoh/PycharmProjects/untitled1/pyside_project/graduate-admissions/Admission_Predict.csv'

        grid = QtWidgets.QGridLayout()
        grid.setColumnStretch(0, 0)
        grid.setColumnStretch(1, 4)
        # grid.setRowStretch(, int stretch)

        tree = TreeWidgit(self.filepath)
        # treeWidgit = tree.get_tree_widgit()
        img_tree = tree.view_img()
        # img_widget = self.scrollable_img(img_label)
        # print(type(img_widget))


        grid.addWidget(self.buttons_for_trees(), 0, 0)
        grid.addWidget(self.buttons_for_visualisation(), 1, 0)
        grid.addWidget(tree.get_tree_widgit(), 0, 1)
        # grid.addWidget(img_tree, 1, 1)
        self.setLayout(grid)

        self.setWindowTitle("PyQt5 Group Box")
        self.resize(400, 300)

    def buttons_for_trees(self):
        tree_buttons = QtWidgets.QGroupBox('Select View Type')
        use_QTreeWidget = QtWidgets.QPushButton('Use QTreeWidget')
        use_QTreeView = QtWidgets.QPushButton('Use QTreeView')

        tree_button_layout = QtWidgets.QVBoxLayout()
        tree_button_layout.addWidget(use_QTreeWidget)
        tree_button_layout.addWidget(use_QTreeView)
        tree_button_layout.addStretch(1)
        tree_buttons.setLayout(tree_button_layout)
        return tree_buttons

    def buttons_for_visualisation(self):
        v_buttons = QtWidgets.QGroupBox('Select View Type')
        decision_tree = QtWidgets.QPushButton('Decision Tree')
        scatter_plot = QtWidgets.QPushButton('Scatter Plot')

        v_button_layout = QtWidgets.QVBoxLayout()
        v_button_layout.addWidget(decision_tree)
        v_button_layout.addWidget(scatter_plot)
        v_button_layout.addStretch(1)
        v_buttons.setLayout(v_button_layout)
        return v_buttons

    def createExampleGroup(self):
        groupBox = QtWidgets.QGroupBox("Best Food")

        radio1 = QtWidgets.QRadioButton("&Radio pizza")
        radio2 = QtWidgets.QRadioButton("R&adio taco")
        radio3 = QtWidgets.QRadioButton("Ra&dio burrito")

        radio1.setChecked(True)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    clock = DataVisualisationApp()
    clock.show()
    sys.exit(app.exec_())
