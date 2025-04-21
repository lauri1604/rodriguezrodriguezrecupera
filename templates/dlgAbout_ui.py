# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgAbout.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_dlgAbout(object):
    def setupUi(self, dlgAbout):
        if not dlgAbout.objectName():
            dlgAbout.setObjectName(u"dlgAbout")
        dlgAbout.resize(394, 302)
        dlgAbout.setModal(True)
        self.logo = QLabel(dlgAbout)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(120, 20, 131, 141))
        self.logo.setPixmap(QPixmap(u"../img/logo.ico"))
        self.autor = QLabel(dlgAbout)
        self.autor.setObjectName(u"autor")
        self.autor.setGeometry(QRect(70, 190, 221, 20))
        font = QFont()
        font.setBold(True)
        self.autor.setFont(font)
        self.copyright = QLabel(dlgAbout)
        self.copyright.setObjectName(u"copyright")
        self.copyright.setGeometry(QRect(60, 230, 81, 16))
        self.botonCerrarAbout = QPushButton(dlgAbout)
        self.botonCerrarAbout.setObjectName(u"botonCerrarAbout")
        self.botonCerrarAbout.setGeometry(QRect(260, 250, 75, 23))

        self.retranslateUi(dlgAbout)

        QMetaObject.connectSlotsByName(dlgAbout)
    # setupUi

    def retranslateUi(self, dlgAbout):
        dlgAbout.setWindowTitle(QCoreApplication.translate("dlgAbout", u"Acerca de...", None))
        self.logo.setText("")
        self.autor.setText(QCoreApplication.translate("dlgAbout", u"Autor: Laura M\u00aa Rodr\u00edguez Rodr\u00edguez", None))
        self.copyright.setText(QCoreApplication.translate("dlgAbout", u"Copyright 2025", None))
        self.botonCerrarAbout.setText(QCoreApplication.translate("dlgAbout", u"Cerrar", None))
    # retranslateUi

