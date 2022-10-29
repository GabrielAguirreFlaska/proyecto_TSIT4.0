# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\crearalbumnuevo_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from tp_disqueria_GUI.ControladoresGUI.CrearAlbumNuevoController import CrearNuevoAlbum
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CrearProducto(object):

    def __init__(self):
        self.crear_nuevo_album = CrearNuevoAlbum(self)

    def setupUi(self, CrearProducto):
        CrearProducto.setObjectName("CrearProducto")
        CrearProducto.resize(552, 491)
        self.layoutWidget = QtWidgets.QWidget(CrearProducto)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 10, 441, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 11, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 2)
        self.input_caratula = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.input_caratula.setFont(font)
        self.input_caratula.setObjectName("input_caratula")
        self.gridLayout.addWidget(self.input_caratula, 15, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.input_precio = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.input_precio.setFont(font)
        self.input_precio.setObjectName("input_precio")
        self.gridLayout.addWidget(self.input_precio, 14, 2, 1, 1)
        self.comboBox_genero = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_genero.setObjectName("comboBox_genero")
        self.gridLayout.addWidget(self.comboBox_genero, 7, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.comboBox_dicografica = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_dicografica.setMouseTracking(False)
        self.comboBox_dicografica.setObjectName("comboBox_dicografica")
        self.gridLayout.addWidget(self.comboBox_dicografica, 11, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 12, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.input_fechadelanzamiento = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.input_fechadelanzamiento.setFont(font)
        self.input_fechadelanzamiento.setObjectName("input_fechadelanzamiento")
        self.gridLayout.addWidget(self.input_fechadelanzamiento, 13, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 13, 0, 1, 2)
        self.comboBox_interprete = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_interprete.setObjectName("comboBox_interprete")
        self.gridLayout.addWidget(self.comboBox_interprete, 6, 2, 1, 1)
        self.comboBox_formato = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_formato.setMouseTracking(False)
        self.comboBox_formato.setObjectName("comboBox_formato")
        self.gridLayout.addWidget(self.comboBox_formato, 12, 2, 1, 1)
        self.input_cantidaddetemas = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.input_cantidaddetemas.setFont(font)
        self.input_cantidaddetemas.setObjectName("input_cantidaddetemas")
        self.gridLayout.addWidget(self.input_cantidaddetemas, 8, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 15, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 14, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.input_codigo = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.input_codigo.setFont(font)
        self.input_codigo.setText("")
        self.input_codigo.setObjectName("input_codigo")
        self.gridLayout.addWidget(self.input_codigo, 1, 2, 1, 1)
        self.input_nombre = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        self.input_nombre.setFont(font)
        self.input_nombre.setText("")
        self.input_nombre.setObjectName("input_nombre")
        self.gridLayout.addWidget(self.input_nombre, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.boton_crear = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.boton_crear.setFont(font)
        self.boton_crear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_crear.setObjectName("boton_crear")
        self.verticalLayout.addWidget(self.boton_crear)

        self.retranslateUi(CrearProducto)
        QtCore.QMetaObject.connectSlotsByName(CrearProducto)


        #--------------------Events--------------------------------------
        self.x = self.boton_crear.clicked.connect(lambda:self.crear_nuevo_album.crear_nuevo_album(self.input_codigo.text(),self.input_nombre.text(),self.comboBox_interprete ,self.comboBox_genero, self.input_cantidaddetemas.text(), self.comboBox_dicografica, self.comboBox_formato, self.input_fechadelanzamiento.text(), self.input_precio.text(), 10, self.input_caratula.text(),CrearProducto))
        #--------------------End Events---------------------------------

    def retranslateUi(self, CrearProducto):
        _translate = QtCore.QCoreApplication.translate
        CrearProducto.setWindowTitle(_translate("CrearProducto", "Form"))
        self.label_8.setText(_translate("CrearProducto", "ID discográfica:"))
        self.label_9.setText(_translate("CrearProducto", "Cantidad de temas:"))
        self.input_caratula.setPlaceholderText(_translate("CrearProducto", "Carátula"))
        self.label.setText(_translate("CrearProducto", "Crear álbum nuevo"))
        self.input_precio.setPlaceholderText(_translate("CrearProducto", "Precio"))
        self.label_5.setText(_translate("CrearProducto", "ID género:"))
        self.label_11.setText(_translate("CrearProducto", "Formato"))
        self.label_2.setText(_translate("CrearProducto", "Nombre:"))
        self.label_4.setText(_translate("CrearProducto", "ID intérprete:"))
        self.input_fechadelanzamiento.setPlaceholderText(_translate("CrearProducto", "Fecha de lanzamiento"))
        self.label_7.setText(_translate("CrearProducto", "Fecha de lanzamiento:"))
        self.input_cantidaddetemas.setPlaceholderText(_translate("CrearProducto", "Cantidad de temas"))
        self.label_6.setText(_translate("CrearProducto", "Carátula:"))
        self.label_10.setText(_translate("CrearProducto", "Precio:"))
        self.label_3.setText(_translate("CrearProducto", "Código:"))
        self.input_codigo.setPlaceholderText(_translate("CrearProducto", "Código"))
        self.input_nombre.setPlaceholderText(_translate("CrearProducto", "Nombre"))
        self.boton_crear.setText(_translate("CrearProducto", "Crear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CrearProducto = QtWidgets.QWidget()
    ui = Ui_CrearProducto()
    ui.setupUi(CrearProducto)
    CrearProducto.show()
    sys.exit(app.exec_())