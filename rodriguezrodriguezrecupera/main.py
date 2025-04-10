from PyQt6 import QtWidgets, QtGui, QtCore
from venPrincipal import *
from venAux import *
import sys
import var
import styles

class Main(QtWidgets.QMainWindow):
    def __init__(self):
       super(Main,self).__init__()
       var.ui = Ui_venprincipal()
       var.ui.setupUi(self)
       self.setStyleSheet(styles.load_stylesheet())
       var.dlgAbrir = FileDialogAbrir()
       var.dlgAbout = dlgAbout()
       
       '''
       eventos del menubar y toolbar
       '''
       var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)
       var.ui.actionCrear_Backup.triggered.connect(eventos.Eventos.crearBackup)
       var.ui.actionRestaurar_Backup.triggered.connect(eventos.Eventos.restaurarBackup)
       
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())
