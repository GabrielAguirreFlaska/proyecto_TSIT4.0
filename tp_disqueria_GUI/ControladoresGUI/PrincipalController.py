
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import tp_disqueria_GUI.control as co
import tp_disqueria_GUI.modelo as mo



class PrincipalController():

    def __init__(self, principal):
        self.con = mo.Conectar()
        self.principal = principal

    def listar_albumes_por_artista(self):
        con = mo.Conectar()
        listado = con.consulta_albumes_por_artista()
        table = self.principal.tabla_principal
        table.setRowCount(0)
        for fila, album in enumerate(listado):
            table.insertRow(fila)
            for columna, data in enumerate(album):
                table.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(data)))

    def abrir_crear_album(self, Ui_CrearProducto):
        self.principal.Form = QtWidgets.QWidget()
        self.principal.ui = Ui_CrearProducto()
        self.principal.ui.setupUi(self.principal.Form)
        self.principal.Form.show()
                
