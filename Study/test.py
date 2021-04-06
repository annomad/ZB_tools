from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(900, 600)
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("click")
        self.myButton.clicked.connect(self.msg)

    @pyqtSlot()
    def msg(self):
        # directory1 = QFileDialog.getExistingDirectory(self,"选取文件夹","./")   #起始路径
        # print(directory1)

        fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                          "All Files (*);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(fileName1, filetype)

        # files, ok1 = QFileDialog.getOpenFileNames(self,"多文件选择", "./", "All Files (*);;Text Files (*.txt)")
        # print(files,ok1)

        # fileName2, ok2 = QFileDialog.getSaveFileName(self,"文件保存", "./","All Files (*);;Text Files (*.txt)")
        # a = QMessageBox.information(self, '提示', '请指定一个资料库文件', QMessageBox.Yes | QMessageBox.No)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()

    sys.exit(app.exec_())
