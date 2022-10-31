
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

    def listar_inter(self):
        con = mo.Conectar()
        listado = con.listar_interpretes()
        table = self.principal.tabla_listar_interpretes
        table.setRowCount(0)
        for fila, inter in enumerate(listado):
            table.insertRow(fila)
            for col, data in enumerate(inter):
                table.setItem(fila, col, QtWidgets.QTableWidgetItem(str(data)))

    def listar_temas(self):
        con = mo.Conectar()
        listado = con.listar_tema()
        table = self.principal.tabla_listar_temas
        table.setRowCount(0)
        for fila, album in enumerate(listado):
            table.insertRow(fila)
            for col, data in enumerate(album):
                table.setItem(fila, col, QtWidgets.QTableWidgetItem(str(data)))

    

        
#############################################
    def deleteProduct(self):
        con = mo.Conectar()
        table = self.principal.tabla_principal
        if table.currentItem() != None:
            cod = table.currentItem().text()
            con.eliminar_album(cod)
        self.listProducts()  
##############################################
    # def abrir_crear_album(self, Ui_CrearProducto):
    #     self.principal.Form = QtWidgets.QWidget()
    #     self.principal.ui = Ui_CrearProducto()
    #     self.principal.ui.setupUi(self.principal.Form)
    #     self.principal.Form.show()

    def crear_nuevo_album(self, cod_album, nombre, interprete, genero,cant_temas, discografica, formato, fec_lanzamiento, precio, cantidad, caratula):
        con = mo.Conectar()
        nombre_apellido = interprete.split(maxsplit=1)
        id_interprete = con.id_interprete_por_nombre(nombre_apellido[0], nombre_apellido[1])
        id_genero = con.id_genero_por_nombre(genero)
        id_discografica = con.id_discografica_por_nombre(discografica)
        id_formato = con.id_formato_por_nombre(formato)
        nuevoAlbum = mo.Album(0,cod_album,nombre,id_interprete[0][0],id_genero[0][0],cant_temas,id_discografica[0][0],id_formato[0][0],fec_lanzamiento,precio,cantidad,caratula)
        self.con.insertar_album(nuevoAlbum)
                

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

#-----------------Carga de ComboBox-------------------------
    def interpretes(self):
        con = mo.Conectar()
        tuplas = con.listar_interpretes()
        lista = [tup[1] + ' ' + tup[2] for tup in tuplas]
        return lista

    def generos(self):
        con = mo.Conectar()
        tuplas = con.listar_genero()
        lista = [tup[1] for tup in tuplas]
        return lista

    def discograficas(self):
        con = mo.Conectar()
        tuplas = con.listar_discografica()
        lista = [tup[1] for tup in tuplas]
        return lista

    def formatos(self):
        con = mo.Conectar()
        tuplas = con.listar_formato()
        lista = [tup[1] for tup in tuplas]
        return lista

    def albumes(self):
        con = mo.Conectar()
        tuplas = con.listar_album()
        lista = [tup[2] for tup in tuplas]
        return lista

#-----------------fin-------------------------

    def cargar_interprete(self, nombre, apellido, nacionalidad, foto):
        con = mo.Conectar()
        interprete = mo.Interprete(0, nombre, apellido, nacionalidad, foto)
        self.con.insertar_interprete(interprete)

    def cargar_formato(self, nombre):
        con = mo.Conectar()
        formato = mo.Formato(0, nombre)
        self.con.insertar_formato(formato)

    def cargar_tema(self, nombre, duracion, autor, compositor, album, interprete):
        con = mo.Conectar()
        id_album = con.id_album_por_nombre(album)
        nombre_interprete = interprete.split(maxsplit=1)
        id_interprete = con.id_interprete_por_nombre(nombre_interprete[0], nombre_interprete[1])
        print(id_album, '###############', id_interprete)
        tema = mo.Tema(0,nombre, duracion, autor, compositor, id_album[0][0], id_interprete[0][0])
        self.con.insertar_tema(tema)

    def busqueda_por_titulo_tema(self, nombre):
        con = mo.Conectar()
        tema = con.busqueda_por_titulo_tema(nombre)
        table = self.principal.tabla_buscar_tema
        table.setRowCount(0)
        print(tema)
        for fila, album in enumerate(tema):
            table.insertRow(fila)
            for columna, data in enumerate(album):
                table.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(data)))
