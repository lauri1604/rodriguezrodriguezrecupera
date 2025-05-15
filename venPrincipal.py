from PyQt6 import QtWidgets, QtGui, QtCore

class Ui_venprincipal(object):
    def setupUi(self,venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.setWindowTitle("Agenda Telefónica")
        venPrincipal.resize(1570, 903)
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
        self.verticalSpacer_1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalSpacer_2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.horizontalSpacer_5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalSpacer_6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setSpacing(20)
        
        self.botonalta = QtWidgets.QPushButton(parent=self.pesContactos)
        self.botonalta.setText("ALTA")
        self.botonalta.setFixedSize(105, 45)
        
        self.botonmodificar = QtWidgets.QPushButton(parent=self.pesContactos)
        self.botonmodificar.setText("MODIFICAR")
        self.botonmodificar.setFixedSize(115, 45)
        
        self.botoneliminar = QtWidgets.QPushButton(parent=self.pesContactos)
        self.botoneliminar.setText("ELIMINAR")
        self.botoneliminar.setFixedSize(105, 45)
        
        # Añadir botones al layout horizontal
        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)
        self.horizontalLayout_3.addWidget(self.botonalta)
        self.horizontalLayout_3.addWidget(self.botonmodificar)
        self.horizontalLayout_3.addWidget(self.botoneliminar)
        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)
        
        # Crear tabla
        self.tablaContactos = QtWidgets.QTableWidget(self.pesContactos)
        self.tablaContactos.setObjectName("tablaContactos")
        self.tablaContactos.setColumnCount(7)
        self.tablaContactos.setHorizontalHeaderLabels(["ID", "Nombre", "Email", "Móvil", "Ciudad", "Notas", "Fecha Alta"])
        self.tablaContactos.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaContactos.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaContactos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaContactos.horizontalHeader().setStretchLastSection(True)
        self.tablaContactos.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tablaContactos.verticalHeader().setVisible(False)
        self.tablaContactos.setMinimumSize(QtCore.QSize(1200, 500))

        
        # Configurar propiedades de la tabla
        self.tablaContactos.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaContactos.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaContactos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaContactos.horizontalHeader().setStretchLastSection(True)
        self.tablaContactos.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.tablaContactos.verticalHeader().setVisible(False)
        
        # Ajustar ancho de columnas
        self.tablaContactos.setColumnWidth(0, 65)    # ID
        self.tablaContactos.setColumnWidth(1, 250)   # Nombre
        self.tablaContactos.setColumnWidth(2, 240)   # Email
        self.tablaContactos.setColumnWidth(3, 85)    # Móvil
        self.tablaContactos.setColumnWidth(4, 130)   # Ciudad
        self.tablaContactos.setColumnWidth(5, 230)   # Notas
        self.tablaContactos.setColumnWidth(6, 90)    # Fecha Alta
        
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
        self.txtid.setStyleSheet("background-color: rgb(255, 255, 220);")

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
        self.txtnombre.setStyleSheet("background-color: rgb(255, 255, 239);")

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
        self.txtfechaalta.setMinimumSize(QtCore.QSize(80, 0))
        self.txtfechaalta.setMaximumSize(QtCore.QSize(90, 25))
        self.txtfechaalta.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.txtfechaalta.setStyleSheet("background-color: rgb(255, 255, 239);")

        # Móvil
        self.lblmovil = QtWidgets.QLabel(parent=self.pesContactos)
        self.lblmovil.setObjectName("lblmovil")
        self.lblmovil.setText("Móvil")
        self.lblmovil.setMinimumSize(QtCore.QSize(40, 0))
        self.lblmovil.setMaximumSize(QtCore.QSize(50, 25))
        self.lblmovil.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.txtmovil = QtWidgets.QLineEdit(parent=self.pesContactos)
        self.txtmovil.setObjectName("txtmovil")
        self.txtmovil.setMinimumSize(QtCore.QSize(85, 0))
        self.txtmovil.setMaximumSize(QtCore.QSize(100, 25))
        self.txtmovil.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.txtmovil.setStyleSheet("background-color: rgb(255, 255, 239);")

        # Ciudad
        self.lblciudad = QtWidgets.QLabel(parent=self.pesContactos)
        self.lblciudad.setObjectName("lblciudad")
        self.lblciudad.setText("Ciudad")
        self.lblciudad.setMinimumSize(QtCore.QSize(50, 0))
        self.lblciudad.setMaximumSize(QtCore.QSize(60, 25))
        self.lblciudad.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.txtciudad = QtWidgets.QLineEdit(parent=self.pesContactos)
        self.txtciudad.setObjectName("txtciudad")
        self.txtciudad.setMinimumSize(QtCore.QSize(80, 0))
        self.txtciudad.setMaximumSize(QtCore.QSize(110, 25))
        self.txtciudad.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.txtciudad.setStyleSheet("background-color: rgb(255, 255, 239);")

        # Añadir widgets al gridLayout
        self.gridLayout_2.addItem(self.verticalSpacer_1, 0, 0, 1, 7)  # Spacer superior
        
        # Primera fila (ID)
        self.gridLayout_2.addWidget(self.lblid, 1, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtid, 1, 2, 1, 1)
        
        # Segunda fila (Nombre y Ciudad)
        self.gridLayout_2.addWidget(self.lblnombre, 2, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtnombre, 2, 2, 1, 2)
        self.gridLayout_2.addWidget(self.lblciudad, 2, 4, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtciudad, 2, 5, 1, 1)
        
        # Tercera fila (Email y Notas)
        self.gridLayout_2.addWidget(self.lblemail, 3, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtemail, 3, 2, 1, 2)
        self.gridLayout_2.addWidget(self.lblnotas, 3, 4, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtnotas, 3, 5, 1, 2)
        
        # Cuarta fila (Móvil y Fecha Alta)
        self.gridLayout_2.addWidget(self.lblmovil, 4, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtmovil, 4, 2, 1, 1)
        self.gridLayout_2.addWidget(self.lblfechaalta, 4, 4, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_2.addWidget(self.txtfechaalta, 4, 5, 1, 1)

        # Botones y tabla
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 5, 1, 1, 5)  # Botones
        self.gridLayout_2.addWidget(self.tablaContactos, 6, 1, 1, 5)      # Tabla
        self.gridLayout_2.addItem(self.verticalSpacer_2, 7, 1, 1, 7)      # Spacer inferior
        
        # Configurar columnas para mejor alineación
        self.gridLayout_2.setColumnMinimumWidth(1, 100)   # Labels izquierda
        self.gridLayout_2.setColumnMinimumWidth(2, 300)   # Campos texto izquierda
        self.gridLayout_2.setColumnMinimumWidth(3, 200)   # Aumentar espacio entre grupos
        self.gridLayout_2.setColumnMinimumWidth(4, 100)   # Labels derecha
        self.gridLayout_2.setColumnMinimumWidth(5, 300)   # Campos texto derecha

        # Ajustar stretch para que ocupe todo el ancho disponible
        self.gridLayout_2.setColumnStretch(0, 1)  # Stretch izquierda
        self.gridLayout_2.setColumnStretch(6, 1)  # Stretch derecha
        
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
        
        self.menuGestion = QtWidgets.QMenu(parent=self.menubar)
        self.menuGestion.setObjectName("menuGestion")
        self.menuGestion.setTitle("Gestión")

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
        self.menubar.addAction(self.menuGestion.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        
        self.retranslateUi(venPrincipal)
        self.panPrincipal.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)
        venPrincipal.setTabOrder(self.txtid, self.txtnombre)
        venPrincipal.setTabOrder(self.txtnotas, self.txtfechaalta)
        venPrincipal.setTabOrder(self.txtmovil, self.txtciudad)
        venPrincipal.setTabOrder(self.botonalta, self.botonmodificar)
        venPrincipal.setTabOrder(self.botoneliminar, self.tablaContactos)
        
    def retranslateUi(self, venPrincipal):
            _translate = QtCore.QCoreApplication.translate
            venPrincipal.setWindowTitle(_translate("venPrincipal", "Agenda Telefónica"))
            self.panPrincipal.setTabText(self.panPrincipal.indexOf(self.pesContactos), _translate("venPrincipal", "CONTACTOS"))
            self.menuArchivo.setTitle(_translate("venPrincipal", "Archivo"))
            self.actionSalir.setText(_translate("venPrincipal", "Salir"))
            self.menuGestion.setTitle(_translate("venPrincipal", "Gestión"))
            self.menuHerramientas.setTitle(_translate("venPrincipal", "Herramientas"))
            self.actionCrear_Backup.setText(_translate("venPrincipal", "Crear Backup"))
            self.actionRestaurar_Backup.setText(_translate("venPrincipal", "Restaurar Backup"))
            self.menuAyuda.setTitle(_translate("venPrincipal", "Ayuda"))
            self.actionAcercaDe.setText(_translate("venPrincipal", "Acerca de"))
            self.botonalta.setText(_translate("venPrincipal", "ALTA"))
            self.botonmodificar.setText(_translate("venPrincipal", "MODIFICAR"))
            self.botoneliminar.setText(_translate("venPrincipal", "ELIMINAR"))
            item = self.tablaContactos.horizontalHeaderItem(0)
            item.setText(_translate("venPrincipal", "ID"))
            item = self.tablaContactos.horizontalHeaderItem(1)
            item.setText(_translate("venPrincipal", "Nombre"))
            item = self.tablaContactos.horizontalHeaderItem(2)
            item.setText(_translate("venPrincipal", "Email"))
            item = self.tablaContactos.horizontalHeaderItem(3)
            item.setText(_translate("venPrincipal", "Móvil"))
            item = self.tablaContactos.horizontalHeaderItem(4)
            item.setText(_translate("venPrincipal", "Ciudad"))
            item = self.tablaContactos.horizontalHeaderItem(5)
            item.setText(_translate("venPrincipal", "Notas"))
            item = self.tablaContactos.horizontalHeaderItem(6)
            item.setText(_translate("venPrincipal", "Fecha Alta"))