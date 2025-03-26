from PyQt6 import QtWidgets, QtGui, QtCore

class Ui_venprincipal(object):
    def setupUi(self,venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.resize(800,600)
        venPrincipal.setMinimumSize(1690,928)
        venPrincipal.setMaximumSize(QtCore.QSize(1024,768))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(venPrincipal.sizePolicy().hasHeightForWidth())
        venPrincipal.setSizePolicy(sizePolicy)
        venPrincipal.setMinimumSize(QtCore.QSize(110, 25))
        venPrincipal.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\\\templates\\../img/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        venPrincipal.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=venPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        