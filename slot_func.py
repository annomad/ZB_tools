
from MainWindow import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
import os
import docx
import logging




"""这是一个槽函数集中营，继承了QT designer设计的ui，加入诸多的槽函数"""
"""这是功能函数集中营"""


class Slotfunc(MainWindow):  # 继承主窗口的类

    progressBar_signal = pyqtSignal(int, int)  # 定义一个进度条的信号。

    def __init__(self):
        super().__init__()


        # 初始化变量
        self.dir_path = ''  # 初始化资料库目录变量
        self.filesystem_model = QFileSystemModel(self)  # 实例化一个QfilesystemModel
        self.standartitem_model = QStandardItemModel()     # 定义一个直接显示文件的model
        self.oswalkThread = Oswalk_thread(self.dir_path)      # 定义一个线程
        self.contextsearch_button.setEnabled(False)  # 内容搜索按钮暂时失效。

        self.search_lineedit.returnPressed.connect(self.search_func)  # 回车信号，链接搜索函数
        # self.search_lineedit.textChanged.connect(self.searchbutton_func)  # 内容改变信号，链接搜索函数
        self.search_lineedit.editingFinished.connect(self.research_func)  # 结束编辑，重新展示函数
        self.searchbutton.clicked.connect(self.search_func)  # 绑定搜索按键功能
        self.contextsearch_button.clicked.connect(self.withNoDir_search_func)  # 文件列表展示功能
        self.dir_treeView.doubleClicked.connect(self.opendocs_func)  # 你编写打开doc文档功能
        self.progressBar_signal.connect(self.pBar_view)  # 进度条信号绑定槽函数
        self.model_status = 'QF'    # 设置model标签

    # ##################################        函数区    ###############################
    # ##################################        函数区    ###############################
    # ##################################        函数区    ###############################

    # 自动绑定信号和槽函数，点击"打开资料库"打开目录选择窗口

    @pyqtSlot()
    def on_openResource_clicked(self):  # 打开资源库按钮
        # fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./","All Files (*);;Excel Files (*.xls)")
        # 设置文件扩展名过滤,注意用双分号间隔
        dir_path_temp = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 打开目录
        #  判断下打开文件被取消了
        if dir_path_temp:
            self.dir_path = dir_path_temp

            # 载入文件结构model
            self.loadfilesystem_func()

            # 实例化一个线程oswalk的线程
            self.oswalkThread = Oswalk_thread(self.dir_path)  # 创建一个多线程的实例.
            self.oswalkThread.oswalkFinished_signal.connect(self.receivesignal_oswalkFunc)  # THread现场信号连接函数
            self.oswalkThread.start()
            logging.debug('准备启动多线程')
            self.contextsearch_button.setEnabled(False)  # 内容搜索暂时失效。
            self.contextsearch_button.setText('扫描中')
    def loadfilesystem_func(self):       # 加载文件目录结构的model功能
        if self.dir_path != '':
            self.dispay_dir_path.setText(self.dir_path)  # 路径显示label控件显示路径的名称
            self.dispay_dir_path.setToolTip(self.dir_path)  # 提示路径绝对路径，（宽度会影响label显示，另加一个提示）
            # # 进行筛选只显示文件夹，不显示文件和特色文件
            self.filesystem_model.setFilter(QDir.Files | QDir.NoDotAndDotDot | QDir.AllDirs)
            # QDir.Files|QDir.NoDotAndDotDot|QDir.AllDirs
            # 进行 treeview 相关操作根目录、加载model，匹配索引
            self.filesystem_model.setRootPath(self.dir_path)  # 设置根目录
            self.dir_treeView.setModel(self.filesystem_model)  # 把设置好的目录model传递给treeview
            self.dir_treeView.setRootIndex(self.filesystem_model.index(self.dir_path))  # 把目录索引传递给treeview索引，必须有！
            for i in [1, 2, 3]:
                self.dir_treeView.setColumnHidden(i, True)

    # @pyqtSlot()
    def search_func(self):  # 搜索按钮功能键
        self.model_status = 'QF'  # 设置model标签
        self.loadfilesystem_func()       # 加载文件目录model

        self.Alert_animation(self.search_lineedit)  # 装在一个动画警示？
        self.search_lineedit.setToolTip('拟增加正则re表达式查询功能')
        self.search_lineedit.setStyleSheet('border: none; background: none')  # 设置背景色
        self.filesystem_model.setNameFilterDisables(False)  # 如果是Ture，则显示灰色的非目标，False直接隐藏
        if self.search_lineedit.text():
            try:
                if self.dir_path != '':
                    print('你搜索框输入的是：' + self.search_lineedit.text())
                    self.search_lineedit.selectAll()  # 全选文本内容，方便下一次输入
                    self.search_lineedit.setFocus()
                    self.filesystem_model.setNameFilters(['*' + self.search_lineedit.text() + '*'])  # 搜索功能核心，设置名字过滤器
                else:
                    print('警告：请输入制定的资料库文件')
                    a = QMessageBox.warning(self, '提示', '您还尚未打开任何资料库！\n\n现在是否选择一个资料库打开？',
                                            QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)

                    if a == QMessageBox.Yes:
                        self.on_openResource_clicked()
                        self.search_func()
                        self.search_lineedit.setStyleSheet('border: none; background: cyan')
                        self.Alert_animation(self.search_lineedit)
                    else:
                        print('取消打开文件')
            except AttributeError:
                logging.debug('这是打开一个错误的文件路径')

    def opendocs_func(self, qmodel_index):  # 定义treeview列表单元双击功能

        # 看看是否处于Qfilesystemmodel状态中
        if self.model_status == 'QF':
            try:
                filepath = self.filesystem_model.filePath(qmodel_index)
            except:
                logging.debug('这个无法返回文本路径')
            finally:
                logging.debug('有效的鼠标点击')
                if os.path.isfile(filepath):  # 如果不是目录，则告知这是一个文件
                    print('这是一个文件')
                    self.Docxviewer(filepath)
                else:
                    print('这里看看能否做点文章')
        elif self.model_status == "QS":
            a = self.standartitem_model.itemData(qmodel_index)
            self.Docxviewer(a[3])



    def research_func(self):  # 非空重搜索
        if self.search_lineedit.text() == '':
            self.search_lineedit.setStyleSheet('border: none; background: none')  # 设置背景色
            self.filesystem_model.setNameFilters([])



        # 这是docx展示的功能：右侧大框里显示内容的功能
    def Docxviewer(self, filepath):
        try:
            file = docx.Document(filepath)
            self.plainviewer.clear()    # 清空文本
            for p in file.paragraphs:
                # print(p.text)
                self.plainviewer.appendPlainText(p.text)  # 显示doc内容
        except:
            logging.debug('Docview_func :这是个非docx文件')

    # 搜索 列举目标文件。
    def withNoDir_search_func(self):
        # ------------------设置全文件的列表模式------------------------------------
        self.model_status = 'QS'        # 设置model标签
        self.standartitem_model = QStandardItemModel(self)
        FileListview = self.standartitem_model.invisibleRootItem()
        self.dir_treeView.setModel(self.standartitem_model)
        self.AllFile_wantted = self.search_inFilelist(self.search_lineedit.text())

        # print('测试All列表内容，', AllFile_temp)
        Allfile_list = list(self.AllFile_wantted.keys())

        for got in range(len(Allfile_list)):
            gosData = QStandardItem(Allfile_list[got])      # 创建Qstandarditem元素
            gosData.setToolTip(str(self.AllFile_wantted[(Allfile_list[got])]))      # 设置tooltips
            FileListview.setChild(got, gosData)         #加入创建子集

    # 在文件列表中搜索目标文件
    def search_inFilelist(self, searchname):
        file_list = []
        oswalk_list = []
        file_dict = {}
        #   定义进度条进度参数
        current = 0
        try:
            total = len(self.oswalk_list)
            for top, dirs, nondirs in self.oswalk_list:
                for item in nondirs:
                    if searchname in item:
                        file_dict[item] = os.path.join(top, item)       # 增加字典
                        #  file_name.append(item)
                        # file_list.append(os.path.join(top, item))
                current += 1
                self.progressBar_signal.emit(current, total)
            # return file_list
            return file_dict
        except:
            QMessageBox.warning(self, '提示', '正在加载中，请稍后！')
            logging.debug('正在递归')
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
        self.contextsearch_button.setText('内容')  # 设置内容搜索按钮可用
        print('QTHread结果已经通过信号接受，并赋值了:')


#   ---------------------------------------------   线程   ————————————————————————————————————————————
#   ---------------------------------------------   线程   ————————————————————————————————————————————

class Oswalk_thread(QThread):

    oswalkFinished_signal = pyqtSignal(list)     # 创建一个信号

    def __init__(self, root):   # 传参只能在init里，不能在run（）里穿参数，切记。
        super().__init__()
        self.root = root

    def run(self):
        logging.debug('oswalk线程开始工作')
        result = list(os.walk(self.root))  # 遍历指定目录下文件结构，并转化成list

        self.oswalkFinished_signal.emit(result)     # 发射oswalk的list数据
        logging.debug('多线程运行完毕')





















