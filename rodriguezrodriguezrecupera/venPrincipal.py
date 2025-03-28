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
        self.horizontalSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 1)
        self.horizontalSpacer2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer2, 4, 3, 1, 1)
        self.panPrincipal = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.panPrincipal.setGeometry(QtCore.QRect(55, 9, 1072, 690))
        self.panPrincipal.setObjectName("panPrincipal")
        
        # Tabla Contactos
        self.pesContactos = QtWidgets.QWidget()
        self.pesContactos.setObjectName("pesContactos")
        self.gridLayout = QtWidgets.QGridLayout(self.pesContactos)
        self.gridLayout.setObjectName("gridLayout")
        
        # Labels and Text Edits
        self.lblid = QtWidgets.QLabel(self.pesContactos)
        self.lblid.setText("Id:")
        self.gridLayout.addWidget(self.lblid, 0, 0)
        self.txtid = QtWidgets.QLineEdit(self.pesContactos)
        self.gridLayout.addWidget(self.txtid, 0, 1)
        self.lblnombre = QtWidgets.QLabel(self.pesContactos)
        self.lblnombre.setText("Nombre:")
        self.gridLayout.addWidget(self.lblnombre, 1, 0)
        self.txtnombre = QtWidgets.QLineEdit(self.pesContactos)
        self.gridLayout.addWidget(self.txtnombre, 1, 1)
        self.lblemail = QtWidgets.QLabel(self.pesContactos)
        self.lblemail.setText("Email:")
        self.gridLayout.addWidget(self.lblemail, 2, 0)
        self.txtemail = QtWidgets.QLineEdit(self.pesContactos)
        self.gridLayout.addWidget(self.txtemail, 2, 1)
        self.lblmovil = QtWidgets.QLabel(self.pesContactos)
        self.lblmovil.setText("Móvil:")
        self.gridLayout.addWidget(self.lblmovil, 3, 0)
        self.txtmovil = QtWidgets.QLineEdit(self.pesContactos)
        self.gridLayout.addWidget(self.txtmovil, 3, 1)
        self.lblciudad = QtWidgets.QLabel(self.pesContactos)
        self.lblciudad.setText("Ciudad:")
        self.gridLayout.addWidget(self.lblciudad, 0, 2)
        self.txtciudad = QtWidgets.QLineEdit(self.pesContactos)
        self.gridLayout.addWidget(self.txtciudad, 0, 3)
        self.lblnotas = QtWidgets.QLabel(self.pesContactos)
        self.lblnotas.setText("Notas:")
        self.gridLayout.addWidget(self.lblnotas, 1, 2)
        self.txtnotas = QtWidgets.QPlainTextEdit(self.pesContactos)
        self.gridLayout.addWidget(self.txtnotas, 1, 3, 2, 1)
        self.lblfechaalta = QtWidgets.QLabel(self.pesContactos)
        self.lblfechaalta.setText("Fecha alta:")
        self.gridLayout.addWidget(self.lblfechaalta, 3, 2)
        self.txtfechaalta = QtWidgets.QLineEdit(self.pesContactos)
        self.gridLayout.addWidget(self.txtfechaalta, 3, 3)
        
        # Botones
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.botonalta = QtWidgets.QPushButton(self.pesContactos)
        self.botonalta.setText("ALTA")
        self.horizontalLayout.addWidget(self.botonalta)
        self.botonmodificar = QtWidgets.QPushButton(self.pesContactos)
        self.botonmodificar.setText("MODIFICAR")
        self.horizontalLayout.addWidget(self.botonmodificar)
        self.botoneliminar = QtWidgets.QPushButton(self.pesContactos)
        self.botoneliminar.setText("ELIMINAR")
        self.horizontalLayout.addWidget(self.botoneliminar)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 4)
        # Table
        self.tablaContactos = QtWidgets.QTableWidget(self.pesContactos)
        self.tablaContactos.setColumnCount(5)
        self.tablaContactos.setHorizontalHeaderLabels(["Id", "Nombre", "Email", "Móvil", "Ciudad"])
        self.gridLayout.addWidget(self.tablaContactos, 5, 0, 1, 4)
        self.panPrincipal.addTab(self.pesContactos, "Contactos")
