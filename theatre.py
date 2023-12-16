class Theatre:
    def __init__(self, nom, capacite, total_clients, recette):
        self._nom = nom
        self._capacite = capacite
        self._total_clients = total_clients
        self._recette = recette

    def inscrire(self, nbr_clients, prix):
        if (self.total_clients + nbr_clients) <= self._capacite:
            self._total_clients += nbr_clients
            self._recette += prix * nbr_clients
        else:
            print("nombre totale atteint")
        return self._recette

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nvnom):
        self._nom = nvnom

    @property
    def capacite(self):
        return self._capacite

    @capacite.setter
    def capacite(self, nvcapacite):
        self._capacite = nvcapacite

    @property
    def total_clients(self):
        return self._total_clients

    @total_clients.setter
    def total_clients(self, nvtotal):
        self._total_clients = nvtotal

    @property
    def recette(self):
        return self._recette

    @recette.setter
    def recette(self, nvrecette):
        self._recette = nvrecette


theatre = Theatre("the1", 120, 90, 1200)
theatre.inscrire(3, 10)
theatre.inscrire(19, 10)
theatre.inscrire(8, 10)
theatre.inscrire(8, 10)
print("le total de clients inscrits: ", theatre.total_clients)
print("la  recette totale de l’établissement: ", theatre.recette)
