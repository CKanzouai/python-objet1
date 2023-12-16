from adresse_postale import AdressePostale
from personne import Personne


class PersonneException(Exception):
    def __init__(self, message):
        super().__init__(message)


class PersonneService:
    def __init__(self, personne:Personne):
        self.personne = personne

    def valider(self, personne: Personne):
        try:
            if not personne.nom or len(personne.nom.strip()) < 2:
                raise PersonneException("Le nom doit être renseigné et doit contenir au moins 2 lettres")
            elif not personne.prenom or len(personne.prenom.strip()) < 2:
                raise PersonneException("Le prénom doit être renseigné et doit contenir au moins 2 lettres")
            elif not personne.adresse_postale:
                raise PersonneException("L'adresse postale doit être renseignée")
            else:
                print("La personne est bien validée")
        except PersonneException as e:
            print(f"la personne [{personne}] ne peut pas etre valider: {e}")
        else:
            print(f"la personne [{personne}] a été bien validée")


adr = AdressePostale(1, "avenue de paris", "71100", "Chalon")
adr1 = AdressePostale(23, "rue de dijon", "21000", "Dijon")
p1 = Personne("a", "kanzouai", adr)
p2 = Personne("ouadie", "boukanzia")
p3 = Personne("", "boukanzia", adr1)
p4 = Personne("ouadie", "b", adr1)
p5 = Personne("ouadie", "boukanzia", adr1)


liste_personne = [p1, p2, p3, p4, p5]

for personne in liste_personne:
    personne_service = PersonneService(personne)
    personne_service.valider(personne)
