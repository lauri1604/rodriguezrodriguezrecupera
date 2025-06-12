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
            nomepdfcont = fecha + "_listadocontactos.pdf"
            pdf_path = os.path.join(rootPath, nomepdfcont)
            var.report = canvas.Canvas(pdf_path)
            titulo = "Listado Contactos"
            query0 = QtSql.QSqlQuery()
            query0.exec("SELECT COUNT(*) FROM CONTACTOS")
            if query0.next():
                print(query0.value(0))
                registros = int(query0.value(0))
                paginas = int(registros / 20) + 1  # quitar 1 poque si es exacto suma 1 nás
            Informes.topInforme(titulo)
            Informes.footInforme(titulo, paginas)
            items = ['ID', 'NOMBRE', 'EMAIL','MOVIL', 'CIUDAD']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(65, 650, str(items[0]))
            var.report.drawString(114, 650, str(items[1]))
            var.report.drawString(250, 650, str(items[2]))
            var.report.drawString(370, 650, str(items[3]))
            var.report.drawString(450, 650, str(items[4]))
            var.report.line(50, 645, 525, 645)
            query = QtSql.QSqlQuery()
            query.prepare("SELECT id, nombre, email, movil, ciudad FROM CONTACTOS ORDER BY NOMBRE ASC")
            if query.exec():
                registros = query.value(0)
                print (registros)
                x = 65
                y = 625
                while query.next():
                    if y <= 90:
                        var.report.setFont('Helvetica-Oblique', size=8)
                        var.report.drawString(450,75, "Página siguiente...")
                        var.report.showPage()  #crea una página nueva
                        Informes.footInforme(titulo, paginas)
                        Informes.topInforme(titulo)
                        items = ['ID', 'NOMBRE', 'EMAIL','MOVIL', 'CIUDAD']
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(95, 650, str(items[0]))
                        var.report.drawString(114, 650, str(items[1]))
                        var.report.drawString(220, 650, str(items[2]))
                        var.report.drawString(280, 650, str(items[3]))
                        var.report.drawString(390, 650, str(items[4]))
                        var.report.line(50, 645, 525, 645)
                        x = 55
                        y = 740
                    var.report.setFont('Helvetica', size=8)
                    var.report.drawString(x, y, str(query.value(0)))  # ID
                    var.report.drawString(x + 53, y, str(query.value(1)))  # Nombre
                    var.report.drawString(x + 200, y, str(query.value(2)))  # Email
                    var.report.drawString(x + 310, y, str(query.value(3)))  # Móvil
                    var.report.drawString(x + 400, y, str(query.value(4)))  # Ciudad
                    y = y - 25
                var.report.save()
                for file in os.listdir(rootPath):
                    if file.endswith(nomepdfcont):
                        os.startfile(pdf_path)
        except Exception as e:
            print("Error en informe contactos", e)
            
    def topInforme(titulo):
        try:
            ruta_logo = '.\\img\\logo.ico'
            logo = Image.open(ruta_logo)
            # drawing = svg2rlg(svg_file)  PARA FICHEROS SVG
            # renderPM.drawToFile(drawing, "logo.png", fmt="PNG")
            # logo = QPixmap("logo.png")
            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'Agenda telefónica')
                var.report.drawCentredString(300, 675, titulo)
                var.report.line(50, 665, 525, 665)
                # Dibuja la imagen en el informe
                var.report.drawImage(ruta_logo, 480, 745, width=35, height=35)
                var.report.setFont('Helvetica', size=8)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Andrea López')
                var.report.drawString(55, 740, 'Avda. Galicia - 101')
                var.report.drawString(55, 725, 'Teléfono: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: agendatelf@mail.com')
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')
        except Exception as error:
            print('Error en cabecera informe:', error)
            
    def footInforme(titulo, paginas):
        try:
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber() + '/' + str(paginas)))
        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)