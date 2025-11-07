from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_dlgCalendar(object):
    def setupUi(self, dlgCalendar):
        dlgCalendar.setObjectName("dlgCalendar")
        dlgCalendar.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        dlgCalendar.resize(312, 185)
        dlgCalendar.setMinimumSize(QtCore.QSize(312, 185))
        dlgCalendar.setMaximumSize(QtCore.QSize(312, 185))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\\\templates\\../img/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlgCalendar.setWindowIcon(icon)
        dlgCalendar.setModal(True)
        self.Calendar = QtWidgets.QCalendarWidget(parent=dlgCalendar)
        self.Calendar.setGeometry(QtCore.QRect(0, 0, 312, 183))
        self.Calendar.setMinimumSize(QtCore.QSize(312, 183))
        self.Calendar.setMaximumSize(QtCore.QSize(312, 183))
        self.Calendar.setGridVisible(True)
        self.Calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.Calendar.setObjectName("Calendar")

        self.retranslateUi(dlgCalendar)
        QtCore.QMetaObject.connectSlotsByName(dlgCalendar)

    def retranslateUi(self, dlgCalendar):
        _translate = QtCore.QCoreApplication.translate
        dlgCalendar.setWindowTitle(_translate("dlgCalendar", "Seleccione Fecha"))