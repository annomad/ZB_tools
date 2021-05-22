import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, QDir, QFile, QIODevice, QTextStream
import logging


if __name__ == '__main__':

 logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
 logging.debug('Start of programe')

 app = QApplication(sys.argv)  # 定义个程序app，用于申请硬件系统资源
 #  思路直接用loadUi形成窗口类MainWindow（），在用slotfunc（）继承MainWindow（）类，并改写。
 #  这样的好处就是把槽函数和Ui函数分开。

 from slot_func import Slotfunc
 testui = QMainWindow()
 mywindow = Slotfunc()  # 以按键为线索的类给他实例化
 mywindow.show()
 sys.exit(app.exec())   # 惯例写法，让程序循环。
