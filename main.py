import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import time
from tkinter import filedialog

# file = filedialog.askopenfilename(initialdir=".")
# filename = str(file)
# print(filename)

nazwa1 = "nodes.csv"  # oznaczenia komiksów i bohaterów
nazwa2 = "hero-network.csv"  # interakcje
nazwa3 = "edges.csv"  #

heros = []  # zbiór bohaterów
comics = []

with open(nazwa1, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if row[1] == 'hero':
            heros.append(row[0])
        elif row[1] == 'comic':
            comics.append(row[0])

heros[heros.index('BLADE/')] = 'BLADE'
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

    hero1.pop(0)
    hero2.pop(0)

for x in range(len(hero1)):
    if hero1[x] == "SPIDER-MAN/PETER PAR":
        hero1[x] = "SPIDER-MAN/PETER PARKER"
    if hero2[x] == "SPIDER-MAN/PETER PAR":
        hero2[x] = "SPIDER-MAN/PETER PARKER"

unique, counts = np.unique(hero2 + hero1, return_counts=True)  # zliczam powtórzenia

# """
G = nx.Graph()  # graf
for x in heros:
    G.add_node(x)

for x, y in zip(hero1, hero2):
    G.add_edge(x, y)

deg = [[], []]
for x in list(G.degree):
    deg[0].append(x[0])
    deg[1].append(x[1])


a = sorted(list(G.degree), key=lambda l: l[1])
b = [x for x in a if x[1] > 10]

deg2 = [[], []]
for x in b:
    deg2[0].append(x[0])
    deg2[1].append(x[1])
# """
# """
    
unique, counts = np.unique(deg[1], return_counts=True)  # zliczam powtórzenia
plt.scatter(unique, counts)
plt.yscale('log')
plt.xscale('log')
plt.xlabel("stopień węzła")
plt.ylabel("liczba węzłów")
plt.show()

print(len(unique))

unique, counts = np.unique(deg2[1], return_counts=True)  # zliczam powtórzenia
print(len(unique))

plt.scatter(unique, counts)
plt.yscale('log')
plt.xscale('log')
plt.xlabel("stopień węzła")
plt.ylabel("liczba węzłów")
plt.show()

# """
"""
nx.draw(G)
plt.show()
# """
