# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\setUp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 748)
        Dialog.setStyleSheet("background-image: url(:/newPrefix/IHM/urneess.jpg);\n"
"background-image: url(:/newPrefix/urnnne.jpg)")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 70, 521, 51))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(93, 93, 93);\n"
"background-color: rgb(113, 113, 113);\n"
"font: 8pt \"Kristen ITC\";\n"
"font: 24pt \"Kristen ITC\";\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(49, 190, 451, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEditNameVote = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditNameVote.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEditNameVote.setObjectName("lineEditNameVote")
        self.horizontalLayout.addWidget(self.lineEditNameVote)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 290, 451, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.dateTimeEditStart = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget_2)
        self.dateTimeEditStart.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 5, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEditStart.setDate(QtCore.QDate(2022, 5, 1))
        self.dateTimeEditStart.setObjectName("dateTimeEditStart")
        self.horizontalLayout_2.addWidget(self.dateTimeEditStart)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.dateTimeEditEnd = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget_2)
        self.dateTimeEditEnd.setDate(QtCore.QDate(2022, 7, 1))
        self.dateTimeEditEnd.setObjectName("dateTimeEditEnd")
        self.horizontalLayout_2.addWidget(self.dateTimeEditEnd)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 370, 451, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        spacerItem3 = QtWidgets.QSpacerItem(18, 46, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_3.addWidget(self.checkBox_3)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(50, 520, 451, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        spacerItem4 = QtWidgets.QSpacerItem(28, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.comboBoxSystemVote = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.comboBoxSystemVote.setObjectName("comboBoxSystemVote")
        self.comboBoxSystemVote.addItem("")
        self.comboBoxSystemVote.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBoxSystemVote)
        self.buttonSetUp = QtWidgets.QPushButton(Dialog)
        self.buttonSetUp.setGeometry(QtCore.QRect(410, 580, 141, 28))
        self.buttonSetUp.setObjectName("buttonSetUp")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(50, 440, 451, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.lineEditNameVote_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEditNameVote_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEditNameVote_2.setObjectName("lineEditNameVote_2")
        self.horizontalLayout_5.addWidget(self.lineEditNameVote_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CREER UNE ELECTION"))
        self.label_4.setText(_translate("Dialog", "NOM DE L\'ELECTION"))
        self.label_2.setText(_translate("Dialog", "DEBUT"))
        self.label_3.setText(_translate("Dialog", "FIN"))
        self.label_5.setText(_translate("Dialog", "Disposer vous d\'une base de donnée?"))
        self.checkBox.setText(_translate("Dialog", "NON"))
        self.checkBox_3.setText(_translate("Dialog", "OUI"))
        self.label_6.setText(_translate("Dialog", "Mode de scrutin"))
        self.comboBoxSystemVote.setItemText(0, _translate("Dialog", "CONDORCET"))
        self.comboBoxSystemVote.setItemText(1, _translate("Dialog", "JUGEMENTMAJORITAIRE"))
        self.buttonSetUp.setText(_translate("Dialog", "CREER L\'ELECTION"))
        self.label_7.setText(_translate("Dialog", "Nom de la BDD"))
import 2_rc
import 3_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
