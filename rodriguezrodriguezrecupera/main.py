from PyQt6 import QtWidgets, QtGui, QtCore
from venPrincipal import *
import sys
import var

class Main(QtWidgets.QMainWindow):
    def __init__(self):
       super(Main,self).__init__()
       var.ui = Ui_venprincipal()
       var.ui.setupUi(self)
             
       
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())
