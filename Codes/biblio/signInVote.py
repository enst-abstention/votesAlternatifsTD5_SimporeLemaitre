# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signInVote.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(371, 590)
        Dialog.setModal(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 110, 91, 51))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 281, 20))
        self.label_2.setObjectName("label_2")
        self.labelIdElex = QtWidgets.QLabel(Dialog)
        self.labelIdElex.setGeometry(QtCore.QRect(60, 230, 61, 16))
        self.labelIdElex.setObjectName("labelIdElex")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(59, 250, 301, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditIdElec = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditIdElec.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.lineEditIdElec.setObjectName("lineEditIdElec")
        self.horizontalLayout.addWidget(self.lineEditIdElec)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(60, 340, 301, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditMdp = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEditMdp.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEditMdp.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEditMdp.setObjectName("lineEditMdp")
        self.horizontalLayout_2.addWidget(self.lineEditMdp)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 320, 81, 16))
        self.label_6.setObjectName("label_6")
        self.buttonBulletin = QtWidgets.QPushButton(Dialog)
        self.buttonBulletin.setGeometry(QtCore.QRect(260, 470, 93, 28))
        self.buttonBulletin.setObjectName("buttonBulletin")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "          VOTER"))
        self.label_2.setText(_translate("Dialog", "VEUILLEZ REMPLIR VOS IDENTIFIANTS DE VOTE"))
        self.labelIdElex.setText(_translate("Dialog", "Identifiant"))
        self.label_6.setText(_translate("Dialog", "Mot de passe"))
        self.buttonBulletin.setText(_translate("Dialog", "CONTINUER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
