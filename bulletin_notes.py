class Etudiant:
    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom


class Note:
    def __init__(self, valeur, date, category):
        self._valeur = valeur
        self._date = date
        self._category = category

    @property
    def valeur(self):
        return self._valeur


class Discipline:
    def __init__(self, nom, notes: list[Note]):
        self._nom = nom
        self._notes = notes

    @property
    def nom(self):
        return self._nom

    @property
    def notes(self):
        return self._notes


class Bulletin:
    def __init__(self, etudiant: Etudiant, disciplines: list[Discipline]):
        self._etudiant = etudiant
        self._disciplines = disciplines

    def calculer_moyenne(self):
        dico = {}
        for discipline in self._disciplines:
            notes_discipline = [note.valeur for note in discipline.notes]
            if notes_discipline:
                dico[discipline.nom] = sum(notes_discipline) / len(notes_discipline)
            else:
                dico[discipline.nom] = 0
        return dico

    def afficher_moyenne(self):
        return self.calculer_moyenne()


etudiant = Etudiant("Jean", "Claude")
note1 = Note(13.5, "2023-12-14", "TP")
note2 = Note(11, "2023-12-15", "QCM")
note4 = Note(9, "2023-12-15", "TD")
note3 = Note(10, "2023-12-17", "QCM")
note5 = Note(12, "2023-12-21", "PROJET")
note6 = Note(17, "2023-12-22", "TP")
note7 = Note(5, "2023-12-23", "QCM")
note8 = Note(12, "2023-12-24", "TD")

discipline1 = Discipline("math", [note7, note8])
discipline2 = Discipline("science", [note1, note2, note4])
discipline3 = Discipline("physics", [note3, note5, note6])
bulletin = Bulletin(etudiant, [discipline1, discipline2, discipline3])
print(bulletin.afficher_moyenne())
