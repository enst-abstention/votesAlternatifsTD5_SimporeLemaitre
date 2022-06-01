# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\results.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 748)
        Dialog.setStyleSheet("background-color: rgb(110, 192, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 90, 541, 71))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(93, 93, 93);\n"
"background-color: rgb(113, 113, 113);\n"
"font: 8pt \"Kristen ITC\";\n"
"font: 20pt \"Kristen ITC\";\n"
"")
        self.label.setObjectName("label")
        self.textEditResults = QtWidgets.QTextEdit(Dialog)
        self.textEditResults.setGeometry(QtCore.QRect(103, 360, 421, 87))
        self.textEditResults.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEditResults.setObjectName("textEditResults")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(103, 340, 421, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "RESULTATS DES ELECTIONS"))
        self.lineEdit.setText(_translate("Dialog", "Le vainqueur de l\'élection est :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
