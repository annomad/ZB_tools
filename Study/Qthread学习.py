from PyQt5.Qt import *
import sys,random

class mainui(QWidget):
    btn_Signal = pyqtSignal(dict)
    def __init__(self):
        super(mainui, self).__init__()
        self.setupUi()
    def setupUi(self):
        test_dict = {i: random.randint(10, 100) for i in range(1, 5)}
        #print(test_dict)
        self.Btn = QPushButton('点我发射信号', self)
        self.Btn.clicked.connect(lambda : self.btn_Signal.emit(test_dict))

if __name__ == '__main__':
    def btn_Signal(dict_):
        print(dict_)
    app = QApplication(sys.argv)
    mainui = mainui()
    mainui.show()
    mainui.btn_Signal.connect(btn_Signal)
    sys.exit(app.exec_())

