import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import modelo as mo, control as co



class PrincipalController():

    def __init__(self, principal):
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
                
