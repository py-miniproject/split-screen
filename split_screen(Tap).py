import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
 
 
form_class = uic.loadUiType('TapUI.ui')[0]
form_class_2 = uic.loadUiType('preveiwUI.ui')[0]
 
class MyWindow(QWidget, form_class, form_class_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.D2btn.clicked.connect(self.D2)
        # self.U2btn.clicked.connect(self.U2)
        # self.R2btn.clicked.connect(self.R2)
        # self.L2btn.clicked.connect(self.L2)
        # self.Q4btn.clicked.connect(self.Q4)
        # self.D3btn.clicked.connect(self.D3)
        # self.U3btn.clicked.connect(self.U3)
        # self.R3btn.clicked.connect(self.R3)
        # self.L3btn.clicked.connect(self.L3)
        self.D2btn.clicked.connect(self.btn_clicked)

    # def D2(self):
    #     pass

    # def D2(self):
    #     pass

    # def D2(self):
    #     pass

    # def D2(self):
    #     pass

    # def D2(self):
    #     pass

    # def D2(self):
    #     pass

    # def D2(self):
    #     pass

    # def D2(self):
    #     pass

    # def D2(self):
    #     pass
    def btn_clicked(self, screen):
        self.screen = screen
        if self.screen == 3:
            pass
        else:
            pass
# down2 = MyWindow()
# down2.btn_clicked(3)
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

