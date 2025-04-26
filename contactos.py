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
            nuevoContacto = [var.ui.txtnombre.text().title(), var.ui.txtemail.text(), var.ui.txtmovil.text(), var.ui.txtciudad.text(), var.ui.txtnotas.text()]
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
            listadocont = conexion.Conexion.listadoContactos()  # Obtener todos los contactos
            var.longcont = len(listadocont)  # Guardar el número total de contactos
            index = 0
            for registro in listadocont:
                var.ui.tablaContactos.setRowCount(index + 1)
                var.ui.tablaContactos.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))  # ID
                var.ui.tablaContactos.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))  # Nombre
                var.ui.tablaContactos.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))  # Email
                var.ui.tablaContactos.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))  # Móvil
                var.ui.tablaContactos.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))  # Ciudad
                var.ui.tablaContactos.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))  # Notas
                var.ui.tablaContactos.setItem(index, 6, QtWidgets.QTableWidgetItem(str(registro[6])))  # Fecha Alta                
                # Opcional: Alineación de columnas
                for col in range(7):  # Suponiendo que tienes 7 columnas
                    var.ui.tablaContactos.item(index, col).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)            
                index += 1
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