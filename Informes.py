from reportlab.pdfgen import canvas
from datetime import datetime
from PIL import Image
from PyQt6 import QtSql, QtWidgets, QtCore, QtGui
import sqlite3
import os
import var
import conexion

class Informes:
    @staticmethod
    def reportContactos(self):
        try:
            rootPath = '.\\informes'
            if not os.path.exists(rootPath):
                os.makedirs(rootPath)
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%M_%S")
            nomepdfcont = fecha + "_listadoclientes.pdf"
            pdf_path = os.path.join(rootPath, nomepdfcont)
            var.report = canvas.Canvas(pdf_path)
            titulo = "Listado Clientes"
            query0 = QtSql.QSqlQuery()
            query0.exec("select count(*) from clientes")
            if query0.next():
                print(query0.value(0))
                registros = int(query0.value(0))
                paginas = int(registros / 20) + 1  # quitar 1 poque si es exacto suma 1 nás
            Informes.topInforme(titulo)
            Informes.footInforme(titulo, paginas)
            items = ['ID', 'NOMBRE', 'EMAIL','MOVIL', 'CIUDAD']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(55, 650, str(items[0]))
            var.report.drawString(100, 650, str(items[1]))
            var.report.drawString(190, 650, str(items[2]))
            var.report.drawString(280, 650, str(items[3]))
            var.report.drawString(355, 650, str(items[4]))
            var.report.drawString(440, 650, str(items[5]))
            var.report.line(50, 645, 525, 645)
        except Exception as e:
            print(e)