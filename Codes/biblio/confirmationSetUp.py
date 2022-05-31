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
        Dialog.resize(400, 300)
        self.labelConfirmation = QtWidgets.QLabel(Dialog)
        self.labelConfirmation.setGeometry(QtCore.QRect(120, 120, 151, 20))
        self.labelConfirmation.setObjectName("labelConfirmation")
        self.buttonBackMain = QtWidgets.QPushButton(Dialog)
        self.buttonBackMain.setGeometry(QtCore.QRect(260, 220, 93, 28))
        self.buttonBackMain.setObjectName("buttonBackMain")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelConfirmation.setText(_translate("Dialog", "L\'election a bien été créée"))
        self.buttonBackMain.setText(_translate("Dialog", "CONTINUER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
