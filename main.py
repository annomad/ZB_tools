import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot,QDir,QFile,QIODevice,QTextStream






if __name__ == '__main__':


 app = QApplication(sys.argv) #定义个程序app，用于申请硬件系统资源

 from MainWindow import MainWindow   #MainWindow已经被载入ui文件，导入
 from slot_func import Slotfunc  # 有了导入刚刚实例化的class，再导入改写子类Slotfunc。
 mainwindow = MainWindow() #现在实例化一个windows窗口（已经包含类ui）




# 直接导入ui文件，省去pyuic转码-----------------------------------------------
 # ui = Slotfunc() # 用改写的ui类实例化一个ui控件：里面已加入类槽函数
 # ui.setupUi(mainwindow) # 利用实例化的ui方法把"实例化的窗口"作为实参传给ui，使之有一个窗口可以展示。
#------------------------------------------------------------------------


 mainwindow.show()
 sys.exit(app.exec())   #惯例写法，让程序循环。
