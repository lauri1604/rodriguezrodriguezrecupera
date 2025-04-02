from PyQt6 import QtWidgets, QtGui, QtCore

class Ui_venprincipal(object):
    def setupUi(self,venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.resize(1537, 903)
        venPrincipal.setMinimumSize(110, 25)
        venPrincipal.setMaximumSize(QtCore.QSize(16777215, 16777215))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(venPrincipal.sizePolicy().hasHeightForWidth())
        venPrincipal.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\\\templates\\../img/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        venPrincipal.setWindowIcon(icon)
        # Panel Principal
        self.centralwidget = QtWidgets.QWidget(venPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        venPrincipal.setCentralWidget(self.centralwidget)
        
        # Layout vertical principal
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(50, 20, 50, 20)
        self.verticalLayout.setSpacing(10)

        # Panel con pestañas
        self.panPrincipal = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.panPrincipal.setObjectName("panPrincipal")
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        self.panPrincipal.setFont(font)

        # Pestaña Contactos
        self.pesContactos = QtWidgets.QWidget()
        self.pesContactos.setObjectName("pesContactos")
        
        # Grid Layout para la pestaña Contactos
        self.gridLayout = QtWidgets.QGridLayout(self.pesContactos)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(25, 50, 25, 50)  # Reducir márgenes laterales
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        
        # ID
        self.lblid = QtWidgets.QLabel(parent=self.pesContactos)
        self.lblid.setObjectName("lblid")
        self.lblid.setText("ID")
        self.lblid.setMinimumSize(QtCore.QSize(20, 0))
        self.lblid.setMaximumSize(QtCore.QSize(30, 25))
        self.lblid.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        
        self.txtid = QtWidgets.QLineEdit(parent=self.pesContactos)
        self.txtid.setObjectName("txtid")
        self.txtid.setMinimumSize(QtCore.QSize(50, 0))
        self.txtid.setMaximumSize(QtCore.QSize(60, 25))
        self.txtid.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

        # Nombre
        self.lblnombre = QtWidgets.QLabel(parent=self.pesContactos)
        self.lblnombre.setObjectName("lblnombre")
        self.lblnombre.setText("Nombre")
        self.lblnombre.setMinimumSize(QtCore.QSize(45, 0))
        self.lblnombre.setMaximumSize(QtCore.QSize(65, 25))
        self.lblnombre.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        
        self.txtnombre = QtWidgets.QLineEdit(parent=self.pesContactos)
        self.txtnombre.setObjectName("txtnombre")
        self.txtnombre.setMinimumSize(QtCore.QSize(200, 0))
        self.txtnombre.setMaximumSize(QtCore.QSize(250, 25))
        self.txtnombre.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

        # Notas
        self.lblnotas = QtWidgets.QLabel(parent=self.pesContactos)
        self.lblnotas.setObjectName("lblnotas")
        self.lblnotas.setText("Notas")
        self.lblnotas.setMinimumSize(QtCore.QSize(40, 0))
        self.lblnotas.setMaximumSize(QtCore.QSize(50, 25))
        self.txtnotas = QtWidgets.QLineEdit(parent=self.pesContactos)
        self.txtnotas.setObjectName("txtnotas")
        self.txtnotas.setMinimumSize(QtCore.QSize(140, 0))
        self.txtnotas.setMaximumSize(QtCore.QSize(240, 25))
        self.txtnotas.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

        # Email
        self.lblemail = QtWidgets.QLabel(parent=self.pesContactos)
        self.lblemail.setObjectName("lblemail")
        self.lblemail.setText("Email")
        self.lblemail.setMinimumSize(QtCore.QSize(45, 0))
        self.lblemail.setMaximumSize(QtCore.QSize(45, 25))
        self.lblemail.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.txtemail = QtWidgets.QLineEdit(parent=self.pesContactos)
        self.txtemail.setObjectName("txtemail")
        self.txtemail.setMinimumSize(QtCore.QSize(150, 0))
        self.txtemail.setMaximumSize(QtCore.QSize(240, 25))
        self.txtemail.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

        # Fecha Alta
        self.lblfechaalta = QtWidgets.QLabel(parent=self.pesContactos)
        self.lblfechaalta.setObjectName("lblfechaalta")
        self.lblfechaalta.setText("Fecha Alta")
        self.lblfechaalta.setMinimumSize(QtCore.QSize(55, 0))
        self.lblfechaalta.setMaximumSize(QtCore.QSize(70, 25))
        self.lblfechaalta.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.txtfechaalta = QtWidgets.QLineEdit(parent=self.pesContactos)
        self.txtfechaalta.setObjectName("txtfechaalta")
        self.txtfechaalta.setMinimumSize(QtCore.QSize(50, 0))
        self.txtfechaalta.setMaximumSize(QtCore.QSize(70, 25))
        self.txtfechaalta.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

        # Móvil
        self.lblmovil = QtWidgets.QLabel(parent=self.pesContactos)
        self.lblmovil.setObjectName("lblmovil")
        self.lblmovil.setText("Móvil")
        self.lblmovil.setMinimumSize(QtCore.QSize(40, 0))
        self.lblmovil.setMaximumSize(QtCore.QSize(50, 25))
        self.lblmovil.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.txtmovil = QtWidgets.QLineEdit(parent=self.pesContactos)
        self.txtmovil.setObjectName("txtmovil")
        self.txtmovil.setMinimumSize(QtCore.QSize(60, 0))
        self.txtmovil.setMaximumSize(QtCore.QSize(70, 25))
        self.txtmovil.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

        # Ciudad
        self.lblciudad = QtWidgets.QLabel(parent=self.pesContactos)
        self.lblciudad.setObjectName("lblciudad")
        self.lblciudad.setText("Ciudad")
        self.lblciudad.setMinimumSize(QtCore.QSize(50, 0))
        self.lblciudad.setMaximumSize(QtCore.QSize(60, 25))
        self.lblciudad.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.txtCiudad = QtWidgets.QLineEdit(parent=self.pesContactos)
        self.txtCiudad.setObjectName("txtCiudad")
        self.txtCiudad.setMinimumSize(QtCore.QSize(80, 0))
        self.txtCiudad.setMaximumSize(QtCore.QSize(110, 25))
        self.txtCiudad.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

        # Añadir widgets al gridLayout
        # Primera fila
        self.gridLayout.addWidget(self.lblid, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout.addWidget(self.txtid, 0, 2, 1, 1)

        # Segunda fila
        self.gridLayout.addWidget(self.lblnombre, 1, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout.addWidget(self.txtnombre, 1, 2, 1, 2)
        self.gridLayout.addWidget(self.lblnotas, 1, 4, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout.addWidget(self.txtnotas, 1, 5, 1, 2)

        # Tercera fila
        self.gridLayout.addWidget(self.lblemail, 2, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout.addWidget(self.txtemail, 2, 2, 1, 2)
        self.gridLayout.addWidget(self.lblfechaalta, 2, 4, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout.addWidget(self.txtfechaalta, 2, 5, 1, 1)

        # Cuarta fila
        self.gridLayout.addWidget(self.lblmovil, 3, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout.addWidget(self.txtmovil, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.lblciudad, 3, 4, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout.addWidget(self.txtCiudad, 3, 5, 1, 1)

        # Configurar columnas para mejor alineación
        self.gridLayout.setColumnMinimumWidth(1, 100)   # Labels izquierda
        self.gridLayout.setColumnMinimumWidth(2, 300)   # Campos texto izquierda
        self.gridLayout.setColumnMinimumWidth(3, 200)   # Aumentar espacio entre grupos
        self.gridLayout.setColumnMinimumWidth(4, 100)   # Labels derecha
        self.gridLayout.setColumnMinimumWidth(5, 300)   # Campos texto derecha

        # Ajustar stretch para que ocupe todo el ancho disponible
        self.gridLayout.setColumnStretch(0, 1)  # Stretch izquierda
        self.gridLayout.setColumnStretch(6, 1) # Stretch derecha

        # Layout horizontal para botones
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        
        # Crear botones
        self.btnAlta = QtWidgets.QPushButton(parent=self.pesContactos)
        self.btnAlta.setText("ALTA")
        self.btnAlta.setFixedSize(100, 30)
        
        self.btnModificar = QtWidgets.QPushButton(parent=self.pesContactos)
        self.btnModificar.setText("MODIFICAR")
        self.btnModificar.setFixedSize(100, 30)
        
        self.btnEliminar = QtWidgets.QPushButton(parent=self.pesContactos)
        self.btnEliminar.setText("ELIMINAR")
        self.btnEliminar.setFixedSize(100, 30)
        
        # Añadir botones al layout horizontal
        self.horizontalLayout.addStretch(1)
        self.horizontalLayout.addWidget(self.btnAlta)
        self.horizontalLayout.addWidget(self.btnModificar)
        self.horizontalLayout.addWidget(self.btnEliminar)
        self.horizontalLayout.addStretch(1)
        
         # Crear tabla
        self.tablaContactos = QtWidgets.QTableWidget(parent=self.pesContactos)
        self.tablaContactos.setMinimumSize(QtCore.QSize(700, 200))  # Reducir ancho de 830 a 700
        self.tablaContactos.setColumnCount(7)
        self.tablaContactos.setHorizontalHeaderLabels(["ID", "Nombre", "Email", "Móvil", "Ciudad", "Notas", "Fecha Alta"])
        
        # Añadir layout de botones y tabla al gridLayout
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 5)  # Reducir span de 7 a 5 columnas, empezar en 1
        self.gridLayout.addWidget(self.tablaContactos, 5, 1, 1, 5)
        
        # Ajustar espaciado vertical
        self.gridLayout.setRowMinimumHeight(4, 50)  # Aumentar espacio antes de botones
        self.gridLayout.setRowMinimumHeight(5, 20)  # Mantener espacio antes de tabla
              
        # Añadir pestaña y panel principal
        self.panPrincipal.addTab(self.pesContactos, "CONTACTOS")
        self.verticalLayout.addWidget(self.panPrincipal)