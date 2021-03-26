"""这是一个槽函数集中营，继承了QT designer设计的ui，加入诸多的槽函数"""
from MainWindow import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Slotfunc(MainWindow):  #继承主窗口的类
    def __init__(self):
        super().__init__()

    # 自动绑定信号和槽函数，点击"打开资料库"打开目录选择窗口
    @pyqtSlot()
    def on_openResource_clicked(self):
        #fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./","All Files (*);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔

        dir_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./") #打开目录
        print(dir_path)

        dir_model = QDirModel()
        # 进行筛选只显示文件夹，不显示文件和特色文件
        # self.dir_model.setFilter(QtCore.QDir.Dirs | QtCore.QDir.NoDotAndDotDot)
        self.dir_treeView.setModel(dir_model)
        print(self.dir_treeView)
        # dir_model.setRootIndex(dir_path)
        self.dir_treeView.setModel(dir_model)  #显示里面的内容















