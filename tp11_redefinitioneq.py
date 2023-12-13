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

    def __repr__(self):
        return f"Personne(nom='{self.nom}', prenom='{self.prenom}', adresse={self.adresse_postale})"

    def __eq__(self, __value):
        if not isinstance(__value, Personne):
            return False
        return self.nom == __value.nom and self.prenom == __value.prenom


adr = AdressePostale(1, "avenue de paris", "71100", "Chalon")
adr1 = AdressePostale(23, "rue de dijon", "21000", "Dijon")
p1 = Personne("ahmed", "kanzouai",adr)
p2 = Personne("ahmed", "kanzouai", adr1)

print(p1 == p2)
