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
        super(Main, self).__init__()
        var.ui = Ui_venprincipal()
        var.ui.setupUi(self)
        self.setStyleSheet(styles.load_stylesheet())
        conexion.Conexion.db_conexion(self)
        var.dlgAbrir = FileDialogAbrir()
        var.dlgAbout = dlgAbout()
        var.longcontacto = 0
        
        contactos.Contactos.cargaTablaContactos(self)
        
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
        
        '''
        eventos de botones
        '''
        var.ui.botonalta.clicked.connect(contactos.Contactos.altaContacto)
        var.ui.botonmodificar.clicked.connect(contactos.Contactos.modificarContacto)
        var.ui.botoneliminar.clicked.connect(contactos.Contactos.eliminarContacto)
        '''
        eventos de tablas
        '''
        eventos.Eventos.resizeTablaContactos(self)
        
        var.ui.tablaContactos.clicked.connect(contactos.Contactos.cargaOneContacto)

    def closeEvent(self, event):
        mbox = QtWidgets.QMessageBox()
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
        mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
        mbox.setWindowTitle('Salir')
        mbox.setText('¿Desea Salir?')
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')
        if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())
