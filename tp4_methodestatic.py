"""• Créez une classe ChaineUtils
• Créez une méthode static est_anagramme qui prend en paramètre 2 chaines de
caractères et retourne si Oui ou Non la 1ère chaine est un anagramme de la seconde.
• Créez une méthode static comptage_chaine qui prend en paramètre 2 chaines de
caractères et compte le nombre de fois où la seconde chaine apparait dans la
première.
"""

class ChaineUtils:
    @staticmethod
    def est_anagramme(chaine1, chaine2):
        chaine1triee = sorted(chaine1)
        chaine2triee = sorted(chaine2)
        if (len(chaine1)==len(chaine2triee)):
            if (chaine1triee == chaine2triee):
                return True
        return False

    @staticmethod
    def comptage_chaine(chaine1, chaine2):
        return chaine1.count(chaine2)


print(ChaineUtils.est_anagramme("listen", "silent"))
print(ChaineUtils.comptage_chaine("silentlisten", "listen"))

