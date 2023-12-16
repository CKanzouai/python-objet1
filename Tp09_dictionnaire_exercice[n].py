dicoVilles = {13: "Marseille", 34: "Montpellier", 44: "Nantes", 75: "Paris", 31: "Toulouse"}

for key in dicoVilles:
    print(key, dicoVilles[key])
print()
print("la taille du dictionnaire est :", len(dicoVilles))
print()


def count_chars(liste):
    dico = {}
    for mot in liste:
        dico[mot] = len(mot)
    return dico


print(count_chars(["Coucou", "Hi"]))


def count_occurrences(liste):
    dico = {}
    for fruit in liste:
        if fruit in dico:
            dico[fruit] += 1
        else:
            dico[fruit] = 1
    return dico


print(count_occurrences(["Ananas", "Banane", "Orange", "Ananas", "Banane"]))


class Salarie():
    def __init__(self, nom, matricule, service):
        self._nom = nom
        self._matricule = matricule
        self._service = service

    def get_services(self):
        return self._service

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nvnom):
        self._nom = nvnom

    @property
    def matricule(self):
        return self._matricule

    @matricule.setter
    def matricule(self, nvmatricule):
        self._matricule = nvmatricule

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, nvservice):
        self._service = nvservice


liste2 = [
    Salarie("Antoine Dupont", 127, "DSI/JAVA"),
    Salarie("Fatima Ouassa", 478, "DSI/JAVA"),
    Salarie("Berthe Casa", 238, "DSI/PHP"),
    Salarie("Cassian Andor", 156, "DSI/PYTHON"),
    Salarie("Lee Wu", 559, "DSI/PHP"),
    Salarie("Hassan Missen", 96, "DSI/PYTHON"),
    Salarie("Aurélien PIC", 889, "DSI/JAVA")]

liste3 = []
for Salarie in liste2:
    liste3.append(Salarie.get_services())

print("nombre de salariés par service est :", count_occurrences(liste3))
