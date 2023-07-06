import matplotlib.pyplot as plt
import numpy as np
from komorka import Komorka
import math
import random


PCS = 0.009  # podział komórki nowotworowej
PCD = 0.0004  # naturalna śmierć komórki nowotworowej
PHIT = 1.3  # stała do prawd. trafienia
const_PRD = 0.5  # stala do smierci komorki w wyniku precyzyjnego trafienia przez promieniowanie
const_PCRD = 0.32  # stala do smierci zwiazanej z radioczuloscia


def p_hit(D):  # prawdopodobienstwo trafienia komorki
    PHit = 1 - math.exp((-PHIT * D))
    return PHit


def p_rd(D):  # prawdopodobieństwo smierci komorki w wyniku precyzyjnego trafienia przez promieniowanie
    PRD = 1 - math.exp(-const_PRD * D)
    return PRD


def p_crd(D):  # prawdopodobienstwo smierci komorki nowotowrowej w zwiazku z radioczuloscia
    PCRD = 1 - math.exp(-const_PCRD * D)
    return PCRD


def pom(a, b, c, zasieg):  # zwraca położenie nowopowstałej komórki
    tab = [[], [], []]  # tab to tablica tablic zawierająca w kolejnych elementach kolejne wartości współrzędnej

    xx = range(max(a - math.ceil(zasieg), 0), min(n, a + math.ceil(zasieg)))
    yy = range(max(b - math.ceil(zasieg), 0), min(n, b + math.ceil(zasieg)))
    zz = range(max(c - math.ceil(zasieg), 0), min(n, c + math.ceil(zasieg)))

    for x in xx:
        for y in yy:
            for z in zz:
                r = math.sqrt(math.pow(a - x, 2) + math.pow(b - y, 2) + math.pow(c - z, 2))
                if r <= zasieg and (organizm[x][y][z].status == "pusta" or organizm[x][y][z].status == "martwa"):
                    tab[0].append(x)
                    tab[1].append(y)
                    tab[2].append(z)

    if len(tab[0]) != 0:  # wybiera położenie nowej komórki w sposób losowy
        nr = random.randint(0, len(tab[0]) - 1)
        return [tab[0][nr], tab[1][nr], tab[2][nr]]
    return [0, 0, 0]


def rozmnazanie(a, b, c, zasieg):
    x, y, z = pom(a, b, c, zasieg)

    if [x, y, z] != [0, 0, 0]:
        organizm[x][y][z].status = organizm[a][b][c].status
        organizm[x][y][z].wiek = 0


def inicjalizacja():
    for x in range(n):
        for y in range(n):
            for z in range(n):
                organizm[x][y][z] = Komorka()
                organizm[x][y][z].wiek = 0.0
                organizm[x][y][z].uszkodzenia = 0
                organizm[x][y][z].status = "pusta"
                organizm[x][y][z].mutacje = 0
    for x in range(n):  # zapełnienie komórkami
        for y in range(n):
            for z in range(n):
                organizm[x][y][z].status = "nowotworowa"
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if x == 0 or y == 0 or z == 0 or x == n - 1 or y == n - 1 or z == n - 1:
                    organizm[x][y][z].status = "sciana"


n = 15
d = 0.5
zasieg = 3
k = 10

organizm = np.ndarray((n, n, n), dtype=object)
inicjalizacja()

zapis = [[], [], []]
nowotworowe, martwe, puste = 0, 0, 0

for s in range(k):
    nowotworowe, martwe, puste = 0, 0, 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if organizm[x][y][z].status == "nowotworowa":
                    PHit = p_hit(d)
                    organizm[x][y][z].wiek += 1
                    losowa1 = random.random()
                    nowotworowe += 1
                if organizm[x][y][z].status == "martwa":
                    martwe += 1

    zapis[0].append(nowotworowe)
    zapis[1].append(martwe)
    zapis[2].append(puste)

plt.plot(zapis[0])
plt.plot(zapis[1])
plt.show()
