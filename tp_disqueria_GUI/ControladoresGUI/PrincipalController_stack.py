
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


import tp_disqueria_GUI.modelo as mo



class PrincipalController():

    def __init__(self, principal):
        self.con = mo.Conectar()
        self.principal = principal

    def listar_album(self):
        con = mo.Conectar()
        listado = con.consulta_album()
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

    

    def crear_nuevo_album(self, cod_album, nombre, interprete, genero,cant_temas, discografica, formato, fec_lanzamiento = 0, precio = 0, cantidad = 0, caratula = 'n'):
        self.con = mo.Conectar()       
        id_interprete = self.con.id_interprete_por_nombre(interprete)
        id_genero = self.con.id_genero_por_nombre(genero)
        id_discografica = self.con.id_discografica_por_nombre(discografica)
        id_formato = self.con.id_formato_por_nombre(formato)
        nuevoAlbum = mo.Album(0,cod_album,nombre,id_interprete[0][0],id_genero[0][0],cant_temas,id_discografica[0][0],id_formato[0][0],fec_lanzamiento,precio,cantidad,caratula)
        self.con.insertar_album(nuevoAlbum)
        msg = QMessageBox()
        msg.setWindowTitle('Disqueria')
        msg.setText('¡Album creado exitosamente!')
        msg.exec_()
                

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
        self.con = mo.Conectar()
        interprete = mo.Interprete(0, nombre, apellido, nacionalidad, foto)
        self.con.insertar_interprete(interprete)

    def cargar_formato(self, nombre):
        self.con = mo.Conectar()
        formato = mo.Formato(0, nombre)
        self.con.insertar_formato(formato)

    def cargar_tema(self, nombre, duracion, autor, compositor, album, interprete):
        self.con = mo.Conectar()
        id_album = self.con.id_album_por_nombre(album)
       
        id_interprete = self.con.id_interprete_por_nombre(interprete)
       
        tema = mo.Tema(0,nombre, duracion, autor, compositor, id_album[0][0], id_interprete[0][0])
        self.con.insertar_tema(tema)
        msg = QMessageBox()
        msg.setWindowTitle('Disqueria')
        msg.setText('Tema creado exitosamente!')
        msg.exec_()

    def busqueda_por_titulo_tema(self, nombre):
        self.con = mo.Conectar()
        tema = self.con.busqueda_por_titulo_tema(nombre)
        table = self.principal.tabla_buscar_tema
        table.setRowCount(0)
        for fila, album in enumerate(tema):
            table.insertRow(fila)
            for columna, data in enumerate(album):
                table.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(data)))

    def buscar_inter_por_id(self, id_i):
        self.con = mo.Conectar()
        interprete = self.con.consulta_inter_por_id(id_i)
        return interprete

    def comboBox_crear_tema(self):
        self.principal.cB_id_interprete.clear()
        self.principal.cB_id_album.clear()

        self.principal.cB_id_interprete.addItems(self.interpretes())
        self.principal.cB_id_album.addItems(self.albumes())

    def comboBox_crear_album(self):
        self.principal.comboBox_interprete_2.clear()
        self.principal.comboBox_genero_2.clear()
        self.principal.comboBox_discografica_2.clear()
        self.principal.comboBox_formato_2.clear()

        self.principal.comboBox_interprete_2.addItems(self.interpretes())
        self.principal.comboBox_genero_2.addItems(self.generos())
        self.principal.comboBox_discografica_2.addItems(self.discograficas())
        self.principal.comboBox_formato_2.addItems(self.formatos())

    def comboBox_modificar(self):
        self.principal.comboBox.clear()
        self.principal.comboBox_interprete_4.clear()
        self.principal.comboBox_genero_4.clear()
        self.principal.comboBox_discografica_4.clear()
        self.principal.comboBox_formato_4.clear()

        self.principal.comboBox.addItems(self.albumes())
        self.principal.comboBox_interprete_4.addItems(self.interpretes())
        self.principal.comboBox_genero_4.addItems(self.generos())
        self.principal.comboBox_discografica_4.addItems(self.discograficas())
        self.principal.comboBox_formato_4.addItems(self.formatos())


    def buscar_album_por_nombre_gui_modif(self, nombre):
        con = mo.Conectar()
        albums = con.consulta_album_por_nombre(nombre)[0]
        inter = con.consulta_inter_por_id(albums[3])[0]
        #inter = self.buscar_inter_por_id(albums[3])
        gen = con.consulta_genero_por_id(albums[4])[0]
        disc = con.consulta_discografica_por_id(albums[6])[0]
        form = con.consulta_formato_por_id(albums[7])[0]


        #----LLeno los cb con los datos del album seleccionado
        self.principal.comboBox_interprete_4.setCurrentText(inter[1]+' '+inter[2])
        self.principal.comboBox_genero_4.setCurrentText(gen[1])
        self.principal.comboBox_discografica_4.setCurrentText(disc[1])
        self.principal.comboBox_formato_4.setCurrentText(form[1])
        #----LLeno los  Line edit con los datos del album seleccionado
        self.principal.input_Nombre.setText(str(albums[2]))
        self.principal.input_cantidaddetemas_4.setText(str(albums[5]))
        self.principal.input_fechadelanzamiento_4.setText(str(albums[8]))
        self.principal.input_precio_4.setText(str(albums[9]))
        self.principal.input_stock_4.setText(str(albums[10]))
        self.principal.input_caratula_4.setText(str(albums[11]))
        self.principal.input_codigo_4.setText(str(albums[1]))

        
    def actualizar_album(self):
        con = mo.Conectar()
        albums = con.consulta_album_por_nombre(self.principal.comboBox.currentText())[0][0]
        #id_a = con.consulta_inter_por_id(albums[3])[0]
        codigo = self.principal.input_codigo_4.text()
        nombre = self.principal.input_Nombre.text()
        nombre_apellido = (self.principal.comboBox_interprete_4.currentText())
        id_inter = con.id_interprete_por_nombre(nombre_apellido)[0][0]
        id_genero = con.id_genero_por_nombre(self.principal.comboBox_genero_4.currentText())[0][0]
        temas = self.principal.input_cantidaddetemas_4.text()
        discog = con.id_discografica_por_nombre(self.principal.comboBox_discografica_4.currentText())[0][0]
        formato = con.id_formato_por_nombre(self.principal.comboBox_formato_4.currentText())[0][0]
        fecha = self.principal.input_fechadelanzamiento_4.text()
        if fecha == 'None':
            fecha = '0000-00-00'
        precio = self.principal.input_precio_4.text()
        stock = self.principal.input_stock_4.text()
        caratula = self.principal.input_caratula_4.text()
        
        con.modificar_album(albums, codigo, nombre, id_inter, id_genero, temas, discog, formato, fecha, precio, stock, caratula)
        
        msg = QMessageBox()
        msg.setWindowTitle('Disqueria')
        msg.setText('¡Album Actualizado exitosamente!')
        msg.exec_()
        # self.principal.comboBox.clear()
        # self.comboBox_modificar()

    def abrir_eliminar(self, Ui_Eliminar):
        self.principal.Form = QtWidgets.QWidget()
        self.principal.ui = Ui_Eliminar()
        self.principal.ui.setupUi(self.principal.Form)
        self.principal.Form.show()