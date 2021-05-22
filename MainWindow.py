from PyQt5.uic import loadUi
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
# import sys
# import os
# from PyQt5 import QtCore
"""这个才是主界面的设计窗口，包括ui定义，以及其他美化的东西"""
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('MainWindow_Ui.ui', self)    #导入ui界面设计，传递给MainWindow。 继承了Qmainwindow。
        self.setWindowTitle('招投标制作工具')

        # 初始化界面
        self.progressBar.hide()  # 隐藏进度条

    # 定义一个警示动画
    def Alert_animation(self, kongjian):  # 做一个警示动画类，做一些重要的提醒
        x = kongjian.geometry().x()  # 获得坐标和y值
        y = kongjian.geometry().y()  # 获得坐标和y值
        w = kongjian.geometry().width()  # 获得坐标和w值
        h = kongjian.geometry().height()  # 获得坐标和h值
        print("输出x坐标为 ,y坐标为d", x, y)
        animation1 = QPropertyAnimation(kongjian, b'geometry', self)  # geometry是坐标+大小，pos是坐标
        animation1.setKeyValueAt(0, QRect(x + 0, y, w, h))  # 此处有bug ， 第二次执行会让变量增加。
        animation1.setKeyValueAt(0.2, QRect(x - 10, y, w, h))
        animation1.setKeyValueAt(0.4, QRect(x + 10, y, w, h))
        animation1.setKeyValueAt(0.65, QRect(x - 10, y, w, h))
        animation1.setKeyValueAt(0.80, QRect(x + 10, y, w, h))
        animation1.setKeyValueAt(0.90, QRect(x - 10, y, w, h))
        animation1.setKeyValueAt(0.95, QRect(x + 10, y, w, h))
        animation1.setKeyValueAt(1, QRect(x, y, w, h))
        animation1.setDuration(300)  # 设置间隔
        animation1.setLoopCount(2)  # 重复3次
        animation1.start(QAbstractAnimation.DeleteWhenStopped)  # 动画完毕后删除动画















if __name__ == '__main__':
    import sys
    """这是用loadUi导入实例方式"""
    testapp = QApplication(sys.argv)
    testui = QMainWindow()      #ui是mainwindow还是widget类型很重要，上一步的实例化千万要弄清楚，搞错就报错！
    loadUi('MainWindow_Ui.ui', testui) #经过测试，能用子类Qmainwindow，不用父类Qwidget
    testui.show()
    sys.exit(testapp.exec())
