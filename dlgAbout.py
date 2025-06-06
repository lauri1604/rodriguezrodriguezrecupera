from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_dlgAbout(object):
    def setupUi(self, dlgAbout):
        dlgAbout.setObjectName("dlgAbout")
        dlgAbout.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        dlgAbout.resize(400, 300)
        dlgAbout.setModal(True)
        self.logo = QtWidgets.QLabel(parent=dlgAbout)
        self.logo.setGeometry(QtCore.QRect(120, 20, 131, 141))
        self.logo.setOpenExternalLinks(True)
        self.logo.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.logo.setObjectName("logo")
        self.logo.setPixmap(QtGui.QPixmap("img/logo.ico"))
        self.autor = QtWidgets.QLabel(parent=dlgAbout)
        self.autor.setGeometry(QtCore.QRect(70, 190, 221, 20))
        font = QtGui.QFont()
        font.setBold(True)
        # font.setWeight(75)
        self.autor.setFont(font)
        self.autor.setOpenExternalLinks(True)
        self.autor.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.autor.setObjectName("autor")
        self.copyright = QtWidgets.QLabel(parent=dlgAbout)
        self.copyright.setGeometry(QtCore.QRect(60, 230, 81, 16))
        self.copyright.setOpenExternalLinks(True)
        self.copyright.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.copyright.setObjectName("copyright")
        self.botonCerrarAbout = QtWidgets.QPushButton(parent=dlgAbout)
        self.botonCerrarAbout.setGeometry(QtCore.QRect(260, 250, 75, 23))
        self.botonCerrarAbout.setObjectName("botonCerrarAbout")
        self.restranslateUi(dlgAbout)
        QtCore.QMetaObject.connectSlotsByName(dlgAbout)
        
    def restranslateUi(self, dlgAbout):
        _translate = QtCore.QCoreApplication.translate
        dlgAbout.setWindowTitle(_translate("dlgAbout", "Acerca de..."))
        self.autor.setText(_translate('dlgAbout', 'Autor: Laura Mª Rodríguez Rodríguez'))
        self.copyright.setText(_translate('dlgAbout', 'Copyright 2025'))
        self.botonCerrarAbout.setText(_translate("dlgAbout", "Cerrar"))