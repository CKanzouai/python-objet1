"""Tâches
• Créez un module tp12 – redefinition hash.py
• Reprenez la classe Personne précédente
• Instanciez 2 personnes avec les mêmes valeurs d’attributs
• Mettez ces classes dans un set et vérifiez que cela ne fonctionne pas.
• Redéfinissez la méthode __hash__ afin de pouvoir désormais stocker des instances de
Personne dans un set.
• Afficher le contenu du set avec une boucle."""
from adresse_postale import AdressePostale

class Personne:
    def __init__(self, nom, prenom, adresse_postale=None):
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
        return self.nom == __value.nom and self.prenom == __value.prenom and self.adresse_postale == __value.adresse_postale


    def __hash__(self):
        return hash((self.nom, self.prenom, self.adresse_postale))


adr = AdressePostale(1, "avenue de paris", "71100", "Chalon")
adr1 = AdressePostale(1, "avenue de paris", "71100", "Chalon")
p1 = Personne("ahmed", "kanzouai",adr)
p2 = Personne("ahmed", "kanzouai", adr1)

set1={p1,p2}
print(set1)