import numpy as np
from abc import ABCMeta, abstractmethod


class Scrutin(metaclass=ABCMeta):
    """
    Auteur : Sheick Simpore

    """

    def __init__(self, candidats):
        self.candidats = candidats

    @abstractmethod
    def resultat(self):
        """On sera obligé de définir une méthode 'resultat' pour chaque classe"""
        pass


class Condorcet(Scrutin):

    def __init__(self, candidats):
        Scrutin.__init__(self, candidats)
        self.__votesautorises = [str(i) for i in range(1, len(candidats) + 1)]

    @property
    def votesautorises(self):
        return self.__votesautorises

    def confrontation2(self, urne):
        """
        Rassemble une liste de bulletins de vote dans une matrice de préférences.
        les "bulletins" devraient être une liste de bulletin, où
        chaque bulletin est une liste de classements.  Pour par exemple,
        s’il y a 3 candidats, chaque bulletin de vote doit être une liste de 3
        numéros correspondant aux candidats.  Les classements les plus petits sont
         meilleurs.
        """

        est_prefere = {}
        n = len(self.candidats)
        for i in self.candidats:
            for j in self.candidats:
                est_prefere[i, j] = 0
        for bulletins in urne:
            for i in self.candidats:
                for j in self.candidats:
                    if bulletins.bulletin[i] and bulletins.bulletin[i] and (
                            bulletins.bulletin[i] < bulletins.bulletin[j]):
                        est_prefere[i, j] += 1
                        est_prefere[j, i] -= 1
        return est_prefere

    def vainqueur_condorcet(self, est_prefere):
        """ Determine le gagnant d'une election en utilisant la methode Schulze ( aussi appellé CSSD).
        'candidats' est de type liste et 'estprefere' un dictionnaire qui a pour cle la liste de candidat [i,j]
        et pour valeur un entier qui represente le nombre de voix du candidat
         i ou j prefere par les electeurs".
        """

        # Confronte les candidats deux par deux et affectent à chaque candidat ses victoires
        marge = {}
        for i in self.candidats:
            for j in self.candidats:
                marge[i, j] = est_prefere[i, j] - est_prefere[j, i]

        # Trouve le meilleur chemin de i a j en utilisant l'algorithme de Floyd
        for i in self.candidats:
            for j in self.candidats:
                for k in self.candidats:
                    if i != j != k != i:
                        smallest = min(marge[j, i], marge[i, k])
                        if marge[j, k] < smallest:
                            marge[j, k] = smallest

        # Le candidat qui reste invaincu est le gagnant
        vainqueurs = []
        for i in self.candidats:
            for j in self.candidats:
                if marge[j, i] > marge[i, j]:
                    break
            else:
                vainqueurs.append(i)
        return vainqueurs

    def resultat(self, urne):
        return self.vainqueur_condorcet(self.confrontation2(urne))


class JugementMajoritaire(Scrutin):

    def __init__(self, candidats):
        Scrutin.__init__(self, candidats)
        self.limite = 2
        self.__votesautorises = ["A rejeter", "Insuffisant", "Passable", "Assez Bien", "Bien", "Très Bien", "Excellent"]

    @property
    def votesautorises(self):
        return self.__votesautorises

    def resultats_candidat(self, urne):
        """
        Compte les votes des candidats et par mention
        retourne un dictionnaire ayant pour cle les noms
        des candidats et pour valeur un tableau de vote
        """

        resultats_par_candidat = {
            candidat: {mention: 0 for mention in self.votesautorises}
            for candidat in self.candidats
        }
        for bulletins in urne:
            for candidat, mention in bulletins.bulletin.items():
                resultats_par_candidat[candidat][mention] += 1
        return resultats_par_candidat

    def mention_majoritaire(self, resultats_par_candidat):
        resultat = {}
        for candidat, resultat1candidat in resultats_par_candidat.items():
            print(resultat1candidat)
            votes_cumules = 0
            for note, compte_vote in enumerate(resultat1candidat):
                votes_cumules += compte_vote
                limite = len(resultats_par_candidat) / 2
                if limite < votes_cumules:
                    resultat[candidat] = {
                        "mention": note,
                        "score": votes_cumules
                    }
                    break

        return resultat

    def resultat(self, urne):
        return self.mention_majoritaire(self.resultats_candidat(urne))