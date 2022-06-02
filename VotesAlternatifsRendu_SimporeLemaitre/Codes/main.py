import functools

from PyQt5 import QtCore, QtGui, QtWidgets
from welcome import Ui_MainWindow
from biblio.setUp import Ui_Dialog as setUpDialog
from biblio.confirmationSetUp import Ui_Dialog as confirmationSetUpDialog
from biblio.signInVote import Ui_Dialog as signInVoteDialog
from biblio.condorcetBulletin import Ui_Dialog as condorcetBulletinDialog
from biblio.jugMajBulletin import Ui_Dialog as jugMajBulletinDialog
from biblio.confirmationVote import Ui_Dialog as confirmationVoteDialog
from biblio.results import Ui_Dialog as resultsDialog

from biblio.vote.electionsBDD import Election, Bulletin
from biblio.vote.scrutins import Condorcet, JugementMajoritaire
from biblio.vote import scrutins as scr

import sys

## Variables d'application
currentElection = False
currentBulletin = False
appreciation = 0

def backMain1():
    confirmationSetUp.close()
    MainWindow.show()

def backMain2():
    global currentElection
    currentElection.remplissage_urne(currentBulletin)
    confirmationVote.close()
    MainWindow.show()


def dispSetUp():
    MainWindow.close()
    setUp.show()

def dispConfirmationSetUp():
    global currentElection
    nom = uiSetUp.lineEditNameVote.text()
    dates = (uiSetUp.dateTimeEditStart.dateTime().toPyDateTime(),uiSetUp.dateTimeEditEnd.dateTime().toPyDateTime())
    electionBDD = uiSetUp.lineEditNameBDD.text()
    mode = uiSetUp.comboBoxSystemVote.currentText()
    currentElection = Election(nom, dates, electionBDD, mode)
    setUp.close()
    confirmationSetUp.show()


def dispSignInVote():
    MainWindow.close()
    if currentElection :
        signInVote.show()
    else :
        print("Aucun vote n'est en cours")


def dispBulletin():
    global currentBulletin
    idElec = int(uiSignInVote.lineEditIdElec.text())
    mdp = uiSignInVote.lineEditMdp.text()
    currentBulletin = Bulletin(currentElection, idElec, mdp)
    signInVote.close()
    if isinstance(currentElection.scrutin, Condorcet):
        dispCondorcetBulletin()

    elif isinstance(currentElection.scrutin, JugementMajoritaire) :
        dispJugMajBulletin()

def dispCondorcetBulletin():
    if not currentElection.urne :
        for i in range(1,len(currentElection.candidats) + 1) :
            instruction = "uiCondorcetBulletin.labelC{}.setText(currentElection.candidats[i-1])".format(i)
            exec(instruction)
            instruction = "uiCondorcetBulletin.comboBoxC{}.addItems(currentElection.scrutin.votesautorises)".format(i)
            exec(instruction)
    condorcetBulletin.show()

def dispJugMajBulletin():
    if not currentElection.urne :
        for i in range(1,len(currentElection.candidats) + 1) :
            instruction = "uiJugMajBulletin.labelC{}.setText(currentElection.candidats[i-1])".format(i)
            exec(instruction)
            instruction2 = "uiJugMajBulletin.comboBoxC{}.addItems(currentElection.scrutin.votesautorises)".format(i)
            exec(instruction2)
    jugMajBulletin.show()


def condorcetAVoter():
    classement = []
    for i in range(len(currentElection.candidats)):
        instruction = "classement.append(int(uiCondorcetBulletin.comboBoxC{}.currentText()))".format(i+1)
        exec(instruction)
        currentBulletin.completeBulletin(currentElection.candidats[i], classement[i])
    condorcetBulletin.hide()
    confirmationVote.show()

def jugMajAVoter():
    appreciation = []
    for i in range(len(currentElection.candidats)):
        instruction = "appreciation.append(uiJugMajBulletin.comboBoxC{}.currentText())".format(i+1)
        exec(instruction)
        currentBulletin.completeBulletin(currentElection.candidats[i], appreciation[i])
    jugMajBulletin.hide()
    confirmationVote.show()

