from PyQt6.QtCore import Qt
from dlgAbout import *
from dlgCalendar import *
from PyQt6.QtCore import Qt
from datetime import datetime
import eventos
import var

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()
        
class dlgAbout(QtWidgets.QDialog):
    def __init__(self):
        super(dlgAbout, self).__init__()
        self.ui = Ui_dlgAbout()
        self.ui.setupUi(self)
        self.ui.botonCerrarAbout.clicked.connect(eventos.Eventos.cerrarAbout)
        
class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.uicalendar = Ui_dlgCalendar()
        var.uicalendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        
        var.uicalendar.Calendar.setSelectedDate((QtCore.QDate(ano,mes,dia)))