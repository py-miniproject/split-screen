import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class selectWinProgram(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        # 화면 타이틀 작성: 윈도우 프로그램 지정
        # self.setWindowTitle('윈도우 프로그램 지정')
        
        # 화면 크기 지정 640 x 480
        self.resize(640, 480)

        # 상단 타이틀바 없애기
        self.setWindowFlag(Qt.FramelessWindowHint)

        # 우상단 화면 종료버튼
        btn = QPushButton('X', self)
        btn.move(600,0)
        btn.resize(40,40)
        btn.clicked.connect(QCoreApplication.instance().quit)

        # 콤보박스
        combo1 = QComboBox(self)
        combo2 = QComboBox(self)
        combo3 = QComboBox(self)
        combo4 = QComboBox(self)
        
        

        # self.center()
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = selectWinProgram()
   sys.exit(app.exec_())