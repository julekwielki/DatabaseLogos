import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import time
from tkinter import filedialog

# file = filedialog.askopenfilename(initialdir=".")
# filename = str(file)
# print(filename)


def fill_graph(graph, node, end1, end2):
    for q in node:
        graph.add_node(q)  # wszystkie postacie jako wierzchołki-nawet te postacie bez interakcji

    for w, e in zip(end1, end2):  # interakcje jako krawędzie
        graph.add_edge(w, e)
    return graph


def fill_grah_group(graph, node, end1, end2):
    for q in node:
        graph.add_node(q)

    for w, e in zip(end1, end2):  # interakcje jako krawędzie
        if w in node or e in node:
            graph.add_edge(w, e)
    return graph


def degrees_sorted(graph):
    lista = sorted(list(graph.degree), key=lambda l: l[1])  # lista postaci i ich stopni posortowana wg stopnia
    sort_list = [q for q in lista if q[1] > 0]

    degrees = [[], []]
    for q in sort_list:
        degrees[0].append(q[0])
        degrees[1].append(q[1])
    return degrees


def draw_degrees(lista, scale='log'):  # linear
    uniq, count = np.unique(lista, return_counts=True)  # zliczam powtórzenia
    plt.scatter(uniq, count)
    plt.yscale(scale)
    plt.xscale(scale)
    plt.xlabel("stopień węzła")
    plt.ylabel("liczba węzłów")
    plt.show()


nazwa1 = "nodes.csv"  # oznaczenia komiksów i bohaterów
nazwa2 = "hero-network.csv"  # interakcje
nazwa3 = "edges.csv"  #

ff = ['MR. FANTASTIC/REED R', 'HUMAN TORCH/JOHNNY S', 'THING/BENJAMIN J. GR', 'INVISIBLE WOMAN/SUE']
Avengers1 = ['IRON MAN/TONY STARK', 'THOR/DR. DONALD BLAK', 'WASP/JANET VAN DYNE', 'ANT-MAN/DR. HENRY J.', 'HULK/DR. ROBERT BRUC']

heros = []  # zbiór bohaterów
comics = []

with open(nazwa1, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if row[1] == 'hero':
            heros.append(row[0])
        elif row[1] == 'comic':
            comics.append(row[0])

heros[heros.index('BLADE/')] = 'BLADE'  # korekta błędów w plikach
heros[heros.index('SABRE/')] = 'SABRE'
heros[heros.index('SPIDER-MAN/PETER PARKERKER')] = 'SPIDER-MAN/PETER PARKER'

hero1 = []
hero2 = []

with open(nazwa2, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if row[0][-1] == " ":
            hero1.append(row[0][0:-1])
        else:
            hero1.append(row[0])
        if row[1][-1] == " ":
            hero2.append(row[1][0:-1])
        else:
            hero2.append(row[1])


for x in range(len(hero1)):
    if hero1[x] == "SPIDER-MAN/PETER PAR":
        hero1[x] = "SPIDER-MAN/PETER PARKER"
    if hero2[x] == "SPIDER-MAN/PETER PAR":
        hero2[x] = "SPIDER-MAN/PETER PARKER"


her = []
com = []
with open(nazwa3, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        hero1.append(row[0])
        hero2.append(row[1])

    hero1.pop(0)
    hero2.pop(0)

"""
G = nx.Graph()  # graf wszystkich
fill_graph(G, heros, hero1, hero2)

Gff = nx.Graph()  # graf fantastycznej czwórki
fill_grah_group(Gff, ff, hero1, hero2)


Ga = nx.Graph()  # graf fantastycznej czwórki
fill_grah_group(Ga, Avengers1, hero1, hero2)

G_one = nx.Graph()  # graf fantastycznej czwórki
fill_grah_group(G_one, ['TILDA'], hero1, hero2)

deg = degrees_sorted(G)
# """


"""
    
unique, counts = np.unique(deg[1], return_counts=True)  # zliczam powtórzenia
# """

"""
t = ""
for x in range(len(deg2[0])):
    t = t + str(deg2[0][x]) + "\t" + str(deg2[1][x]) + "\n"
with open('stopnie.txt', 'w') as f:
    f.write(t)

# """
"""
nx.draw_networkx(G_one)
plt.show()
# """
