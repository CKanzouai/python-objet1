"""1) Créez la classe AdressePostale représentant une adresse postale.
a. elle doit avoir les 4 attributs d’instance suivants : numéro de rue, libellé de
la rue, code postal et ville.
2) Créez 2 instances d’AdressePostale en renseignant les valeurs de tous les
attributs"""


class AdressePostale:
    def __init__(self, num_rue, libele_rue, code_postal, nom_ville):
        self.num_rue = num_rue
        self.libele_rue = libele_rue
        self.code_postal = code_postal
        self.nom_ville = nom_ville

    def __str__(self):
        return f"{self.num_rue} {self.libele_rue}, {str(self.code_postal)}, {str(self.nom_ville)}"


adr1 = AdressePostale(1, "avenue de paris", "71100", "Chalon")

adr2 = AdressePostale(23, "rue de dijon", "21000", "Dijon")

print(adr1.num_rue)
