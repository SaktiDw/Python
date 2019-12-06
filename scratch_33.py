import numpy as np
import networkx as nx
import pylab as plt

# G = nx.Graph()
# G.add_edge('A','B')
# G.add_edge('B','D')
# G.add_edge('B','C')
# G.add_edge('C','D')
# G.add_edge('A','D')
# short = nx.shortest_path(G,'A','C')
# print(short)

graph = np.array([
    [0,1,1,0,1,1],
    [1,0,1,0,0,0],
    [1,1,0,1,1,0],
    [0,0,1,0,1,0],
    [1,0,1,1,1,0],
    [1,0,0,0,1,0]
    ])#ANJING
G = nx.Graph(graph)
pos = nx.spring_layout(G)
nx.draw(G, pos, font_size=14, with_labels=True)

print("Cari Jarak terpendek")
a= int(input("titik mulai : "))
b= int(input("titik akhir : "))
shortest = nx.shortest_path(G,a,b)
print("Jalur terpendek adalah ",shortest)
plt.show()

