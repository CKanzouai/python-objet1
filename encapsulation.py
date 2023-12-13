class Livre:
    def __init__(self, titre, auteur):
        self.__titre = titre
        self.__auteur = auteur
        self.__achetable = False

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
        return f"Titre: {self.titre}, Auteur: {self.auteur}, Achetable: {self.achetable}"


livre = Livre("titre", "victor")
print(livre)
livre.titre = "nvtitre"
livre.auteur = "hugo"
livre.achetable = True
print(livre)
print(livre.titre, livre.auteur, livre.achetable)