from PyQt6 import QtWidgets, QtGui, QtCore

class Ui_venprincipal(object):
    def setupUi(self,venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.setWindowTitle("Agenda Telefónica")
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 20, 50, 20)
        self.verticalLayout_2.setSpacing(10)

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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.pesContactos)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(25, 50, 25, 50)
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setVerticalSpacing(10)
        
        # ID
        self.lblid= QtWidgets.QLabel(parent=self.pesContactos)
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
        self.txtid.setStyleSheet("background-color: rgb(130, 94, 104);")

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
        self.gridLayout_2.addWidget(self.lblid, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtid, 0, 2, 1, 1)

        # Segunda fila
        self.gridLayout_2.addWidget(self.lblnombre, 1, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtnombre, 1, 2, 1, 2)
        self.gridLayout_2.addWidget(self.lblnotas, 1, 4, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtnotas, 1, 5, 1, 2)

        # Tercera fila
        self.gridLayout_2.addWidget(self.lblemail, 2, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtemail, 2, 2, 1, 2)
        self.gridLayout_2.addWidget(self.lblfechaalta, 2, 4, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtfechaalta, 2, 5, 1, 1)

        # Cuarta fila
        self.gridLayout_2.addWidget(self.lblmovil, 3, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtmovil, 3, 2, 1, 1)
        self.gridLayout_2.addWidget(self.lblciudad, 3, 4, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtCiudad, 3, 5, 1, 1)

        # Configurar columnas para mejor alineación
        self.gridLayout_2.setColumnMinimumWidth(1, 100)   # Labels izquierda
        self.gridLayout_2.setColumnMinimumWidth(2, 300)   # Campos texto izquierda
        self.gridLayout_2.setColumnMinimumWidth(3, 200)   # Aumentar espacio entre grupos
        self.gridLayout_2.setColumnMinimumWidth(4, 100)   # Labels derecha
        self.gridLayout_2.setColumnMinimumWidth(5, 300)   # Campos texto derecha

        # Ajustar stretch para que ocupe todo el ancho disponible
        self.gridLayout_2.setColumnStretch(0, 1)  # Stretch izquierda
        self.gridLayout_2.setColumnStretch(6, 1)  # Stretch derecha

        # Layout horizontal para botones
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setSpacing(20)
        
        # Crear horizontal spacers
        self.horizontalSpacer_5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalSpacer_6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        
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
        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)
        self.horizontalLayout_3.addWidget(self.btnAlta)
        self.horizontalLayout_3.addWidget(self.btnModificar)
        self.horizontalLayout_3.addWidget(self.btnEliminar)
        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)
        
         # Crear tabla
        self.tablaContactos = QtWidgets.QTableWidget(parent=self.pesContactos)
        self.tablaContactos.setObjectName("tablaContactos")
        self.tablaContactos.setMinimumSize(QtCore.QSize(700, 200))
        self.tablaContactos.setColumnCount(7)
        self.tablaContactos.setRowCount(0)
        self.tablaContactos.setHorizontalHeaderLabels(["ID", "Nombre", "Email", "Móvil", "Ciudad", "Notas", "Fecha Alta"])
        
        # Configurar propiedades de la tabla
        self.tablaContactos.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaContactos.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaContactos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaContactos.horizontalHeader().setStretchLastSection(True)
        self.tablaContactos.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tablaContactos.verticalHeader().setVisible(False)
        
        # Ajustar ancho de columnas
        self.tablaContactos.setColumnWidth(0, 60)    # ID (como txtid: 60)
        self.tablaContactos.setColumnWidth(1, 250)   # Nombre (como txtnombre: 250)
        self.tablaContactos.setColumnWidth(2, 240)   # Email (como txtemail: 240)
        self.tablaContactos.setColumnWidth(3, 70)    # Móvil (como txtmovil: 70)
        self.tablaContactos.setColumnWidth(4, 110)   # Ciudad (como txtCiudad: 110)
        self.tablaContactos.setColumnWidth(5, 240)   # Notas (como txtnotas: 240)
        self.tablaContactos.setColumnWidth(6, 70)    # Fecha Alta (como txtfechaalta: 70)

        # Añadir layouts y widgets al gridLayout_2
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 1, 1, 5)  # Botones
        self.gridLayout_2.addWidget(self.tablaContactos, 5, 1, 1, 5)      # Tabla
        
        # Ajustar espaciado vertical
        self.gridLayout_2.setRowMinimumHeight(4, 30)  # Espacio antes de botones
        self.gridLayout_2.setRowMinimumHeight(5, 20)  # Espacio antes de tabla
              
        # Añadir pestaña y panel principal
        self.panPrincipal.addTab(self.pesContactos, "CONTACTOS")
        self.verticalLayout_2.addWidget(self.panPrincipal)

        # Crear barra de menú
        self.menubar = QtWidgets.QMenuBar(venPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1537, 21))
        self.menubar.setObjectName("menubar")

        # Crear menús principales
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuArchivo.setTitle("Archivo")

        self.menuHerramientas = QtWidgets.QMenu(parent=self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        self.menuHerramientas.setTitle("Herramientas")

        self.menuAyuda = QtWidgets.QMenu(parent=self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuAyuda.setTitle("Ayuda")

        # Establecer la barra de menú
        venPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=venPrincipal)
        self.statusbar.setObjectName("statusbar")
        venPrincipal.setStatusBar(self.statusbar)
        self.toolbar = QtWidgets.QToolBar(parent=venPrincipal)
        self.toolbar.setObjectName("toolbar")
        venPrincipal.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolbar)

        # Crear acciones para el menú Archivo
        self.actionSalir = QtGui.QAction(venPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.actionSalir.setText("Salir")
        self.actionSalir.setShortcut("Ctrl+S")

        # Crear acciones para el menú Herramientas
        self.actionCrear_Backup = QtGui.QAction(venPrincipal)
        self.actionCrear_Backup.setObjectName("actionCrear_Backup")
        self.actionCrear_Backup.setText("Crear Backup")

        self.actionRestaurar_Backup = QtGui.QAction(venPrincipal)
        self.actionRestaurar_Backup.setObjectName("actionRestaurar_Backup")
        self.actionRestaurar_Backup.setText("Restaurar Backup")

        # Crear acciones para el menú Ayuda
        self.actionAcercaDe = QtGui.QAction(venPrincipal)
        self.actionAcercaDe.setObjectName("actionAcercaDe")
        self.actionAcercaDe.setText("Acerca de")

        # Añadir acciones a los menús
        self.menuArchivo.addAction(self.actionSalir)
        
        # Añadir acciones a Herramientas
        self.menuHerramientas.addAction(self.actionCrear_Backup)
        self.menuHerramientas.addAction(self.actionRestaurar_Backup)
        
        self.menuAyuda.addAction(self.actionAcercaDe)
        
        # Añadir menús a la barra de menú
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
