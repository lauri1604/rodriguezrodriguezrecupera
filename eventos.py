from PyQt6 import QtWidgets, QtGui
from venAux import *
from email.feedparser import headerRE
from datetime import datetime
import os
import sys
import var
import eventos
import re
import locale
import time
import zipfile
import shutil
import conexion
import contactos
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

class Eventos(QtWidgets.QMainWindow):
    @staticmethod
    def mensajeSalir(self=None):
        mbox = QtWidgets.QMessageBox()
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
        mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
        mbox.setWindowTitle('Salir')
        mbox.setText('¿Desea Salir?')
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')
        mbox.resize(600, 800) #no funciona si no usa QDialgo QmessageBox lo tienen bloqueado
        if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            mbox.hide()
            
    def cerrarVentana(self = None):
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
            mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
            mbox.setWindowTitle('Salir')
            mbox.setText('¿Desea Salir?')
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')
            mbox.resize(600, 800) #no funciona si no usa QDialgo QmessageBox lo tienen bloqueado
            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                sys.exit()
            else:
                mbox.hide()
        except Exception as error:
             print("Error al cerrar ventana:", error)

    def abrirAbout(self):
        var.dlgAbout.show()

    def cerrarAbout(self):
        var.dlgAbout.hide()
    
    def validarMail(mail):
        mail = mail.lower()
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if re.match(regex, mail) or mail =="":
            return True
        else:
            return False
        
    def validarMovil(movil):
        regex =  r"^[67]\d{8}$"
        if re.match(regex, movil):
            return True
        else:
            return False
        
    def resizeTablaContactos(self):
        try:
            header = var.ui.tablaContactos.horizontalHeader()
            for i in range(header.count()):
                if (i == 1 or i == 2 or i == 4 or i == 5):
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                header_items = var.ui.tablaContactos.horizontalHeaderItem(i)
                font = header_items.font()
                font.setBold(True)
                header_items.setFont(font)
        except Exception as e:
            print("error en resize tabla contactos: ", e)
            
    def limpiarPanel(self):
        try:
            camposcontacto = [var.ui.txtnombre, var.ui.txtapellidos, var.ui.txtemail, var.ui.txtmovil, var.ui.txttelefono, var.ui.txtdireccion, var.ui.txtciudad, var.ui.txtprovincia, var.ui.txtpais, var.ui.txtnotas]
            for i, dato in enumerate (camposcontacto):
                if i == 4 or i == 5:
                    pass
                else:
                    dato.setText("")
                    contactos.Contactos.cargaTablaContactos(self)
        except Exception as e:
            print("Error al limpiar panel:", e)
            
    def abrirCalendar(boton):
        try:
            var.boton = boton
            var.uicalendar.show()
        except Exception as e:
            print("Error al abrir calendario:", e)