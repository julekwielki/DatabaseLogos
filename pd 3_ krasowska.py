import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt


# """
# wersja trochę szybsza wersja startująca od 2 wierzchołków, a nie jednego
def chose_node2(tab):
    norm = [float(i) / sum(tab) for i in tab]  # normowanie do 1
    norm2 = [sum(norm[:b + 1]) for b in range(len(norm))]  # sumowanie - zakres zajmowany w tablicy przez każdy węzeł jest liniowo proporcjonalny do jego stopnia
    rand = random.random()  # losowanie wartości
    ind = norm2.index(min([a for a in norm2 if (a > rand)]))  # sprawdzanie, na który węzeł przypada wartość
    return ind


m = 1
le = 1500
G = nx.Graph()  # graf
G.add_node(0)  # pierwszy wierzchołek
G.add_node(1)
degree = [m, m]  # tablica przechowująca stopień wierzchołka - 2 wierzchołki o stopniu m
for nn in range(m):
    G.add_edge(0, 1)  # dodanie krawędzi między pierwszymi 2 wierzchołkami

for x in range(2, le):
    print(x)
    G.add_node(x)  # tworzę nowy wierzchołek
    nodes = []  # tablica na wierzchołki, o których mam się dołączyć (jeśli m > 1)
    for nn in range(m):
        nodes.append(chose_node2(degree))  # wybieram wierzchołki, do których mam się dołączyć
    degree.append(0)  # tworzę w tablicy pomocniczej miejsce na stopień nowego wierzchołka
    for nn in nodes:
        G.add_edge(x, nn)  # dodaję krawędź
        degree[x] += 1  # zwiększam stopień wierzchołków, do których się dołączam
        degree[nn] += 1

unique, counts = np.unique(degree, return_counts=True)  # zliczam powtórzenia

plt.scatter(unique, counts)
plt.yscale('log')
plt.xscale('log')
plt.xlabel("stopień węzła")
plt.ylabel("liczba węzłów")
plt.show()
# """

"""
def chose_node(tab):
    if tab == [0]:  # jeśli mamy tylko 1 węzeł przyłączamy się do niego
        return 0
    else:
        norm = [float(i)/sum(tab) for i in tab]  # normowanie do 1
        norm2 = [sum(norm[:b+1]) for b in range(len(norm))]  # sumowanie - zakres zajmowany w tablicy przez każdy węzeł jest liniowo proporcjonalny do jego stopnia
        rand = random.random()  # losowanie wartości
        ind = norm2.index(min([a for a in norm2 if (a > rand)]))  # sprawdzanie, na który węzeł przypada wartość
        return ind


m = 1  # liczba krawędzi dodawanych wraz z dodaniem węzła
le = 5000
G = nx.Graph()  # graf
G.add_node(0)  # pierwszy wierzchołek
degree = [0]  # tablica przechowująca stopień węzła - 0 stopień jedynego węzła
for x in range(1, le):
    G.add_node(x)  # tworzę nowy wierzchołek
    nodes = []  # tablica na wierzchołki, o których mam się dołączyć (jeśli m > 1)
    for nn in range(m):
        nodes.append(chose_node(degree))  # wybieram węzła=y, do których mam się dołączyć
    degree.append(0)  # tworzę w tablicy pomocniczej miejsce na stopień nowego węzła
    for nn in nodes:
        G.add_edge(x, nn)  # dodaję krawędź
        degree[x] += 1  # zwiększam stopień węzłów, do których się dołączam
        degree[nn] += 1
unique, counts = np.unique(degree, return_counts=True)  # zliczam powtórzenia

plt.scatter(unique, counts)
plt.yscale('log')
plt.xscale('log')
plt.xlabel("stopień węzła")
plt.ylabel("liczba węzłów")

plt.show()
"""
