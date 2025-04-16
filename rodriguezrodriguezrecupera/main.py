from PyQt6 import QtWidgets, QtGui, QtCore
from venPrincipal import *
from venAux import *
import sys
import var
import conexion
import eventos
import styles
import locale
import contactos

class Main(QtWidgets.QMainWindow):
    def __init__(self):
       super(Main,self).__init__()
       var.ui = Ui_venprincipal()
       var.ui.setupUi(self)
       self.setStyleSheet(styles.load_stylesheet())
       conexion.Conexion.db_conexion(self)
       var.dlgAbrir = FileDialogAbrir()
       var.dlgAbout = dlgAbout()
       
       '''
       evento de ventana principal
       '''
       var.ui.actionSalir.triggered.connect(eventos.Eventos.cerrarVentana)
       
       '''
       eventos del menubar y toolbar
       '''
       var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)
       var.ui.actionAcercaDe.triggered.connect(eventos.Eventos.abrirAbout)
       
       '''
       eventos de cajas de texto
       '''
       var.ui.txtemail.textChanged.connect(lambda: contactos.Contactos.checkEmail(var.ui.txtemail.text()))
       var.ui.txtmovil.textChanged.connect(lambda: contactos.Contactos.checkMovil(var.ui.txtmovil.text()))
    
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())
