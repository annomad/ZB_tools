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
        self.opendirwin = OpenDirWin()
        self.opendirwin.show()
        # self.opendirwin.setWindowFlags()# 打开窗口，并设置了独占窗口

    # @pyqtSlot(
    # def on_openResourceWinOk_clicked(self):    #查询窗口的确定按钮
    #     print('运行到这一步了么')
    #     _signal = pyqtSignal(dir_str)
    #
    #     dir_str = self.labelopendir.text()
    #
    #     self._signal.emit(dir_str)
    #     self.opendir_win.close












