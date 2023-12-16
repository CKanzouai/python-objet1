class Salarie:
    def __init__(self, nom, prenom, salaire):
        self._nom = nom
        self._prenom = prenom
        self._salaire =salaire

    def __str__(self):
        return f"le nom: {self._nom}, le prenom: {self._prenom}, le salaire: {self._salaire}"


chaine = "Durand;Marcel;2 523.5"
print(chaine.split(";"))
premier_caractere = chaine[0]
print("Premier caractère: " + premier_caractere)
print(len(chaine))
print(chaine.index(";"))
element = chaine.split(";")
print(element)
print(element[2].replace(" ", ""))
print(chaine[0:6])
print(chaine[0:6].upper())
print(chaine[0:6].lower())
print(chaine.replace(" ", ""))

#salarie = Salarie(chaine[0:6].upper(), chaine[7:13].lower(), chaine[14:].replace(" ", ""))
salarie = Salarie(element[0], element[1], element[2].replace(" ", ""))
print(salarie)
