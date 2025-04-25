from PyQt6 import QtWidgets, QtGui, QtCore
from datetime import datetime
from sys import exception
import var
import eventos
import conexion

class Contactos:
    def __init__(self):
        self.valor = 0
        
    def checkEmail(mail):
        try:
           if eventos.Eventos.validarMail(mail):
                 var.ui.txtemail.setStyleSheet('background-color: rgb(255, 255, 255);')
           else:
                var.ui.txtemail.setStyleSheet('background-color: #FFC0CB; font-style: italic;')
                var.ui.txtemail.setPlaceholderText("correo no válido")
                var.ui.txtemail.setFocus()
        except Exception as error:
            print("error check mail", error)

    def checkMovil(movil):
        try:
           if eventos.Eventos.validarMovil(movil):
                var.ui.txtmovil.setStyleSheet('background-color: rgb(255, 255, 239);')
           else:
                var.ui.txtmovil.setStyleSheet('background-color: #FFC0CB; font-style: italic;')                
                var.ui.txtmovil.setPlaceholderText("móvil no válido")
                var.ui.txtmovil.setFocus()
        except Exception as error:
            print("error check movil", error)

    def altaContacto(self):
        try:
            op = 0
            nuevoContacto = [var.ui.txtnombre.text().title(), var.ui.txtemail.text(), var.ui.txtmovil.text(), var.ui.txtciudad.text(), var.ui.txtnotas.toPlainText()]
            if (nuevoContacto[0] != "" and nuevoContacto[1] != "" and nuevoContacto[2] != "" and nuevoContacto[3] != "" and nuevoContacto[4] != ""):
                op = 1
                if conexion.Conexion.altaContacto and op == 1:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setWindowIcon(QtGui.QIcon('img/logo.ico'))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText("Alta Contacto en Base de Datos")
                    mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()
                    Contactos.cargaTablaContactos(self)
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle("Aviso")
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                    mbox.setWindowIcon(QtGui.QIcon('img/logo.ico'))
                    mbox.setText('Error Faltan Datos o Contacto Existe')
                    mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Cancel).setText('Cancelar')
                    mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('img/logo.ico'))
                mbox.setText('Error Faltan Datos')
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Cancel).setText('Cancelar')
                mbox.exec()
        except Exception as error:
            print("error alta contacto", error)
    
    @staticmethod
    def cargaTablaContactos(self):
        try:
            # Obtener el listado de contactos
            listadoContactos = conexion.Conexion.listadoContactos()
            # Manejar caso de listado vacío
            if not listadoContactos:
                var.ui.tablaContactos.setRowCount(1)  # Una fila para el mensaje
                item = QtWidgets.QTableWidgetItem("No hay contactos para mostrar")
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaContactos.setItem(0, 0, item)
                var.ui.tablaContactos.setSpan(0, 0, 1, var.ui.tablaContactos.columnCount())  # Combinar celdas
                return
            # Configurar el número de filas en la tabla según el listado
            var.ui.tablaContactos.setRowCount(len(listadoContactos))

            # Enumerar el listado y añadir cada contacto a la tabla
            for index, registro in enumerate(listadoContactos):
                columnas = [(QtCore.Qt.AlignmentFlag.AlignCenter, 0),  # id
                    (QtCore.Qt.AlignmentFlag.AlignLeft, 1),    # nombre
                    (QtCore.Qt.AlignmentFlag.AlignLeft, 2),    # email
                    (QtCore.Qt.AlignmentFlag.AlignCenter, 3),  # movil
                    (QtCore.Qt.AlignmentFlag.AlignLeft, 4),    # ciudad
                    (QtCore.Qt.AlignmentFlag.AlignLeft, 5),    # notas
                    (QtCore.Qt.AlignmentFlag.AlignCenter, 6)   # fecha_alta
                ]
                for col, (alignment, i) in enumerate(columnas):
                    item = QtWidgets.QTableWidgetItem(str(registro[i]))
                    item.setTextAlignment(alignment)
                    var.ui.tablaContactos.setItem(index, col, item)
        except Exception as e:
            print("error carga tabla contactos", e)
            
    def cargaOneContacto(self):
        try:
             # Obtener el contacto seleccionado de la tabla
            fila = var.ui.tablaContactos.selectedItems()
            datos = [dato.text() for dato in fila]
            # Obtener datos completos desde la base de datos
            registro = conexion.Conexion.datosOneContacto(str(datos[0]))            
            # Asegurarse de que no hay valores None
            registro_limpio = []
            for dato in registro:
                if dato == 'None':
                    registro_limpio.append('')
                else:
                    registro_limpio.append(dato)
            # Lista de campos UI en el mismo orden que vienen de la base de datos
            listado = [var.ui.txtid, var.ui.txtnombre, var.ui.txtemail, var.ui.txtmovil, var.ui.txtciudad, var.ui.txtnotas, var.ui.txtfechaalta]
            # Asignar valores directamente a los campos
            for i in range(len(listado)):
                listado[i].setText(registro_limpio[i])
        except Exception as error:
            print("error cargaOneContacto", error)