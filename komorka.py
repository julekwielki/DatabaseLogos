"""
zawiera parametry danej komorki i funkcje wykorzystywane do zmian parametrów
"""


class Komorka(object):

    def __init__(self):
        self.status = ""
        self.wiek = 0
        self.uszkodzenia = 0
        self.uszkodzenia2 = 0
        self.mutacje = 0
        self.umieranie = 0  # odliczanie czasu od inicjacji śmierci

        # do efektu sąsiedztwa
        self.uszkodzenia0 = 0
        self.uszkodzenia1 = 0
        self.stala_dyfuzji_MDP = 0.0
        self.stala_dyfuzji_GJP = 0.0
        self.M = 0.0  # ilość sygnałów produkowanych na drodze MDP w czasie t
        self.M1 = 0.0  # ilość sygnałów produkowanych na drodze MDP w czasie t + 1
        self.G = 0
        self.G1 = 0

    def martwa(self):
        self.status = "martwa"
        self.umieranie = 12  # rozpoczęcie odliczania do czasu zwolnienia pola