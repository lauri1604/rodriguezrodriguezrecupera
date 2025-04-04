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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1182, 749)
        MainWindow.setMaximumSize(QSize(16777215, 16777194))
        icon = QIcon()
        icon.addFile(u"img/logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionCrear_Backup = QAction(MainWindow)
        self.actionCrear_Backup.setObjectName(u"actionCrear_Backup")
        self.actionRestaurar_Backup = QAction(MainWindow)
        self.actionRestaurar_Backup.setObjectName(u"actionRestaurar_Backup")
        self.actionExportar_Datos = QAction(MainWindow)
        self.actionExportar_Datos.setObjectName(u"actionExportar_Datos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.panPrincipal = QTabWidget(self.centralwidget)
        self.panPrincipal.setObjectName(u"panPrincipal")
        self.panPrincipal.setGeometry(QRect(80, 20, 1001, 681))
        self.pesContactos = QWidget()
        self.pesContactos.setObjectName(u"pesContactos")
        self.layoutWidget = QWidget(self.pesContactos)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(21, 10, 821, 146))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lblfechaalta = QLabel(self.layoutWidget)
        self.lblfechaalta.setObjectName(u"lblfechaalta")
        self.lblfechaalta.setMinimumSize(QSize(50, 0))
        self.lblfechaalta.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.lblfechaalta, 2, 2, 1, 1)

        self.txtciudad = QTextEdit(self.layoutWidget)
        self.txtciudad.setObjectName(u"txtciudad")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtciudad.sizePolicy().hasHeightForWidth())
        self.txtciudad.setSizePolicy(sizePolicy)
        self.txtciudad.setMinimumSize(QSize(131, 20))
        self.txtciudad.setMaximumSize(QSize(230, 20))

        self.gridLayout.addWidget(self.txtciudad, 0, 3, 1, 1)

        self.lbllnotas = QLabel(self.layoutWidget)
        self.lbllnotas.setObjectName(u"lbllnotas")
        self.lbllnotas.setMinimumSize(QSize(50, 25))
        self.lbllnotas.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.lbllnotas, 1, 2, 1, 1)

        self.txtnombre = QPlainTextEdit(self.layoutWidget)
        self.txtnombre.setObjectName(u"txtnombre")
        sizePolicy.setHeightForWidth(self.txtnombre.sizePolicy().hasHeightForWidth())
        self.txtnombre.setSizePolicy(sizePolicy)
        self.txtnombre.setMinimumSize(QSize(400, 25))
        self.txtnombre.setMaximumSize(QSize(400, 20))

        self.gridLayout.addWidget(self.txtnombre, 1, 1, 1, 1)

        self.lblmovil = QLabel(self.layoutWidget)
        self.lblmovil.setObjectName(u"lblmovil")
        self.lblmovil.setMinimumSize(QSize(50, 25))
        self.lblmovil.setMaximumSize(QSize(60, 25))

        self.gridLayout.addWidget(self.lblmovil, 3, 0, 1, 1)

        self.txtmovil = QTextEdit(self.layoutWidget)
        self.txtmovil.setObjectName(u"txtmovil")
        sizePolicy.setHeightForWidth(self.txtmovil.sizePolicy().hasHeightForWidth())
        self.txtmovil.setSizePolicy(sizePolicy)
        self.txtmovil.setMinimumSize(QSize(140, 24))
        self.txtmovil.setMaximumSize(QSize(140, 24))

        self.gridLayout.addWidget(self.txtmovil, 3, 1, 1, 1)

        self.txtfechaalta = QTextEdit(self.layoutWidget)
        self.txtfechaalta.setObjectName(u"txtfechaalta")
        self.txtfechaalta.setMinimumSize(QSize(80, 0))
        self.txtfechaalta.setMaximumSize(QSize(80, 20))

        self.gridLayout.addWidget(self.txtfechaalta, 2, 3, 1, 1)

        self.txtnotas = QTextEdit(self.layoutWidget)
        self.txtnotas.setObjectName(u"txtnotas")
        self.txtnotas.setMinimumSize(QSize(151, 25))
        self.txtnotas.setMaximumSize(QSize(200, 25))

        self.gridLayout.addWidget(self.txtnotas, 1, 3, 1, 1)

        self.txtemail = QPlainTextEdit(self.layoutWidget)
        self.txtemail.setObjectName(u"txtemail")
        sizePolicy.setHeightForWidth(self.txtemail.sizePolicy().hasHeightForWidth())
        self.txtemail.setSizePolicy(sizePolicy)
        self.txtemail.setMinimumSize(QSize(240, 20))
        self.txtemail.setMaximumSize(QSize(200, 20))

        self.gridLayout.addWidget(self.txtemail, 2, 1, 1, 1)

        self.txtid = QTextEdit(self.layoutWidget)
        self.txtid.setObjectName(u"txtid")
        sizePolicy.setHeightForWidth(self.txtid.sizePolicy().hasHeightForWidth())
        self.txtid.setSizePolicy(sizePolicy)
        self.txtid.setMaximumSize(QSize(80, 25))
        self.txtid.setStyleSheet(u"")

        self.gridLayout.addWidget(self.txtid, 0, 1, 1, 1)

        self.lblnombre = QLabel(self.layoutWidget)
        self.lblnombre.setObjectName(u"lblnombre")
        self.lblnombre.setMinimumSize(QSize(50, 25))
        self.lblnombre.setMaximumSize(QSize(60, 25))

        self.gridLayout.addWidget(self.lblnombre, 1, 0, 1, 1)

        self.lblemail = QLabel(self.layoutWidget)
        self.lblemail.setObjectName(u"lblemail")
        self.lblemail.setMinimumSize(QSize(47, 20))
        self.lblemail.setMaximumSize(QSize(48, 20))

        self.gridLayout.addWidget(self.lblemail, 2, 0, 1, 1)

        self.lblid = QLabel(self.layoutWidget)
        self.lblid.setObjectName(u"lblid")
        self.lblid.setMinimumSize(QSize(50, 25))
        self.lblid.setMaximumSize(QSize(30, 20))

        self.gridLayout.addWidget(self.lblid, 0, 0, 1, 1)

        self.lblciudad = QLabel(self.layoutWidget)
        self.lblciudad.setObjectName(u"lblciudad")
        self.lblciudad.setMinimumSize(QSize(50, 25))
        self.lblciudad.setMaximumSize(QSize(60, 25))

        self.gridLayout.addWidget(self.lblciudad, 0, 2, 1, 1)

        self.layoutWidget1 = QWidget(self.pesContactos)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 150, 821, 331))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.botonalta_2 = QPushButton(self.layoutWidget1)
        self.botonalta_2.setObjectName(u"botonalta_2")

        self.horizontalLayout_2.addWidget(self.botonalta_2)

        self.botonmodificar_2 = QPushButton(self.layoutWidget1)
        self.botonmodificar_2.setObjectName(u"botonmodificar_2")

        self.horizontalLayout_2.addWidget(self.botonmodificar_2)

        self.botoneliminar_2 = QPushButton(self.layoutWidget1)
        self.botoneliminar_2.setObjectName(u"botoneliminar_2")

        self.horizontalLayout_2.addWidget(self.botoneliminar_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 4, 1, 1)

        self.tableWidget = QTableWidget(self.layoutWidget1)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_2.addWidget(self.tableWidget, 3, 0, 1, 5)

        self.panPrincipal.addTab(self.pesContactos, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.panPrincipal.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1182, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuGesti_n = QMenu(self.menubar)
        self.menuGesti_n.setObjectName(u"menuGesti_n")
        self.menuHerramientas = QMenu(self.menubar)
        self.menuHerramientas.setObjectName(u"menuHerramientas")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuGesti_n.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHerramientas.addAction(self.actionCrear_Backup)
        self.menuHerramientas.addAction(self.actionRestaurar_Backup)
        self.menuHerramientas.addSeparator()
        self.menuHerramientas.addAction(self.actionExportar_Datos)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Agenda telef\u00f3bica", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionCrear_Backup.setText(QCoreApplication.translate("MainWindow", u"Crear Backup", None))
        self.actionRestaurar_Backup.setText(QCoreApplication.translate("MainWindow", u"Restaurar Backup", None))
        self.actionExportar_Datos.setText(QCoreApplication.translate("MainWindow", u"Exportar Datos", None))
        self.lblfechaalta.setText(QCoreApplication.translate("MainWindow", u"Fecha alta:", None))
        self.lbllnotas.setText(QCoreApplication.translate("MainWindow", u"Notas:", None))
#if QT_CONFIG(tooltip)
        self.txtnombre.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lblmovil.setText(QCoreApplication.translate("MainWindow", u"M\u00f3vil:", None))
#if QT_CONFIG(whatsthis)
        self.txtmovil.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.txtfechaalta.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.txtemail.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.txtid.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lblnombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.lblemail.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.lblid.setText(QCoreApplication.translate("MainWindow", u"id:", None))
        self.lblciudad.setText(QCoreApplication.translate("MainWindow", u"Ciudad:", None))
        self.botonalta_2.setText(QCoreApplication.translate("MainWindow", u"ALTA", None))
        self.botonmodificar_2.setText(QCoreApplication.translate("MainWindow", u"MODIFICAR", None))
        self.botoneliminar_2.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Movil", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ciudad", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Notas", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Fecha Alta", None));
        self.panPrincipal.setTabText(self.panPrincipal.indexOf(self.pesContactos), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.panPrincipal.setTabText(self.panPrincipal.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuGesti_n.setTitle(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n", None))
        self.menuHerramientas.setTitle(QCoreApplication.translate("MainWindow", u"Herramientas", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

