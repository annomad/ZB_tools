"""这是一个槽函数集中营，继承了QT designer设计的ui，加入诸多的槽函数"""
from MainWindow import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# import threading
import docx
# import time


class Slotfunc(MainWindow):  # 继承主窗口的类

    progressBar_signal = pyqtSignal(int, int)  # 定义一个进度条的信号。

    def __init__(self):
        super().__init__()



        # 初始化变量
        self.dir_path = ''  # 初始化资料库目录变量
        self.dir_model = QFileSystemModel(self)  # 实例化一个QfilesystemModel
        self.filelistsview_model = QStandardItemModel()     # 定义一个直接显示文件的model
        self.oswalk_QTHread = Oswalk_thread(self.dir_path)      # 定义一个线程
        self.contextsearch_button.setEnabled(False)  # 内容搜索按钮暂时失效。

        self.search_lineedit.returnPressed.connect(self.searchbutton_func)  # 回车信号，链接搜索函数
        # self.search_lineedit.textChanged.connect(self.searchbutton_func)  # 内容改变信号，链接搜索函数
        self.search_lineedit.editingFinished.connect(self.research_func)  # 结束编辑，重新展示函数
        self.searchbutton.clicked.connect(self.searchbutton_func)  # 绑定搜索按键功能
        self.contextsearch_button.clicked.connect(self.serch_inDir)  # 文件列表展示功能
        self.dir_treeView.doubleClicked.connect(self.opendocs_func)  # 你编写打开doc文档功能
        self.progressBar_signal.connect(self.pBar_view)  # 进度条信号绑定槽函数



    # ##################################        函数区    ###############################
    # ##################################        函数区    ###############################
    # ##################################        函数区    ###############################

    # 自动绑定信号和槽函数，点击"打开资料库"打开目录选择窗口
    @pyqtSlot()
    def on_openResource_clicked(self):  # 打开资源库按钮

        # fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./","All Files (*);;Excel Files (*.xls)")
        # 设置文件扩展名过滤,注意用双分号间隔
        self.dir_path_temp = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 打开目录
        #  判断下打开文件被取消了
        if self.dir_path_temp:
            self.dir_path = self.dir_path_temp

            # 载入文件结构model
            self.load_dir_model()

            # 定义一个线程Oswalk的线程
            self.oswalk_QTHread = Oswalk_thread(self.dir_path)  # 创建一个多线程的实例.
            self.oswalk_QTHread.oswalkFinished_signal.connect(self.receivesignal_oswalkFunc)  # THread现场信号连接函数
            self.oswalk_QTHread.start()
            self.contextsearch_button.setEnabled(False)  # 内容搜索暂时失效。

    def load_dir_model(self):       # 加载文件目录结构的model功能
        if self.dir_path != '':
            self.dispay_dir_path.setText(self.dir_path)  # 路径显示label控件显示路径的名称
            self.dispay_dir_path.setToolTip(self.dir_path)  # 提示路径绝对路径，（宽度会影响label显示，另加一个提示）
            # # 进行筛选只显示文件夹，不显示文件和特色文件
            # dir_model.setFilter(QtCore.QDir.Dirs | QtCore.QDir.NoDotAndDotDot)
            # 进行 treeview 相关操作根目录、加载model，匹配索引
            self.dir_model.setRootPath(self.dir_path)  # 设置根目录
            self.dir_treeView.setModel(self.dir_model)  # 把设置好的目录model传递给treeview
            self.dir_treeView.setRootIndex(self.dir_model.index(self.dir_path))  # 把目录索引传递给treeview索引，必须有！
            for i in [1, 2, 3]:
                self.dir_treeView.setColumnHidden(i, True)

    # @pyqtSlot()
    def searchbutton_func(self):  # 搜索按钮功能键
        self.load_dir_model()       # 加载文件目录model

        self.Alert_animation(self.search_lineedit)  # 装在一个动画警示？
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
        try:
            if not self.dir_model.filePath(qmodel_index) == '':
                print('这是一个实心的鼠标')
        except:
            print('这是一个     空心的鼠标')

        print(self.dir_model.filePath(qmodel_index))  # 传递 双击对象的的绝对路径
        if not self.dir_model.fileInfo(qmodel_index).isDir():  # 如果不是目录，则告知这是一个文件
            print('这是一个文件')
            self.Docxviewer(self.dir_model.filePath(qmodel_index))

    def research_func(self):  # 非空重搜索
        if self.search_lineedit.text() == '':
            self.search_lineedit.setStyleSheet('border: none; background: none')  # 设置背景色
            self.dir_model.setNameFilters([])
        pass  # 拟开启资料库搜索功能

    def Alert_animation(self, kongjian):  # 做一个警示动画类，做一些重要的提醒
        x = kongjian.geometry().x()     # 获得坐标和y值
        y = kongjian.geometry().y()     # 获得坐标和y值
        w = kongjian.geometry().width()     # 获得坐标和w值
        h = kongjian.geometry().height()        # 获得坐标和h值
        print("输出x坐标为 ,y坐标为d", x, y)
        animation1 = QPropertyAnimation(kongjian, b'geometry', self)    # geometry是坐标+大小，pos是坐标
        animation1.setKeyValueAt(0, QRect(x+0, y, w, h))    # 此处有bug ， 第二次执行会让变量增加。
        animation1.setKeyValueAt(0.2, QRect(x-10, y, w, h))
        animation1.setKeyValueAt(0.4, QRect(x+10, y, w, h))
        animation1.setKeyValueAt(0.65, QRect(x-10, y, w, h))
        animation1.setKeyValueAt(0.80, QRect(x+10, y, w, h))
        animation1.setKeyValueAt(0.90, QRect(x-10, y, w, h))
        animation1.setKeyValueAt(0.95, QRect(x+10, y, w, h))
        animation1.setKeyValueAt(1, QRect(x, y, w, h))
        animation1.setDuration(300)  # 设置间隔
        animation1.setLoopCount(2)  # 重复3次
        animation1.start(QAbstractAnimation.DeleteWhenStopped)       # 动画完毕后删除动画

        # 这是docx展示的功能：右侧大框里显示内容的功能
    def Docxviewer(self, filepath):
        try:
            file = docx.Document(filepath)
            self.plainviewer.clear()    # 清空文本
            for p in file.paragraphs:
                print(p.text)
                self.plainviewer.appendPlainText(p.text)  # 显示doc内容
        except:
            print('这是个非docx文件')

    # 搜索 列举目标文件。
    def serch_inDir(self):
        # ------------------设置全文件的列表模式------------------------------------
        self.filelistsview_model = QStandardItemModel(self)
        FileListview = self.filelistsview_model.invisibleRootItem()
        self.dir_treeView.setModel(self.filelistsview_model)
        self.AllFile_temp = self.search_inFilelist(self.search_lineedit.text())

        print('测试All列表内容，', self.AllFile_temp)

        for got in range(len(self.AllFile_temp)):
            gosData = QStandardItem(self.AllFile_temp[got])
            FileListview.setChild(got, gosData)


    def search_inFilelist(self, searchname):
        file_list = []
        oswalk_list = []
        #   定义进度条进度参数
        current = 0
        try:
            total = len(self.oswalk_list)
            for top, dirs, nondirs in self.oswalk_list:
                for item in nondirs:
                    if searchname in item:
                        # file_list.append(item)
                        file_list.append(os.path.join(top, item))
                current += 1
                self.progressBar_signal.emit(current, total)
            return file_list
        except:
            QMessageBox.warning(self, '提示', '正在加载中，请稍后！')
            print('正在递归')
            # time.sleep(1)
            return self.search_inFilelist(searchname)

    # -------------------------------------自定义进度条功能---------------------------------
    def pBar_view(self, a, total):
        self.progressBar.show()
        self.progressBar.setMaximum(total)
        self.progressBar.setValue(a)
        if a == total:
            self.progressBar.hide()
            self.progressBar.reset()

    def receivesignal_oswalkFunc(self, oswalk):     # 接受QThread信号
        self.oswalk_list = oswalk
        self.contextsearch_button.setEnabled(True)  # 设置内容搜索按钮可用


        print('QTHread正在运行中，尝试返回:')


#   ---------------------------------------------   线程   ————————————————————————————————————————————
#   ---------------------------------------------   线程   ————————————————————————————————————————————

class Oswalk_thread(QThread):

    oswalkFinished_signal = pyqtSignal(list)     # 创建一个信号

    def __init__(self, root):   # 传参只能在init里，不能在run（）里穿参数，切记。
        super().__init__()

        self.root = root

    def run(self):
        self.result = list(os.walk(self.root))  # 遍历指定目录下文件结构，并转化成list

        self.oswalkFinished_signal.emit(self.result)     # 发射oswalk的list数据





















