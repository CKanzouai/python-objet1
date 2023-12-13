
class Livre:
    def __init__(self, titre, auteur):
        self.__titre = titre
        self.__auteur = auteur
        self.__achetable = False

    def afficher_infos(self):
        print("le titre : ", self.__titre, ", l'auteur : ", self.__auteur,", est achetable : ", self.__achetable)

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
        super().__init__(titre, auteur)
        self.__etat = etat

    def afficher_infos(self):
        super().afficher_infos()
        print(", etat:", self.__etat)


class LivreNumerique(Livre):
    def __init__(self, titre, auteur, format, achetable):
        super().__init__(titre, auteur)
        self.__format = format

    def afficher_infos(self):
        super().afficher_infos()
        print(", format:", self.__format)


livre = LivreNumerique("titre1", "auteur1", "pdf", True)
livre2 = LivreNumerique("titre2", "auteur3", "Kindle", False)
livre3=LivrePapier("titre3", "auteur4", "neuf", False)
livre4 = LivrePapier("titre4", "auteur5", "occasion",True)
liste = [livre, livre2, livre3, livre4]

for livre in liste:
    livre.afficher_infos()

