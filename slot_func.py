"""这是一个槽函数集中营，继承了QT designer设计的ui，加入诸多的槽函数"""
from MainWindow import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtCore import *


class Slotfunc(MainWindow):  # 继承主窗口的类
    def __init__(self):
        super().__init__()

        self.search_lineedit.returnPressed.connect(self.searchbutton_func)  # 回车信号，链接搜索函数
        self.search_lineedit.editingFinished.connect(self.research_func)  # 结束编辑，重新展示函数
        self.searchbutton.clicked.connect(self.searchbutton_func)  # 绑定搜索按键功能
        self.dir_treeView.doubleClicked.connect(self.opendocs_func)  # 你编写打开doc文档功能

        # 初始化变量
        self.dir_path = ''  # 初始化资料库目录变量
        self.dir_model = QFileSystemModel(self)  # 实例化一个QfilesystemModel


    # ##################################        函数区    ###############################
    # ##################################        函数区    ###############################
    # ##################################        函数区    ###############################

    # 自动绑定信号和槽函数，点击"打开资料库"打开目录选择窗口
    @pyqtSlot()
    def on_openResource_clicked(self):  # 打开资源库按钮
        # fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./","All Files (*);;Excel Files (*.xls)")
        # 设置文件扩展名过滤,注意用双分号间隔
        self.dir_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 打开目录
        # 判断程序是否有非none返回,如果不是则对treeview进行设置，并建立信号槽操作
        if self.dir_path != '':
            self.dispay_dir_path.setText(self.dir_path)  # 路径显示label控件显示路径的名称
            self.dispay_dir_path.setToolTip(self.dir_path)  # 提示路径绝对路径，（宽度会影响label显示，另加一个提示）
            # # 进行筛选只显示文件夹，不显示文件和特色文件
            # dir_model.setFilter(QtCore.QDir.Dirs | QtCore.QDir.NoDotAndDotDot)
            # 进行 treeview 相关操作根目录、加载model，匹配索引
            self.dir_model.setRootPath(self.dir_path)  # 设置根目录
            self.dir_treeView.setModel(self.dir_model)  # 把设置好的目录model传递给treeview
            self.dir_treeView.setRootIndex(self.dir_model.index(self.dir_path))  # 把目录索引传递给treeview索引。
            for i in [1, 2, 3]:
                self.dir_treeView.setColumnHidden(i, True)

    # @pyqtSlot()
    def searchbutton_func(self):  # 搜索按钮功能键
        self.Alert_animation(self.search_lineedit) ##############################################
        self.search_lineedit.setToolTip('拟增加正则re表达式查询功能')
        self.search_lineedit.setStyleSheet('border: none; background: none')  # 设置背景色
        # self.research_func()    # 先检查下搜索框是否是空值，如果是空值，则禁用名称过滤  有待商榷？
        self.dir_model.setNameFilterDisables(False)  # 如果是Ture，则显示灰色的非目标，False直接隐藏
        if self.search_lineedit.text() != '':
            try:
                if self.dir_path != '':
                    print('你搜索框输入的是：' + self.search_lineedit.text())
                    self.search_lineedit.selectAll()  # 全选文本内容，方便下一次输入
                    self.search_lineedit.setFocus()
                    self.dir_model.setNameFilters(['*' + self.search_lineedit.text() + '*'])  # 搜索功能核心，设置名字过滤器
                    # self.dir_model.setnam   # 设置非目标文件不可见。。
                else:
                    print('警告：请输入制定的资料库文件')
                    a = QMessageBox.warning(self, '提示', '您还尚未打开任何资料库！\n\n现在是否选择一个资料库打开？',
                                            QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)
                    if a == QMessageBox.Yes:
                        self.on_openResource_clicked()
                        self.searchbutton_func()
                        self.search_lineedit.setStyleSheet('border: none; background: cyan')
                        self.Alert_animation(self.search_lineedit)
                    else:
                        print('取消打开文件')
            except AttributeError:
                pass

            # self.dir_model.setNameFilters()

    def opendocs_func(self, qmodel_index):  # 定义treeview列表单元双击功能
        print(self.dir_model.filePath(qmodel_index))  # 传递 双击对象的的绝对路径
        # print(self.dir_model.fileName(qmodel_index))  # 打印双击对象的文件名称，没有路径
        # print(self.dir_model.fileInfo(qmodel_index))  # 打印双击对象的类型
        if not self.dir_model.fileInfo(qmodel_index).isDir():  # 如果不是目录，则告知这是一个文件
            print('这是一个文件')

    def research_func(self):  # 非空重搜索
        if self.search_lineedit.text() == '':
            self.search_lineedit.setStyleSheet('border: none; background: none')  # 设置背景色
            self.dir_model.setNameFilters([])
        pass  # 拟开启资料库搜索功能

    def Alert_animation(self, kongjian):  # 做一个警示动画，做一些重要的提醒
        x = kongjian.geometry().x()# 获得坐标和y值
        y = kongjian.geometry().y()# 获得坐标和y值
        print("输出x坐标为 ,y坐标为d", x, y)
        animation1 = QPropertyAnimation(kongjian, b'pos', self)    #geometry是坐标+大小，pos是坐标

        animation1.setKeyValueAt(0, QPoint(x+10, y+1))
        animation1.setKeyValueAt(0.25, QPoint(x-10, y-1))
        animation1.setKeyValueAt(0.5, QPoint(x+5, y+1))
        animation1.setKeyValueAt(0.75, QPoint(x-5, y-1))
        animation1.setKeyValueAt(1, QPoint(x, y))
        animation1.setDuration(1000)
        animation1.start()
        print('动画出现了么')
