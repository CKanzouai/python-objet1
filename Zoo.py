"""Projet approche-objet
• créez un module tp3 – methode de classe.py
• Créez une classe Zoo
• Cette classe Zoo a 2 attributs de classe :
o La liste des animaux représentés dans le Zoo
o Le nombre total d’animaux
• Créez une méthode de classe ajouter_animaux qui prend en paramètre l’espèce de
l’animal (par exemple Lion) et le nombre d’animaux ajoutés.
o Si l’espèce n’existe pas dans la liste, cette méthode ajoute l’animal à la liste des
animaux du zoo
o Cette méthode augmente le nombre d’animaux du zoo du nombre indiqué
• Ajoutez une méthode de classe afficher_animaux qui affiche toutes les espèces du Zoo
ainsi que le nombre total d’animaux dans le Zoo."""


class Zoo:
    list_animaux = []
    nombre = 0

    @classmethod
    def ajouter_animaux(cls, animal, nombre):
        if animal not in cls.list_animaux:
            cls.list_animaux.append(animal)
        cls.nombre += nombre

    @classmethod
    def afficher_animaux(cls):
        print("Espèces d'animaux :", cls.list_animaux)
        print("Nombre total d'animaux :", cls.nombre)

Zoo.ajouter_animaux("Lion", 3)
Zoo.ajouter_animaux("Tigre", 1)

Zoo.afficher_animaux()

