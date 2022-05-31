# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\confirmationVote.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(413, 593)
        Dialog.setModal(True)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 10, 410, 590))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(470, 430, 221, 20))
        self.label_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);\n"
"color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(390, 660, 93, 28))
        self.pushButton.setStyleSheet("font: 8pt \"Kristen ITC\";\n"
"color: rgb(188, 0, 108);\n"
"font: 8pt \"Kristen ITC\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 320, 301, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonBack = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonBack.setObjectName("buttonBack")
        self.horizontalLayout.addWidget(self.buttonBack)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonSubmit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonSubmit.setObjectName("buttonSubmit")
        self.horizontalLayout.addWidget(self.buttonSubmit)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 70, 421, 101))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Valider"))
        self.buttonBack.setText(_translate("Dialog", "ANNULER"))
        self.buttonSubmit.setText(_translate("Dialog", "VALIDER"))
        self.label.setText(_translate("Dialog", "Cliquez sur Valider pour confirmer vos votes.\n"
"Attention, une fois validés, les votes ne pourront plus être modifiés."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
