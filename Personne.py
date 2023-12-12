"""attributs.
3) créer la classe Personne représentant une personne.
a. Cette classe a 3 attributs :
i. le nom
ii. le prénom
iii. une adresse postale (de type AdressePostale)
4) Créer 2 instances de la classe Personne en renseignant la valeur de tous les
attributs.
5) Affichez les 2 instances avec la fonction print. Que constatez-vous ?"""

from AdressePostale import AdressePostale

class Personne:
    def __init__(self, nom, prenom, adresse_postale):
        self.nom = nom
        self.prenom = prenom
        self.adresse_postale = adresse_postale

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_adresse_postale(self):
        return self.adresse_postale

    def set_nom(self, nom):
        self.nom = nom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_adresse_postale(self, adresse_postale):
        self.adresse_postale = adresse_postale

    def maj(self):
        return f"{self.nom.upper()} {self.prenom.upper()}"

    def __str__(self):
       return f"{self.nom} {self.prenom}, {str(self.adresse_postale)}"



adr = AdressePostale(1, "avenue de paris", "71100", "Chalon")
adr1 = AdressePostale(23, "rue de dijon", "21000", "Dijon")
p1 = Personne("ahmed", "kanzouai",adr)
p2 = Personne("ouadie", "boukanzia", adr1)
p1.set_nom("dlia")
p1.set_prenom("asmae")
print(p1.get_nom(), p1.get_prenom())

print(p1.maj())
print(p1.nom, p1.prenom, p1.get_adresse_postale())
print(p2.nom, p2.prenom, p2.get_adresse_postale())

class TestPersonne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.adresse_postale = None

    def set_adresse_postale(self, adresse_postale):
        self.adresse_postale = adresse_postale

p3 = TestPersonne("ouadie", "boukanzia")
adr3 = AdressePostale(56, "rue de paris", "69000", "Lyon")
p3.set_adresse_postale(adr3)
print(p3.adresse_postale)

