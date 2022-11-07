import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import tp_disqueria_GUI.modelo as mo

class EliminarController():

    def __init__(self, eliminar):
        self.con = mo.Conectar()
        self.eliminar = eliminar

    def listar_album(self):
        con = mo.Conectar()
        listado = con.consulta_album()
        table = self.eliminar.tabla
        table.setRowCount(0)
        for fila, album in enumerate(listado):
            table.insertRow(fila)
            for columna, data in enumerate(album):
                table.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(data)))

    def eliminar_album(self):
        con = mo.Conectar()
        msg = QMessageBox()
        table = self.eliminar.tabla
        if table.currentItem() != None:
            cod = table.currentItem().text()
            con.eliminar_album(cod)
        msg.setWindowTitle('Disqueria')
        msg.setText('¡Album Eliminado exitosamente!')
        msg.exec_()
        self.listar_album()