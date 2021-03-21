"""这是一个槽函数集中营，继承了QT designer设计的ui，加入诸多的槽函数"""
from MainWindow import MainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from  PyQt5.uic import loadUi

class Slotfunc(MainWindow):  #继承 QT designer设计界面的类
    def __init__(self):
        super().__init__()
        self.setWindowTitle('招投标制作工具')
        # self.openResource.clicked.connect(self.test)
        # self.a = 1



    @pyqtSlot()
    def on_openResource_clicked(self):   #这是添加打开资料库的功能。打开查询窗口
        print('这是个按钮和槽函数----自动绑定的测试:')
        self.opendir_win = QDialog()
        loadUi('open_dir.ui', self.opendir_win)
        self.opendir_win.setWindowTitle('这是第二个窗口')
        print(self.opendir_win.windowTitle())
        self.opendir_win.show()










