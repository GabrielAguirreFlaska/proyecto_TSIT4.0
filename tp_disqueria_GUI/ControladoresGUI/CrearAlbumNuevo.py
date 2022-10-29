

import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import tp_disqueria_GUI.control as co
import tp_disqueria_GUI.modelo as mo


class CrearNuevoAlbum():
    def __init__(self, nuevo_album):
        self.crear_nuevo_album = nuevo_album 