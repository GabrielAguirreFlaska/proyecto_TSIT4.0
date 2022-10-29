

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
        self.con = mo.Conectar()
        self.nuevo = nuevo_album


    def crear_nuevo_album(self, cod_album, nombre, interprete, genero,cant_temas, discografica, formato, fec_lanzamiento, precio, cantidad, caratula, vista):
        con = mo.Conectar()
        nombre_apellido = interprete.split()
        id_interprete = con.id_interprete_por_nombre(nombre_apellido[0], nombre_apellido[1])
        id_genero = con.id_genero_por_nombre(genero)
        id_discografica = con.id_discografica_por_nombre(discografica)
        id_formato = con.id_formato_por_nombre(formato)
        nuevoAlbum = mo.Album(0,cod_album,nombre,id_interprete[0][0],id_genero[0][0],cant_temas,id_discografica[0][0],id_formato[0][0],fec_lanzamiento,precio,cantidad,caratula)
        self.con.insertar_album(nuevoAlbum)
        vista.hide()

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



