# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\confirmationSetUp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 748)
        Dialog.setStyleSheet("background-image: url(:/4/validess.jpg);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 220, 521, 61))
        self.label.setStyleSheet("color: rgb(0, 85, 0);\n"
"font: 8pt \"Kristen ITC\";\n"
"font: 24pt \"Kristen ITC\";")
        self.label.setObjectName("label")
        self.buttonBackMain = QtWidgets.QPushButton(Dialog)
        self.buttonBackMain.setGeometry(QtCore.QRect(480, 430, 93, 28))
        self.buttonBackMain.setObjectName("buttonBackMain")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "L\'election a bien été créer"))
        self.buttonBackMain.setText(_translate("Dialog", "CONTINUER"))
import 4_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
