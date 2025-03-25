# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'venPrincipal.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_venPrincipal(object):
    def setupUi(self, venPrincipal):
        if not venPrincipal.objectName():
            venPrincipal.setObjectName(u"venPrincipal")
        venPrincipal.setEnabled(True)
        venPrincipal.setMinimumSize(QSize(1024, 768))
        self.centralwidget = QWidget(venPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1898, 903))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(70, 10, 2220, 691))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableWidget = QTableWidget(self.tab)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(100, 240, 701, 351))
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(260, 180, 245, 25))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.botonalta = QPushButton(self.widget)
        self.botonalta.setObjectName(u"botonalta")

        self.horizontalLayout.addWidget(self.botonalta)

        self.botonmodificar = QPushButton(self.widget)
        self.botonmodificar.setObjectName(u"botonmodificar")

        self.horizontalLayout.addWidget(self.botonmodificar)

        self.botoneliminar = QPushButton(self.widget)
        self.botoneliminar.setObjectName(u"botoneliminar")

        self.horizontalLayout.addWidget(self.botoneliminar)

        self.widget1 = QWidget(self.tab)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(60, 30, 551, 100))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lblid = QLabel(self.widget1)
        self.lblid.setObjectName(u"lblid")
        self.lblid.setMinimumSize(QSize(30, 20))
        self.lblid.setMaximumSize(QSize(30, 20))

        self.gridLayout.addWidget(self.lblid, 0, 0, 1, 1)

        self.txtid = QTextEdit(self.widget1)
        self.txtid.setObjectName(u"txtid")
        self.txtid.setMaximumSize(QSize(40, 20))

        self.gridLayout.addWidget(self.txtid, 0, 1, 1, 1)

        self.lblciudad = QLabel(self.widget1)
        self.lblciudad.setObjectName(u"lblciudad")
        self.lblciudad.setMinimumSize(QSize(47, 20))
        self.lblciudad.setMaximumSize(QSize(48, 20))

        self.gridLayout.addWidget(self.lblciudad, 0, 2, 1, 1)

        self.txtciudad = QTextEdit(self.widget1)
        self.txtciudad.setObjectName(u"txtciudad")
        self.txtciudad.setMinimumSize(QSize(131, 20))
        self.txtciudad.setMaximumSize(QSize(230, 20))

        self.gridLayout.addWidget(self.txtciudad, 0, 3, 1, 1)

        self.lblnombre = QLabel(self.widget1)
        self.lblnombre.setObjectName(u"lblnombre")
        self.lblnombre.setMinimumSize(QSize(46, 20))
        self.lblnombre.setMaximumSize(QSize(47, 20))

        self.gridLayout.addWidget(self.lblnombre, 1, 0, 1, 1)

        self.txtnombre = QTextEdit(self.widget1)
        self.txtnombre.setObjectName(u"txtnombre")
        self.txtnombre.setMinimumSize(QSize(170, 20))
        self.txtnombre.setMaximumSize(QSize(180, 20))

        self.gridLayout.addWidget(self.txtnombre, 1, 1, 1, 1)

        self.lbllnotas = QLabel(self.widget1)
        self.lbllnotas.setObjectName(u"lbllnotas")

        self.gridLayout.addWidget(self.lbllnotas, 1, 2, 1, 1)

        self.txtnotas = QTextEdit(self.widget1)
        self.txtnotas.setObjectName(u"txtnotas")
        self.txtnotas.setMinimumSize(QSize(151, 20))
        self.txtnotas.setMaximumSize(QSize(200, 20))

        self.gridLayout.addWidget(self.txtnotas, 1, 3, 1, 1)

        self.lblemail = QLabel(self.widget1)
        self.lblemail.setObjectName(u"lblemail")
        self.lblemail.setMinimumSize(QSize(47, 20))
        self.lblemail.setMaximumSize(QSize(48, 20))

        self.gridLayout.addWidget(self.lblemail, 2, 0, 1, 1)

        self.txtemail = QTextEdit(self.widget1)
        self.txtemail.setObjectName(u"txtemail")
        self.txtemail.setMinimumSize(QSize(191, 20))
        self.txtemail.setMaximumSize(QSize(200, 20))

        self.gridLayout.addWidget(self.txtemail, 2, 1, 1, 1)

        self.lblfechaalta = QLabel(self.widget1)
        self.lblfechaalta.setObjectName(u"lblfechaalta")

        self.gridLayout.addWidget(self.lblfechaalta, 2, 2, 1, 1)

        self.txtfechaalta = QTextEdit(self.widget1)
        self.txtfechaalta.setObjectName(u"txtfechaalta")
        self.txtfechaalta.setMinimumSize(QSize(111, 20))
        self.txtfechaalta.setMaximumSize(QSize(112, 20))

        self.gridLayout.addWidget(self.txtfechaalta, 2, 3, 1, 1)

        self.lblmovil = QLabel(self.widget1)
        self.lblmovil.setObjectName(u"lblmovil")
        self.lblmovil.setMinimumSize(QSize(47, 20))
        self.lblmovil.setMaximumSize(QSize(48, 20))

        self.gridLayout.addWidget(self.lblmovil, 3, 0, 1, 1)

        self.txtmovil = QTextEdit(self.widget1)
        self.txtmovil.setObjectName(u"txtmovil")
        self.txtmovil.setMinimumSize(QSize(121, 20))
        self.txtmovil.setMaximumSize(QSize(122, 20))

        self.gridLayout.addWidget(self.txtmovil, 3, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        venPrincipal.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(venPrincipal)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1266, 22))
        venPrincipal.setMenuBar(self.menuBar)

        self.retranslateUi(venPrincipal)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(venPrincipal)
    # setupUi

    def retranslateUi(self, venPrincipal):
        venPrincipal.setWindowTitle(QCoreApplication.translate("venPrincipal", u"MainWindow", None))
        self.botonalta.setText(QCoreApplication.translate("venPrincipal", u"ALTA", None))
        self.botonmodificar.setText(QCoreApplication.translate("venPrincipal", u"MODIFICAR", None))
        self.botoneliminar.setText(QCoreApplication.translate("venPrincipal", u"ELIMINAR", None))
        self.lblid.setText(QCoreApplication.translate("venPrincipal", u"id:", None))
        self.lblciudad.setText(QCoreApplication.translate("venPrincipal", u"Ciudad:", None))
        self.lblnombre.setText(QCoreApplication.translate("venPrincipal", u"Nombre:", None))
        self.lbllnotas.setText(QCoreApplication.translate("venPrincipal", u"Nottas:", None))
        self.lblemail.setText(QCoreApplication.translate("venPrincipal", u"Email:", None))
        self.lblfechaalta.setText(QCoreApplication.translate("venPrincipal", u"Fecha alta:", None))
        self.lblmovil.setText(QCoreApplication.translate("venPrincipal", u"M\u00f3vil:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("venPrincipal", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("venPrincipal", u"Tab 2", None))
    # retranslateUi

