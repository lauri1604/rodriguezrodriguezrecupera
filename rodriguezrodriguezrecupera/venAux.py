from PyQt6.QtCore import Qt
from dlgAbout import *

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()
        
class dlgAbout(QtWidgets.QDialog):
    def __init__(self):
        super(dlgAbout, self).__init__()
        self.ui = Ui_dlgAbout()
        self.ui.setupUi(self)
        self.ui.botonCerrarAbout.clicked.connect(eventos.Eventos.cerrarAbout)