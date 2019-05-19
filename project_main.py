
import sys

# from PyQt5.QtWidgets import (QApplication, QGridLayout, QGroupBox,
#                              QPushButton, QRadioButton, QVBoxLayout, QWidget)
from PySide2 import QtCore, QtWidgets, QtGui

from PyQt5.QtCore import *
from PyQt5.QtGui import *

from csvviewui import TreeWidgit
from image_viewer import Viewer


class DataVisualisationApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DataVisualisationApp, self).__init__(parent)

        self.filepath = \
            '/Users/johnwondoh/PycharmProjects/untitled1/pyside_project/graduate-admissions/Admission_Predict.csv'

        self.grid = QtWidgets.QGridLayout()

        self.btn_QTreeWidget = QtWidgets.QPushButton('Use QTreeWidget')
        self.btn_QTreeView = QtWidgets.QPushButton('Use QTreeView')
        self.btn_decision_tree = QtWidgets.QPushButton('Decision Tree')
        self.btn_scatter_plot = QtWidgets.QPushButton('Scatter Plot')
        # self.new_btn = QtWidgets.QPushButton('new button')

        self.tree = TreeWidgit(self.filepath)
        self.treeWidget = self.tree.get_tree_widget()
        self.treeView = self.tree.get_tree_view()
        print(type(self.treeView))

        self.img = self.tree.view_img3()

        self.img_box = QtWidgets.QGroupBox("Visualise Decision Tree")
        self.img_box.setLayout(self.img)
        # self.img_tree = self.tree.view_img()

        self.grid_ui()

        self.btn_QTreeWidget.clicked.connect(self.on_click_QTreeWidget)
        self.btn_QTreeView.clicked.connect(self.on_click_QTreeView)

    def grid_ui(self):
        self.grid.setColumnStretch(0, 0)
        self.grid.setColumnStretch(1, 4)
        # grid.setRowStretch(, int stretch)

        self.grid.addWidget(self.buttons_for_trees(), 0, 0)
        self.grid.addWidget(self.buttons_for_visualisation(), 1, 0)
        self.grid.addWidget(self.treeWidget, 0, 1)
        self.grid.addWidget(self.img_box, 1, 1)
        self.setLayout(self.grid)

        self.setWindowTitle("PyQt5 Group Box")
        self.resize(800, 500)

    def buttons_for_trees(self):
        tree_buttons = QtWidgets.QGroupBox('Select Tree View Type')
        # use_QTreeWidget = QtWidgets.QPushButton('Use QTreeWidget')
        # use_QTreeView = QtWidgets.QPushButton('Use QTreeView')

        tree_button_layout = QtWidgets.QVBoxLayout()
        tree_button_layout.addWidget(self.btn_QTreeWidget)
        tree_button_layout.addWidget(self.btn_QTreeView)
        tree_button_layout.addStretch(1)
        tree_buttons.setLayout(tree_button_layout)
        return tree_buttons

    def buttons_for_visualisation(self):
        v_buttons = QtWidgets.QGroupBox('Select Visualisation type Type')
        # decision_tree = QtWidgets.QPushButton('Decision Tree')
        # scatter_plot = QtWidgets.QPushButton('Scatter Plot')

        v_button_layout = QtWidgets.QVBoxLayout()
        v_button_layout.addWidget(self.btn_decision_tree)
        v_button_layout.addWidget(self.btn_scatter_plot)
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

    # actions
    @pyqtSlot()
    def on_click_QTreeView(self):
        print('tree view clicked')

        view = self.grid.itemAtPosition(0, 1).widget()
        view.setParent(None)

        # new_img_box = QtWidgets.QGroupBox("Visualise Decision Tree")
        new_tree_view = self.tree.get_tree_view()
        # new_img_box.setLayout(new_img)
        self.grid.addWidget(new_tree_view, 0, 1)

    def on_click_QTreeWidget(self):
        print('tree qtwidget clicked')

        widget = self.grid.itemAtPosition(0, 1).widget()
        widget.setParent(None)

        # new_img_box = QtWidgets.QGroupBox("Visualise Decision Tree")
        new_tree_widget = self.tree.get_tree_widget()
        # new_img_box.setLayout(new_img)
        self.grid.addWidget(new_tree_widget, 0, 1)

    def on_click_decision_tree(self):
        print('clicked')

        img_widget = self.grid.itemAtPosition(1, 1).widget()
        img_widget.setParent(None)

        new_img_box = QtWidgets.QGroupBox("Visualise Decision Tree")
        new_img = self.tree.view_img4()
        new_img_box.setLayout(new_img)
        self.grid.addWidget(new_img_box, 1, 1)


    def on_click_scatter_plot(self):
        print('scatter plot clicked')

        img_widget = self.grid.itemAtPosition(1, 1).widget()
        img_widget.setParent(None)

        new_img_box = QtWidgets.QGroupBox("Visualise Scatter Plot")
        new_img = self.tree.view_img4()
        new_img_box.setLayout(new_img)
        self.grid.addWidget(new_img_box, 1, 1)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    clock = DataVisualisationApp()
    clock.show()
    sys.exit(app.exec_())
