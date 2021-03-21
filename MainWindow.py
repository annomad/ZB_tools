from  PyQt5.QtWidgets import QMainWindow,QApplication
from  PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('MainWindow_Ui.ui', self)    #导入ui界面设计，传递给MainWindow。 继承了Qmainwindow。






# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     ui = MainWindow()
#     ui.show()
#     sys.exit(app.exec())