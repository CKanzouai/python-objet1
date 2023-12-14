from abc import ABC, abstractmethod


class Livre(ABC):
    def __init__(self, titre, auteur, achetable=False):
        self.__titre = titre
        self.__auteur = auteur
        self.__achetable = achetable

    def afficher_infos(self):
        print("le titre : ", self.__titre, ", l'auteur : ", self.__auteur, ", est achetable : ", self.__achetable)

    @abstractmethod
    def get_tjm(self):
        pass

    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self, nvtire):
        self.__titre = nvtire

    @property
    def auteur(self):
        return self.__auteur

    @auteur.setter
    def auteur(self, nvauteur):
        self.__auteur = nvauteur

    @property
    def achetable(self):
        return self.__achetable

    @achetable.setter
    def achetable(self, valeur):
        self.__achetable = valeur

    def __str__(self):
        return f"Titre: {self.__titre}, Auteur: {self.__auteur}, Achetable: {self.__achetable}"


"""livre = Livre("titre", "victor")
print(livre)
livre.titre = "nvtitre"
livre.auteur = "hugo"
livre.achetable = True
print(livre)
print(livre.titre, livre.auteur, livre.achetable)"""


class LivrePapier(Livre):


    def __init__(self, titre, auteur, etat, achetable):
        super().__init__(titre, auteur, achetable)
        self.__etat = etat

    def afficher_infos(self):
        super().afficher_infos()
        print(", etat:", self.__etat)

    def get_tjm(self):
        return 0.5


class LivreNumerique(Livre):
    def __init__(self, titre, auteur, format, achetable):
        super().__init__(titre, auteur, achetable)
        self.__format = format

    def afficher_infos(self):
        super().afficher_infos()
        print(", format:", self.__format)

    def get_tjm(self):
        return 0.25


livre = LivreNumerique("titre1", "auteur1", "pdf", True)
livre2 = LivreNumerique("titre2", "auteur3", "Kindle", False)
livre3 = LivrePapier("titre3", "auteur4", "neuf", False)
livre4 = LivrePapier("titre4", "auteur5", "occasion", True)
liste = [livre, livre2, livre3, livre4]

for livre in liste:
    livre.afficher_infos()


class Sortie(ABC):
    def __init__(self, __date, __livre: Livre):
        self.__date = __date
        self.__livre = __livre

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, nvdate):
        self.__date = nvdate

    @property
    def livre(self):
        return self.__livre

    @livre.setter
    def livre(self, nvlivre):
        self.__livre = nvlivre

    @abstractmethod
    def get_montant(self):
        pass


class Emprunt(Sortie):
    def __init__(self, __duree, date, livre):
        super().__init__(date, livre)
        self.__duree = __duree

    def get_montant(self):

        return self.__duree*self.livre.get_tjm()

class Achat(Sortie):
    def __init__(self, __montant, date, livre):
        super().__init__(date, livre)
        self.__montant = __montant

    def get_montant(self):
        return self.__montant


def montant_global(liste):
    montant_global = 0
    for l in liste:
        montant_global += l.get_montant()
    return montant_global


def montant_par_type(sorties):
    montants = {"Achat": 0, "Emprunt": 0}
    for sortie in sorties:
        if isinstance(sortie, Achat):
            montants["Achat"] += sortie.get_montant()
        elif isinstance(sortie, Emprunt):
            montants["Emprunt"] += sortie.get_montant()
    return montants


emprunt = Emprunt(2, "09/03/2022", livre2)
emprunt2 = Emprunt(6, "25/04/2023", livre3)
achat = Achat(50, "02/05/2022", livre)
achat2 = Achat(39, "06/12/2022", livre4)
liste2 = [emprunt, emprunt2, achat, achat2]
print(f"montant globale: {montant_global(liste2)}")
print(f"Montant par type: {montant_par_type(liste2)}")
print(emprunt.get_montant(), "et ", emprunt2.get_montant())
print(achat.get_montant(), "et", achat2.get_montant())