def backBulletin():
    confirmationVote.setModal(False)
    confirmationVote.close()
    condorcetBulletin.show()


def dispResults():
    if currentElection and currentElection.urne :
        vainqueur = currentElection.depouillement()
        uiResults.textEditResults.setText(vainqueur)
        results.show()
    elif currentElection :
        print("Personne n'a voté, l'urne est vide !")
    else :
        print("Aucun vote n'est en cours !")


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.setStyleSheet("""
    .QMainWindow{ 
    background-image: url(biblio/ui/img/urneess.jpg);
    background-position: center;
    }   
    """)

setUp = QtWidgets.QDialog()
setUp.setStyleSheet("""
    .QDialog{
    background-image: url(biblio/ui/img/urneess.jpg);
    background-position: center;
    }
    """)
uiSetUp = setUpDialog()
uiSetUp.setupUi(setUp)

confirmationSetUp = QtWidgets.QDialog()
confirmationSetUp.setStyleSheet(""".QDialog{
    background-image: url(biblio/ui/img/validess.jpg);
    background-position: center;
    }
    """)
uiConfirmationSetUp = confirmationSetUpDialog()
uiConfirmationSetUp.setupUi(confirmationSetUp)

signInVote = QtWidgets.QDialog()
signInVote.setStyleSheet(""".QDialog{
    background-image: url(biblio/ui/img/urneess.jpg);
    background-position: center;
    }
    """)
uiSignInVote = signInVoteDialog()
uiSignInVote.setupUi(signInVote)

condorcetBulletin = QtWidgets.QDialog()
condorcetBulletin.setStyleSheet(""".QDialog{
    background-image: url(biblio/ui/img/urnnne.jpg);
    background-position: center;
    }
    """)
uiCondorcetBulletin = condorcetBulletinDialog()
uiCondorcetBulletin.setupUi(condorcetBulletin)

jugMajBulletin = QtWidgets.QDialog()
jugMajBulletin.setStyleSheet(""".QDialog{
    background-image: url(biblio/ui/img/urnnne.jpg);
    background-position: center;
    }
    """)
uiJugMajBulletin = jugMajBulletinDialog()
uiJugMajBulletin.setupUi(jugMajBulletin)

confirmationVote = QtWidgets.QDialog()
confirmationVote.setStyleSheet(""".QDialog{
    background-image: url(biblio/ui/img/validess.jpg);
    background-position: center;
    }
    """)
uiConfirmationVote = confirmationVoteDialog()
uiConfirmationVote.setupUi(confirmationVote)

results = QtWidgets.QDialog()
results.setStyleSheet(""".QDialog{
    background-image: url(biblio/ui/img/validess.jpg);
    background-position: center;
    }
    """)
uiResults = resultsDialog()
uiResults.setupUi(results)

##Slots et signaux
ui.buttonSetUp.clicked.connect(dispSetUp)
ui.buttonVote.clicked.connect(dispSignInVote)
ui.buttonResults.clicked.connect(dispResults)

uiSetUp.buttonSetUp.clicked.connect(dispConfirmationSetUp)

uiSignInVote.buttonBulletin.clicked.connect(dispBulletin)


uiCondorcetBulletin.buttonBack.clicked.connect(backMain1)
uiCondorcetBulletin.buttonAVoter.clicked.connect(condorcetAVoter)
uiJugMajBulletin.buttonBack.clicked.connect(backMain1)
uiJugMajBulletin.buttonAVoter.clicked.connect(jugMajAVoter)

uiConfirmationSetUp.buttonBackMain.clicked.connect(backMain1)

uiConfirmationVote.buttonBack.clicked.connect(backBulletin)
uiConfirmationVote.buttonSubmit.clicked.connect(backMain2)

MainWindow.show()
sys.exit(app.exec_())
