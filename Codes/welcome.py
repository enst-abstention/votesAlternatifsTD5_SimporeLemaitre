# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\welcome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 797)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(129, 420, 351, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonSetUp = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonSetUp.setObjectName("buttonSetUp")
        self.horizontalLayout.addWidget(self.buttonSetUp)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(129, 500, 351, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonResults = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.buttonResults.setObjectName("buttonResults")
        self.horizontalLayout_2.addWidget(self.buttonResults)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 360, 351, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonVote = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonVote.setObjectName("buttonVote")
        self.verticalLayout.addWidget(self.buttonVote)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonSetUp.setText(_translate("MainWindow", "CREER UNE ELECTION"))
        self.buttonResults.setText(_translate("MainWindow", "AFFICHER LES RESULTATS"))
        self.buttonVote.setText(_translate("MainWindow", "VOTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
