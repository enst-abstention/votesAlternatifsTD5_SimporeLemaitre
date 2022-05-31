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
        Dialog.resize(426, 552)
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(120, 90, 171, 16))
        self.labelResult.setObjectName("labelResult")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 190, 191, 20))
        self.label.setObjectName("label")
        self.textEditResult = QtWidgets.QTextEdit(Dialog)
        self.textEditResult.setGeometry(QtCore.QRect(73, 260, 281, 87))
        self.textEditResult.setObjectName("textEditResult")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelResult.setText(_translate("Dialog", "RESULTATS DES ELECTIONS"))
        self.label.setText(_translate("Dialog", "Le vainqueur de l\'élection est :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
