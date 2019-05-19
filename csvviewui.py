import sys
from PySide2 import QtCore, QtWidgets, QtGui
import pandas as pd


class TreeMain(QtWidgets.QWidget):
    def __init__(self, filename, parent=None):
        super(TreeMain, self).__init__(parent)
        self.filename = filename
        self.dataset = pd.read_csv(self.filename, delimiter=',')
        self.df = pd.DataFrame(self.dataset)

        self.header_labels = self.df.columns.tolist()
        self.data_list = self.df.values.tolist()

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

    def get_tree_widget(self):
        layout = QtWidgets.QVBoxLayout()

        tree = QtWidgets.QTreeWidget()
        tree.setHeaderLabels(self.header_labels)
        tree.setAlternatingRowColors(True)

        ranges = [(0, 0.4),
                  (0.4, 0.5),
                  (0.6, 0.7),
                  (0.7, 0.8),
                  (0.8, 0.9),
                  (0.9, 1)
                  ]

        tree_range = self.put_data_in_ranges(ranges, self.data_list)
        self.create_tree_and_subtrees(tree, tree_range)
        layout.addWidget(tree)

        group = QtWidgets.QGroupBox("View CSV with QTreeWidget")
        group.setLayout(layout)
        return group

    def get_tree_view(self):
        view_layout = QtWidgets.QVBoxLayout()
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(self.header_labels)

        for col_index, col_name in enumerate(self.header_labels):
            for row_index, name in enumerate(self.df[col_name].values.tolist()):
                item = QtGui.QStandardItem(str(name))
                model.setItem(row_index, col_index, item)

        tree_view = QtWidgets.QTreeView()
        tree_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        tree_view.setModel(model)
        tree_view.setUniformRowHeights(True)
        tree_view.setAlternatingRowColors(True)

        view_layout.addWidget(tree_view)

        group_view = QtWidgets.QGroupBox("View CSV with QTreeView")
        group_view.setLayout(view_layout)
        return group_view

    def view_tree_plot_img(self):
        tree_img_layout = QtWidgets.QVBoxLayout()

        pixmap = QtGui.QPixmap('tree.png')
        t_label = QtWidgets.QLabel()
        t_label.setPixmap(pixmap)

        tree_img_layout.addWidget(t_label)
        return tree_img_layout

    def view_scatter_plot_img(self):
        scatter_plot_img_layout = QtWidgets.QVBoxLayout()

        pixmap = QtGui.QPixmap('scatter_graph.png')
        s_label = QtWidgets.QLabel()
        s_label.setPixmap(pixmap)

        scatter_plot_img_layout.addWidget(s_label)
        return scatter_plot_img_layout


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(window)

    f = filepath = '/Users/johnwondoh/PycharmProjects/untitled1/pyside_project/graduate-admissions/Admission_Predict.csv'
    tw = TreeMain(f)
    layout.addWidget(tw.get_tree_widgit())
    window.show()
    sys.exit(app.exec_())
