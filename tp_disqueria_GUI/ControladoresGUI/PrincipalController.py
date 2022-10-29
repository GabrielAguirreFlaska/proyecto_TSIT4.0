
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

    def listProducts(self):
        con = mo.Conectar()
        listado = con.consulta_albumes()
        table = self.principal.tabla_principal
        table.setRowCount(0)
        for fila, album in enumerate(listado):
            table.insertRow(fila)
            for columna, data in enumerate(album):
                table.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(data)))
#############################################
    def deleteProduct(self):
        con = mo.Conectar()
        table = self.principal.tabla_principal
        if table.currentItem() != None:
            cod = table.currentItem().text()
            con.eliminar_album(cod)
        self.listProducts()  
##############################################
    def abrir_crear_album(self, Ui_CrearProducto):
        self.principal.Form = QtWidgets.QWidget()
        self.principal.ui = Ui_CrearProducto()
        self.principal.ui.setupUi(self.principal.Form)
        self.principal.Form.show()
                

    def updateProduct(self):
        con = mo.Conectar()
        table = self.principal.tabla_principal
        products = []
        fila = []
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number,column_number) != None:
                    fila.append(table.item(row_number,column_number).text())
            if len(fila)>0:
                products.append(fila)
            fila = []
        
        if len(products)>0:
            for prod in products:
                self.con.updateProduct(prod[0],prod[1],prod[2],prod[3])
        
        self.listProducts() 
