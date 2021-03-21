"""这是一个槽函数集中营，继承了QT designer设计的ui，加入诸多的槽函数"""
from MainWindow import MainWindow
from PyQt5.QtCore import pyqtSlot

class Slotfunc(MainWindow):  #继承 QT designer设计界面的类
    def __init__(self):
        super().__init__()
        self.openResource.clicked.connect(self.test)
        self.a = 1

    def test(self):
        print("资料库按钮被点击类")

    @pyqtSlot()
    def on_openResource_clicked(self):   #这是添加打开资料库的功能。
        print('这是个按钮和槽函数----自动绑定的测试:')










