from PyQt6 import QtWidgets, QtGui
from venAux import *
from email.feedparser import headerRE
import os
import sys
import var
import eventos
import re
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

class Eventos(QtWidgets.QMainWindow):
    staticmethod
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

    def abrirAbout(self):
        var.dlgAbout.show()

    def cerrarAbout(self):
        var.dlgAbout.hide()