from PyQt6 import QtSql, QtWidgets, QtCore
from idlelib.query import Query
from datetime import datetime
import os
import var
import sqlite3
import var
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
            query.prepare("INSERT into CONTACTOS (nombre, email, movil, ciudad, notas, fecha_alta ) VALUES (:nombre, :email, :movil, :ciudad, :notas, :fecha_alta)")
            query.bindValue(":nombre", str(nuevoContacto[0]))
            query.bindValue(":email", str(nuevoContacto[1]))
            query.bindValue(":movil", str(nuevoContacto[2]))
            query.bindValue(":ciudad", str(nuevoContacto[3]))
            query.bindValue(":notas", str(nuevoContacto[4]))
            query.bindValue(":fecha_alta", str(nuevoContacto[5]))
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
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM CONTACTOS WHERE fecha_alta is NULL ORDER BY nombre ASC")
            if query.exec():
                while query.next():
                    fila = [query.value(i) for i in range(query.record().count())]
                    listado.append(fila)
                return listado
            else:
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
                        registro.append(str(query.value(i)))
            return registro
        except Exception as e:
            print("Error datos un contacto", e)
            
    def datosContacto(id):
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM CONTACTOS WHERE id = :id")
        query.bindValue(":id", str(id))
        if query.exec():
            while query.next():
                fila = []
                for i in range(query.record().count()):
                    fila.append(str(query.value(i)))
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
                        query.prepare("UPDATE CONTACTOS SET fecha_alta = :fecha_alta,  nombre = :nombre", "email = :email, movil = :movil, ciudad = :ciudad, notas = :notas WHERE id = :id")
                        query.bindValue(":id", str(registro[0]))
                        query.bindValue(":nombre", str(registro[1]))
                        query.bindValue(":email", str(registro[2]))
                        query.bindValue(":movil", str(registro[3]))
                        query.bindValue(":ciudad", str(registro[4]))
                        query.bindValue(":notas", str(registro[5]))
                        query.bindValue(":fecha_alta", str(registro[6]))
                        if registro[7] == "":
                            query.bindValue(":fecha_alta", QtCore.QVariant())
                        else:
                            query.bindValue(":fecha_alta", str(registro[7]))
                        if query.exec():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except Exception as e:
            print("Error modificar contacto: ", e)
            
    