import sys
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import *
from PyQt5 import uic
# from PyQt5.QtWidgets import QListWidget, QHBoxLayout, QVBoxLayout


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("ThemaListUI.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QWidget, form_class) :
    def __init__(self) :
        super().__init__()
        # self.setupUi(self)
        self.initUI()
        self.setGeometry(803, 300, 257, 322)
    
        #리스트 위젯 이벤트
        # self.themlist.ItemClicked.connect(self.clickedItem)

        # self.addbtn.clikked.connect(self.add_list)


    def initUI(self):
        #콤보박스
        themcomb = QComboBox(self)
 
        # #리스트 위젯
        themlist = QListWidget(self)
        themlist.resize(251, 300)
        deftlst = ["테마1", "테마2", "테마3"]
        themlist.addItems(deftlst)
        

        # model = QStandardItemModel()
        # for t in theme:
        #     model.appendRow(QStandardItem(t))
        # themlist.setModel(model)

        

        
        #버튼
        addbtn = QPushButton('추가', self)
        addbtn.setCheckable(True)
        

        
        delbtn = QPushButton('삭제', self)
        delbtn.setCheckable(True)
        # self.delbtn.clikked.connect(self.del_list)
        

        optbtn = QPushButton('설정', self)
        optbtn.setCheckable(True)
        # self.optbtn.clikked.connect(self.option)
        
       

        #레이아웃
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(addbtn)
        hbox.addStretch(1)
        hbox.addWidget(delbtn)
        hbox.addStretch(3)
        hbox.addWidget(optbtn)

        vbox = QVBoxLayout()
        vbox.addWidget(themlist)
        vbox.addLayout(hbox)
        vbox.addWidget(themcomb)
        
        
        self.setLayout(vbox)
        # self.setLayout(hbox)
        self.show()
    
       

    #     self.addbtn.clicked.connect(self.addbtnFunction)
    #     self.dellbtn.clicked.connect(self.dellbtnFunction)
    #     self.optbtn.clicked.connect(self.optbtnFunction)
        

    # def addbtnFuntion(self):
    #     print("add")
    # def dellbtnFuntion(self):
    #     print("dell")
    # def optbtnFuntion(self):
    #     print("option")

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()