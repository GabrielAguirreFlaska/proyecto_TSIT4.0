# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\eliminar.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets

from tp_disqueria_GUI.ControladoresGUI.EliminarController import EliminarController


class Ui_Eliminar(object):

    def __init__(self):
        self.eliminar_controller = EliminarController(self)

    def setupUi(self, Eliminar):
        Eliminar.setObjectName("Eliminar")
        Eliminar.resize(480, 620)
        Eliminar.setStyleSheet("QFrame { \n"
"    background-color: rgb(70, 70, 80);\n"
"    border-radius: 10px;}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(100, 200, 200);\n"
"border-radius: 8px;\n"
"font: 20 12pt;\n"
"padding: 8px}\n"
"\n"
"QPushButton:hover{\n"
"background-color:  rgb(70, 100, 250);\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover#btn_eliminar{\n"
"background-color: rgba(255, 97, 97, 147);\n"
"border-radius: 10px;}\n"
"\n"
"QLabel { \n"
"    background-color: rgb(70, 70, 80);\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    font-weight: bold}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Eliminar)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(Eliminar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color: rgb(231, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)
        self.tabla = QtWidgets.QTableWidget(Eliminar)
        self.tabla.setWordWrap(True)
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(3)
        self.tabla.setAlternatingRowColors(True)
        self.tabla.setStyleSheet("alternate-background-color: rgb(100, 200, 200);background-color: rgb(200, 200, 200);");
        self.tabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(2, item)
        self.tabla.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla.horizontalHeader().setDefaultSectionSize(150)
        self.gridLayout.addWidget(self.tabla, 1, 2, 1, 1)
        self.frame = QtWidgets.QFrame(Eliminar)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_eliminar = QtWidgets.QPushButton(self.frame)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout.addWidget(self.btn_eliminar)
        self.gridLayout.addWidget(self.frame, 2, 2, 1, 1)

        self.retranslateUi(Eliminar)
        QtCore.QMetaObject.connectSlotsByName(Eliminar)

        self.eliminar_controller.listar_album()
        self.e = self.btn_eliminar.clicked.connect(lambda:self.eliminar_controller.eliminar_album())

    def retranslateUi(self, Eliminar):
        _translate = QtCore.QCoreApplication.translate
        Eliminar.setWindowTitle(_translate("Eliminar", "Form"))
        self.label.setText(_translate("Eliminar", "Seleccione el Codigo del album a eliminar"))
        item = self.tabla.horizontalHeaderItem(0)
        item.setText(_translate("Eliminar", "ID"))
        item = self.tabla.horizontalHeaderItem(1)
        item.setText(_translate("Eliminar", "Codigo"))
        item = self.tabla.horizontalHeaderItem(2)
        item.setText(_translate("Eliminar", "Nombre"))
        self.btn_eliminar.setText(_translate("Eliminar", "ELIMINAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Eliminar = QtWidgets.QWidget()
    ui = Ui_Eliminar()
    ui.setupUi(Eliminar)
    Eliminar.show()
    sys.exit(app.exec_())
