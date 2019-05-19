
import sys
from PySide2 import QtWidgets

# from other py files
from csvviewui import TreeMain
from treeanalysis import Classification


class DataVisualisationApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DataVisualisationApp, self).__init__(parent)

        self.filepath = \
            '/Users/johnwondoh/PycharmProjects/untitled1/pyside_project/graduate-admissions/Admission_Predict.csv'

        # Setting up visualisation
        self.plots = Classification(self.filepath)
        self.plots.decision_tree()
        self.plots.scatter_plots()

        self.grid = QtWidgets.QGridLayout()

        self.btn_QTreeWidget = QtWidgets.QPushButton('Use QTreeWidget')
        self.btn_QTreeView = QtWidgets.QPushButton('Use QTreeView')
        self.btn_decision_tree = QtWidgets.QPushButton('Decision Tree')
        self.btn_scatter_plot = QtWidgets.QPushButton('Scatter Plot')

        # set the style sheet for when the buttons are clicked
        self.set_clicked_style = 'QPushButton {' \
                                 'width: 100px;' \
                                 'background-color: #4286f4; ' \
                                 'border-radius: 2px;' \
                                 '}'

        self.tree = TreeMain(self.filepath)

        # create placeholders to be added to the grid
        self.placeholder1 = QtWidgets.QLabel()
        self.placeholder1.setText('Select method to view the data')

        self.placeholder2 = QtWidgets.QLabel()
        self.placeholder2.setText('Select your preferred visualisation type')
        # self.img_tree = self.tree.view_img()

        self.grid_ui()

        # make connections to buttons
        self.btn_QTreeWidget.clicked.connect(self.on_click_QTreeWidget)
        self.btn_QTreeView.clicked.connect(self.on_click_QTreeView)
        self.btn_decision_tree.clicked.connect(self.on_click_decision_tree)
        self.btn_scatter_plot.clicked.connect(self.on_click_scatter_plot)

    def grid_ui(self):
        self.grid.setColumnStretch(0, 0)
        self.grid.setColumnStretch(1, 4)
        # grid.setRowStretch(, int stretch)

        self.grid.addWidget(self.buttons_for_trees(), 0, 0)
        self.grid.addWidget(self.buttons_for_visualisation(), 1, 0)
        self.grid.addWidget(self.placeholder1, 0, 1)
        self.grid.addWidget(self.placeholder2, 1, 1)
        self.setLayout(self.grid)

        self.setWindowTitle("PyQt5 Group Box")
        self.resize(1000, 800)

    def buttons_for_trees(self):
        tree_button_layout = QtWidgets.QVBoxLayout()
        tree_button_layout.addWidget(self.btn_QTreeWidget)
        tree_button_layout.addWidget(self.btn_QTreeView)
        tree_button_layout.addStretch(1)

        tree_buttons = QtWidgets.QGroupBox('Select Tree View Type')
        tree_buttons.setLayout(tree_button_layout)
        return tree_buttons

    def buttons_for_visualisation(self):
        v_button_layout = QtWidgets.QVBoxLayout()
        v_button_layout.addWidget(self.btn_decision_tree)
        v_button_layout.addWidget(self.btn_scatter_plot)
        v_button_layout.addStretch(1)

        v_buttons = QtWidgets.QGroupBox('Select Visualisation type Type')
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
    # @pyqtSlot()
    def on_click_QTreeView(self):
        # toggling button clicked
        self.btn_QTreeView.setStyleSheet(self.set_clicked_style)
        self.btn_QTreeWidget.setStyleSheet('')

        # add widget
        view = self.grid.itemAtPosition(0, 1).widget()
        view.setParent(None)
        new_tree_view = self.tree.get_tree_view()
        self.grid.addWidget(new_tree_view, 0, 1)

    def on_click_QTreeWidget(self):
        self.btn_QTreeWidget.setStyleSheet(self.set_clicked_style)
        self.btn_QTreeView.setStyleSheet('')

        widget = self.grid.itemAtPosition(0, 1).widget()
        widget.setParent(None)
        new_tree_widget = self.tree.get_tree_widget()
        self.grid.addWidget(new_tree_widget, 0, 1)

    def on_click_decision_tree(self):
        self.btn_decision_tree.setStyleSheet(self.set_clicked_style)
        self.btn_scatter_plot.setStyleSheet('')

        img_widget = self.grid.itemAtPosition(1, 1).widget()
        img_widget.setParent(None)

        new_img_box = QtWidgets.QGroupBox("Visualise Decision Tree")
        new_img = self.tree.view_tree_plot_img()
        new_img_box.setLayout(new_img)
        self.grid.addWidget(new_img_box, 1, 1)

    def on_click_scatter_plot(self):
        self.btn_scatter_plot.setStyleSheet(self.set_clicked_style)
        self.btn_decision_tree.setStyleSheet('')

        img_widget = self.grid.itemAtPosition(1, 1).widget()
        img_widget.setParent(None)

        new_img_box = QtWidgets.QGroupBox("Visualise Scatter Plot")
        new_img = self.tree.view_scatter_plot_img()
        new_img_box.setLayout(new_img)
        self.grid.addWidget(new_img_box, 1, 1)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    clock = DataVisualisationApp()
    clock.show()
    sys.exit(app.exec_())
