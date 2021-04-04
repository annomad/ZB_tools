"""这是一个槽函数集中营，继承了QT designer设计的ui，加入诸多的槽函数"""
from MainWindow import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtCore import *


class Slotfunc(MainWindow):  #继承主窗口的类
    def __init__(self):
        super().__init__()

        #建立资料库检索文本框回车键启动搜索
        self.search_lineedit.returnPressed.connect(self.searchbutton_func)#回车信号，链接搜索函数
        self.searchbutton.clicked.connect(self.searchbutton_func)   # 绑定搜索按键功能
        self.dir_treeView.doubleClicked.connect(self.opendocs_func)   # 绑定搜索按键功能







    ###################################        函数区    ###############################
    # 自动绑定信号和槽函数，点击"打开资料库"打开目录选择窗口
    @pyqtSlot()
    def on_openResource_clicked(self):
        #fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./","All Files (*);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔
        self.dir_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./") #打开目录
        # 判断程序是否有非none返回,如果不是则对treeview进行设置，并建立信号槽操作
        if self.dir_path != '':
            self.dir_model = QFileSystemModel(self)  # 实例化一个QfilesystemModel
            #再label上显示目录名称以及tooltip
            self.dispay_dir_path.setText(self.dir_path)  # 路径显示label控件显示路径的名称
            self.dispay_dir_path.setToolTip(self.dir_path)  # 提示路径绝对路径，（宽度会影响label显示，另加一个提示）
            # # 进行筛选只显示文件夹，不显示文件和特色文件
            #dir_model.setFilter(QtCore.QDir.Dirs | QtCore.QDir.NoDotAndDotDot)
            #进行treeview相关操作根目录、加载model，匹配索引
            self.dir_model.setRootPath(self.dir_path) #设置根目录
            self.dir_treeView.setModel(self.dir_model)  # 把设置好的目录model传递给treeview
            self.dir_treeView.setRootIndex(self.dir_model.index(self.dir_path))  # 把目录索引传递给treeview索引。

    # @pyqtSlot()
    def searchbutton_func(self):

        if self.search_lineedit.text() != '':
            self.search_lineedit.setToolTip('拟增加正则re表达式查询')
            try:
                if self.dir_model != None:
                    print('你搜索框输入的是：' + self.search_lineedit.text())
                    print('查看model是什么：' + str(id(self.dir_model)))
                    self.search_lineedit.selectAll()    #全选文本内容，方便下一次输入

            except AttributeError:
                print('警告：请输入制定的资料库文件')
                a = QMessageBox.warning(self, '提示', '您还尚未打开资料库！\n\n现在是否打开资料库文件？', QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)
                if a == QMessageBox.Yes:
                    self.on_openResource_clicked()
                    self.searchbutton_func()
                else:
                    print('取消打开文件')
            print('程序运行完毕')

            # self.dir_model.setNameFilters()


    # def search(str):    #定义一个信号
    #         str = self.search_linedit.Text()
    #         serch = pyqtSignal(str)

    #定义treeview列表单元双击显示按钮
    def opendocs_func(self):
        print('treeview能正确被点击')