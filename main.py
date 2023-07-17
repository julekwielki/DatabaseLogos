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


def inicjalizacja(organizm):
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


def sym(K, D, zasieg, n, organizm):
    inicjalizacja(organizm)
    d = D
    zapis = [[], []]

    for s in range(K):
        nowotworowe, martwe = 0, 0
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    if organizm[x][y][z].status == "nowotworowa":
                        PHit = p_hit(d)
                        organizm[x][y][z].wiek += 1
                        losowa1 = random.random()
                        nowotworowe += 1

                        if losowa1 <= PHit:  # trafiona komórka nowotworowa
                            losowa2 = random.random()
                            PRD = p_rd(d)  # śmierć w precyzyjnym trafieniu
                            PCRD = p_crd(d)  # smierci komorki nowotowrowej w zwiazku z radioczuloscia
                            # PCS = 0.009 # podział komórki nowotworowej
                            # PCD = 0.0004 # naturalna śmierć komórki nowotworowej

                            temp1 = PCD + PRD + PCRD
                            temp2 = temp1 + PCS
                            if losowa2 <= temp1:
                                organizm[x][y][z].martwa()
                            elif losowa2 <= temp2:
                                rozmnazanie(x, y, z, zasieg)

                        else:
                            losowa2 = random.random()
                            if losowa2 <= PCD:
                                organizm[x][y][z].martwa()
                            elif losowa2 <= PCD + PCS:
                                rozmnazanie(x, y, z, zasieg)

                    elif organizm[x][y][z].status == "martwa":
                        martwe += 1
                        if organizm[x][y][z].umieranie != 0:
                            organizm[x][y][z].umieranie -= 1

        zapis[0].append(nowotworowe)
        zapis[1].append(martwe)

    nowotworowe, martwe = 0, 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if organizm[x][y][z].status == "nowotworowa":
                    nowotworowe += 1
                elif organizm[x][y][z].status == "martwa":
                    martwe += 1

    zapis[0].append(nowotworowe)
    zapis[1].append(martwe)

    return zapis


n = 32
zasieg = 3
k = 1

dawki = [0, 0.2, 0.5, 0.7, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
data = [[], []]
# """
for aa in dawki:
    organizm = np.ndarray((n, n, n), dtype=object)
    zapis = sym(k, aa, zasieg, n, organizm)
    data[0].append(aa)
    data[1].append(zapis[0][len(zapis)-1])

    losowa2 = random.random()
    PRD = p_rd(aa)  # śmierć w precyzyjnym trafieniu
    PCRD = p_crd(aa)  # smierci komorki nowotowrowej w zwiazku z radioczuloscia
    PHit = p_hit(aa)
    PCS = 0.009 # podział komórki nowotworowej
    PCD = 0.0004 # naturalna śmierć komórki nowotworowej

    temp1 = PCD + PRD + PCRD
    temp2 = temp1 + PCS

    print(PHit, PRD, PCRD, PCS, PCD, temp1, PHit*temp1, temp2)

    t = "dawka (jeden krok)\tżywe komórki\n"
    for x in range(len(data[0])):
        t = t + str(data[0][x]) + "\t" + str(data[1][x]) + "\n"
    with open("jeden krok.txt", 'w') as file:
        file.write(t)
# """

"""
dawki = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.5, 2, 2.5]
n = 32
zasieg = 3
k = int(6 / dawki[0]) + 1

nn = np.zeros((len(dawki)*2, k))

for aa in range(len(dawki)):
    organizm = np.ndarray((n, n, n), dtype=object)
    kk = int(6 / dawki[aa])
    zapis = sym(kk, dawki[aa], zasieg, n, organizm)

    for x in range(len(zapis[0])):
        nn[aa * 2, x] = x*dawki[aa]
        nn[aa * 2 + 1, x] = zapis[0][x]

t = ""
for x in range(k):
    for y in range(len(dawki)*2):
        t = t + str(nn[y][x]) + "\t"
    t = t + "\n"
with open("dawka.txt", 'w') as file:
    file.write(t)
"""
