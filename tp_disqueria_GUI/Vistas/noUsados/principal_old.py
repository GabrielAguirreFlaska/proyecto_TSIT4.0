# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
print('###########################')
print(myDir)
print('###########################')


from tp_disqueria_GUI.ControladoresGUI.PrincipalController import PrincipalController
from tp_disqueria_GUI.Vistas.crearalbumnuevo_v2 import Ui_CrearProducto
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principal(object):

    def __init__(self):
        self.principal_controller = PrincipalController(self)


    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(1431, 711)
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 10, 1291, 651))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.tabla_principal = QtWidgets.QTableWidget(self.widget)
        self.tabla_principal.setRowCount(10)
        self.tabla_principal.setObjectName("tabla_principal")
        self.tabla_principal.setColumnCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_principal.setHorizontalHeaderItem(9, item)
        self.gridLayout.addWidget(self.tabla_principal, 1, 0, 1, 5)
        self.boton_listar = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.boton_listar.setFont(font)
        self.boton_listar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_listar.setObjectName("boton_listar")
        self.gridLayout.addWidget(self.boton_listar, 2, 0, 1, 1)
        self.boton_actualizar = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.boton_actualizar.setFont(font)
        self.boton_actualizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_actualizar.setObjectName("boton_actualizar")
        self.gridLayout.addWidget(self.boton_actualizar, 2, 1, 1, 1)
        self.boton_crear = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.boton_crear.setFont(font)
        self.boton_crear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_crear.setObjectName("boton_crear")
        self.gridLayout.addWidget(self.boton_crear, 2, 2, 1, 1)
        self.boton_seleccionar = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.boton_seleccionar.setFont(font)
        self.boton_seleccionar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_seleccionar.setObjectName("boton_seleccionar")
        self.gridLayout.addWidget(self.boton_seleccionar, 2, 3, 1, 1)
        self.boton_eliminar = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.boton_eliminar.setFont(font)
        self.boton_eliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_eliminar.setObjectName("boton_eliminar")
        self.gridLayout.addWidget(self.boton_eliminar, 2, 4, 1, 1)
        Principal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Principal)
        self.statusbar.setObjectName("statusbar")
        Principal.setStatusBar(self.statusbar)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)


        #--------------------Events--------------------------------------
        self.l = self.boton_listar.clicked.connect(lambda:self.principal_controller.listProducts())   #ok
        self.c = self.boton_crear.clicked.connect(lambda:self.principal_controller.abrir_crear_album(Ui_CrearProducto))
        # self.r = self.btn_read.clicked.connect(lambda:self.principal_controller.showProduct())
        # self.u = self.boton_actualizar.clicked.connect(lambda:self.principal_controller.updateProduct())
        self.d = self.boton_eliminar.clicked.connect(lambda:self.principal_controller.deleteProduct())  #ok
        #--------------------End Events---------------------------------


    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "MainWindow"))
        self.label.setText(_translate("Principal", "??lbum Principal"))
        item = self.tabla_principal.horizontalHeaderItem(0)
        item.setText(_translate("Principal", "id_album"))
        item = self.tabla_principal.horizontalHeaderItem(1)
        item.setText(_translate("Principal", "cod_album"))
        item = self.tabla_principal.horizontalHeaderItem(2)
        item.setText(_translate("Principal", "NOMBRE"))
        item = self.tabla_principal.horizontalHeaderItem(3)
        item.setText(_translate("Principal", "id_interprete"))
        item = self.tabla_principal.horizontalHeaderItem(4)
        item.setText(_translate("Principal", "id_genero"))
        item = self.tabla_principal.horizontalHeaderItem(5)
        item.setText(_translate("Principal", "cant_temas"))
        item = self.tabla_principal.horizontalHeaderItem(6)
        item.setText(_translate("Principal", "id_discografia"))
        item = self.tabla_principal.horizontalHeaderItem(7)
        item.setText(_translate("Principal", "id_formato"))
        item = self.tabla_principal.horizontalHeaderItem(8)
        item.setText(_translate("Principal", "fecha de lanzamiento"))
        item = self.tabla_principal.horizontalHeaderItem(9)
        item.setText(_translate("Principal", "precio"))
        self.boton_listar.setText(_translate("Principal", "Listar"))
        self.boton_actualizar.setText(_translate("Principal", "Actualizar"))
        self.boton_crear.setText(_translate("Principal", "Crear"))
        self.boton_seleccionar.setText(_translate("Principal", "Seleccionar"))
        self.boton_eliminar.setText(_translate("Principal", "Eliminar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_Principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
