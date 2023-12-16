class Animal:
    def __init__(self, nom, category, comportement):
        self._nom = nom
        self._category = category
        self._comportement = comportement

        @property
        def nom(self):
            return self._nom

        @property
        def category(self):
            return self._category


class Zone:
    def __init__(self, nom, animaux: list[Animal] = None):
        self._nom = nom
        self._animaux = animaux

    @property
    def nom(self):
        return self._nom

    @property
    def animaux(self):
        return self._animaux


class SavaneAfricaine(Zone):
    def __init__(self, animaux=None):
        super().__init__("Savane Africaine", animaux)

    def get_quantite_nourriture(self):
        return len(self._animaux) * 100

    def ajout_animal(self, animal: Animal):
        if animal._category == "carnivore" or animal._category == "mammifére":
            self._animaux.append(animal)


class FermeReptiles(Zone):
    def __init__(self, animaux=None):
        super().__init__("Ferme aux Reptiles", animaux)

    def get_quantite_nourriture(self):
        return len(self._animaux) * 0.1

    def ajout_animal(self, animal: Animal):
        if animal._category == "reptile":
            self._animaux.append(animal)


class Aquarium(Zone):
    def __init__(self, animaux=None):
        super().__init__("Aquarium", animaux)

    def get_quantite_nourriture(self):
        return len(self._animaux)

    def ajout_animal(self, animal: Animal):
        if animal._category == "poisson":
            self._animaux.append(animal)


class ZoneCarnivore(Zone):
    def __init__(self, animaux=None):
        super().__init__("Zone Carnivore", animaux)

    def get_quantite_nourriture(self):
        return len(self._animaux) * 10

    def ajout_animal(self, animal: Animal):
        if animal._category == "carnivore" or animal._category == "mammifére":
            self._animaux.append(animal)


class Voliere(Zone):
    def __init__(self, animaux=None):
        super().__init__("Volière", animaux)

    def get_quantite_nourriture(self):
        return len(self._animaux) * 0.25

    def ajout_animal(self, animal: Animal):
        if animal._category == "oiseau":
            self._animaux.append(animal)


class Zoo:
    def __init__(self, nom, zones: list[Zone]):
        self._nom = nom
        self._zones = zones

    def ajouter_animal(self, animal: Animal):
        for zone in self._zones:
            print(f"Ajout de {animal._nom} à {zone._nom}")
            zone.ajout_animal(animal)


lion = Animal("Lion", "Mammifere", "Carnivore")
gazelle = Animal("Gazelle", "Mammifere", "Herbivore")
python = Animal("Python", "Reptile", "Carnivore")
tortue = Animal("Tortue", "Reptile", "Herbivore")
requin = Animal("Requin", "Poisson", "Carnivore")
poisson_clown = Animal("Poisson-clown", "Poisson", "Herbivore")
vautour = Animal("Vautour", "Oiseau", "Carnivore")
perroquet = Animal("Perroquet", "Oiseau", "Herbivore")

savane = SavaneAfricaine([lion, gazelle])
ferme_reptiles = FermeReptiles([python, tortue])
aquarium = Aquarium([requin, poisson_clown])
zone_carnivore = ZoneCarnivore([lion, python, requin, vautour])
voliere = Voliere([gazelle, vautour, perroquet])

zoo = Zoo("Zoo Example", [savane, ferme_reptiles, aquarium, zone_carnivore, voliere])
nouvel_animal = Animal("Nouvel Animal", "Mammifere", "Herbivore")
zoo.ajouter_animal(nouvel_animal)
for zone in zoo._zones:
    print(f"{zone.nom}: {[animal._nom for animal in zone._animaux]}")

for zone in zoo._zones:
    print(f"{zone._nom}: {zone.get_quantite_nourriture()} kg de nourriture")
