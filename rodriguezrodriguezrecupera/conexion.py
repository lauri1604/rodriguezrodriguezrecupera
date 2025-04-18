from PyQt6 import QtSql, QtWidgets, QtCore
from idlelib.query import Query
from datetime import datetime
import os
import var
import sqlite3

class Conexion:
    @staticmethod
    def db_conexion(self = None):
        if not os.path.isfile('bbdd.db'):
            QtWidgets.QMessageBox.critical(None, 'Error', 'El archivo de la base de datos no existe.',
                                        QtWidgets.QMessageBox.StandardButton.Cancel)
            return False
        
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('bbdd.db')

        if db.open():
            query = QtSql.QSqlQuery()
            query.exec("SELECT name FROM sqlite_master WHERE type='table';")

            if not query.next():
                QtWidgets.QMessageBox.critical(None, 'Error', 'Base de datos vacía o no válida.',
                                            QtWidgets.QMessageBox.StandardButton.Cancel)
                return False
            else:
                QtWidgets.QMessageBox.information(None, 'Aviso', 'Conexión Base de Datos realizada',
                                            QtWidgets.QMessageBox.StandardButton.Ok)
                return True
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', 'No se pudo abrir la base de datos.',
                                        QtWidgets.QMessageBox.StandardButton.Cancel)
            return False
    
    def altaContacto(nuevoContacto):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT into CONTACTOS (id, nombre, email, movil, ciudad, notas, fecha_alta) VALUES (:id, :nombre, :email, :movil, :ciudad, :notas, :fecha_alta)")
            query.bindValue(":id", nuevoContacto[0])
            query.bindValue(":nombre", nuevoContacto[1])
            query.bindValue(":email", nuevoContacto[2])
            query.bindValue(":movil", nuevoContacto[3])
            query.bindValue(":ciudad", nuevoContacto[4])
            query.bindValue(":notas", nuevoContacto[5])
            query.bindValue(":fecha_alta", nuevoContacto[6])
            if query.exec():
                return True
            else:
                return False
        except Exception as e:
            print("Error al insertar el contacto: ", e)
        except sqlite3.IntegrityError:
            return False
        
    def listadoContactos(self):
        try:
            listado = []
            if var.historico == 1:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM CONTACTOS WHERE fecha_alta is NULL ORDER BY nombre ASC")
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                        return listado
                elif var.historico == 0:
                    query = QtSql.QSqlQuery()
                    query.prepare("SELECT * FROM CONTACTOS ORDER BY nombre ASC")
                    if query.exec():
                        while query.next():
                            fila = [query.value(i) for i in range(query.record().count())]
                            listado.append(fila)
                            return listado
        except Exception as e:
            print("Error listado en conexion", e)
            
    def datosOneContacto(id):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM CONTACTOS WHERE id = :id")
            query.bindValue(":id", str(id))
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(query.value(i))
                return registro
        except Exception as e:
            print("Error datos un contacto", e)
            
    def datosContacto(id):
        Query = QtSql.QSqlQuery()
        Query.prepare("SELECT * FROM CONTACTOS WHERE id = :id")
        Query.bindValue(":id", str(id))
        if Query.exec():
            while Query.next():
                fila = []
                for i in range(Query.record().count()):
                    fila.append(str(Query.value(i)))
                return fila
            
    def modificarContacto(registro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT count(*) FROM CONTACTOS WHERE id = :id")
            query.bindValue(":id", str(registro[0]))
            if query.exec():
                if query.next() and query.value(0)>0:
                    if query.exec():
                        query = QtSql.QSqlQuery()
                        query.prepare("UPDATE CONTACTOS SET fecha_alta = :fecha_alta :nombre, email = :email, movil = :movil, ciudad = :ciudad, notas = :notas WHERE id = :id")
                        query.bindValue(":id", registro[0])
                        query.bindValue(":nombre", registro[1])
                        query.bindValue(":email", registro[2])
                        query.bindValue(":movil", registro[3])
                        query.bindValue(":ciudad", registro[4])
                        query.bindValue(":notas", registro[5])
                        if query.exec():
                            return True
                        else:
                            return False
                else:
                    return False
            else:
                return False
        except Exception as e:
            print("Error al modificar el contacto: ", e)