from  PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from  PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('MainWindow_Ui.ui', self)    #导入ui界面设计，传递给MainWindow。 继承了Qmainwindow。






if __name__ == '__main__':
    import sys
    """这是用loadUi导入实例方式"""
    testapp = QApplication(sys.argv)
    testui = QMainWindow()      #ui是mainwindow还是widget类型很重要，上一步的实例化千万要弄清楚，搞错就报错！
    loadUi('MainWindow_Ui.ui', testui) #经过测试，能用子类Qmainwindow，不用父类Qwidget


    testui.show()
    sys.exit(testapp.exec())






"""这是传统的方式"""
    # app = QApplication(sys.argv)
    # ui = MainWindow()
    # ui.show()
    # sys.exit(app.exec())