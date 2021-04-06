import sys, os
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QDirModel

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file system view - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def tree_cilcked(self, Qmodelidx):
        print(self.model.filePath(Qmodelidx))
        print(self.model.fileName(Qmodelidx))
        print(self.model.fileInfo(Qmodelidx))

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # 这里得到目录结构
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())
        # 这里过滤，只显示 py 文件
        mf = self.model.setNameFilters(['*.py'])
        self.model.setNameFilterDisables(False)
        # 这里做展示
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QDir.currentPath()))
        self.tree.doubleClicked.connect(self.tree_cilcked)
        # 这里隐藏了目录信息展示
        for i in [1, 2, 3]:
            self.tree.setColumnHidden(i, True)
        # 缩进
        self.tree.setIndentation(10)
        self.tree.setWindowTitle("Dir View")
        self.tree.resize(640, 480)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.setLayout(windowLayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
