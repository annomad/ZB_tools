import sys,os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir,QStringListModel,QSortFilterProxyModel,QModelIndex
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QFileSystemModel,
                             QListView, QTreeView, QVBoxLayout, QAbstractItemView)
 
class DemoModel(QWidget):
    def __init__(self, parent=None):
        super(DemoModel, self).__init__(parent)
        
         # 设置窗口标题
        self.setWindowTitle('实战PyQt5: Model-View框架演示')      
        # 设置窗口大小
        self.resize(640, 480)
      
        self.initUi()
        
    def initUi(self):
        vLayout = QVBoxLayout(self)
        
        vLayout.addWidget(QLabel('QStringListModel 演示'))
        vLayout.addWidget(self.createStringListModelDemo())
        
        vLayout.addWidget(QLabel('QFileSystemModel 演示'))
        vLayout.addWidget(self.createFileSystemModelDemo())
        
        vLayout.addWidget(QLabel('QSortFilterProxyModel 演示'))
        vLayout.addWidget(self.createSortFilterProxyModelDemo())
        
        self.setLayout(vLayout)
        
    def createStringListModelDemo(self):
        slm = QStringListModel()
        lv = QListView(self)
        sportNames=('篮球','足球','网球','羽毛球','橄榄球')
        slm.setStringList(sportNames)
        lv.setModel(slm)
        lv.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked)
        
        return lv   #这个return蛮屌的。

    def createFileSystemModelDemo(self):     
        #创建文件系统模型
        fsm = QFileSystemModel()
        fsm.setRootPath(QDir.currentPath())
        #树状视图
        tv = QTreeView(self)
        tv.setModel(fsm)
        tv.setRootIndex(fsm.index(QDir.currentPath()))
 
        return tv
                
    def createSortFilterProxyModelDemo(self):
        #创建文件系统模型
        fsm = QFileSystemModel()
        fsm.setRootPath(QDir.currentPath())
        #代理模型
        sfpm = QSortFilterProxyModel()
        sfpm.setFilterKeyColumn(1)
        sfpm.setSourceModel(fsm)
        
        #树状视图
        tv = QTreeView(self)
        #为视图指定模型
        tv.setModel(sfpm)
        #指定根索引
        tv.setRootIndex(sfpm.index(0, 0, QModelIndex()))
 
        return tv
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoModel()
    window.show()
    sys.exit(app.exec())