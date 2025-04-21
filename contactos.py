from PyQt6 import QtWidgets, QtGui, QtCore
from datetime import datetime
from sys import exception
import var
import eventos
import conexion

class Contactos:
    def __init__(self):
        self.valor = 0
        
    def checkEmail(mail):
        try:
           if eventos.Eventos.validarMail(mail):
                 var.ui.txtemail.setStyleSheet('background-color: rgb(255, 255, 255);')
           else:
                var.ui.txtemail.setStyleSheet('background-color: #FFC0CB; font-style: italic;')
                var.ui.txtemail.setPlaceholderText("correo no válido")
                var.ui.txtemail.setFocus()
        except Exception as error:
            print("error check mail", error)

    def checkMovil(movil):
        try:
           if eventos.Eventos.validarMovil(movil):
                var.ui.txtmovil.setStyleSheet('background-color: rgb(255, 255, 239);')
           else:
                var.ui.txtmovil.setStyleSheet('background-color: #FFC0CB; font-style: italic;')                
                var.ui.txtmovil.setPlaceholderText("móvil no válido")
                var.ui.txtmovil.setFocus()
        except Exception as error:
            print("error check movil", error)

    def altaContacto(self):
        try:
            op = 0
            nuevoContacto = [
                var.ui.txtnombre.text().title(), var.ui.txtemail.text(),
                var.ui.txtmovil.text(), var.ui.txtciudad.text(),
                var.ui.txtnotas.toPlainText()]
            if (nuevoContacto[0] != "" and nuevoContacto[1] != "" 
                and nuevoContacto[2] != "" and nuevoContacto[3] != "" 
                and nuevoContacto[4] != ""):
                op = 1
                if conexion.Conexion.altaContacto and op == 1:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setWindowIcon(QtGui.QIcon('img/logo.ico'))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText("Alta Contacto en Base de Datos")
                    mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()
                    Contactos.cargaTablaContactos(self)
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle("Aviso")
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                    mbox.setWindowIcon(QtGui.QIcon('img/logo.ico'))
                    mbox.setText('Error Faltan Datos o Contacto Existe')
                    mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Cancel).setText('Cancelar')
                    mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/logo.ico'))
                mbox.setText('Error Faltan Datos')
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Cancel).setText('Cancelar')
                mbox.exec()
        except Exception as error:
            print("error alta contacto", error)
    
    @staticmethod
    def cargaTablaContactos(self):
        try:
            pass
        except Exception as error:
            print("error carga tabla contactos", error)