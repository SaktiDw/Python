import networkx as nx
import pylab as plt
import re

#default
V = ['a','b','c','d','e','f','g','z'] # Vertices
E = [('a','b',2),('a','f',1),('b','c',2),('b','d',2),
    ('b','e',4),('c','e',3),('c','z',1),('d','e',4),('d','f',3),
    ('e','g',7),('f','g',4),('g','z',1)] # Edges & Weight-nya

# # With I N P U T
# v = input("Masukkan vertex : ")
# V = re.split(",",v)
#
# E = []
# e =None
# while e != "sudah":
#     e = input("Masukkan edges : ")
#     c = re.split(",",e)
#     # c.append(int(c[2]))
#     if e != "sudah":
#         E.append(c)
#
# print(E,V)

# Mulai Membentuk Graph-nya
G = nx.Graph() # Empty Graph
for vertex in V: # Menambahkan semua vertexnya
    G.add_node(vertex)
for v1,v2,w in E: # Menambahkan edgesnya
    if(v1 and v2 and w is not None):
        G.add_edge(v1,v2, weight=w)
print('G: {0} nodes, {1} edges'.format(G.number_of_nodes(),G.number_of_edges()))

while True:
    pos = nx.spring_layout(G)
    eL = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_labels(G,pos)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=eL)
    nx.draw_networkx_edges(G,pos)
    plt.show()
    print("Rute terpendek")
    a= input("titik mulai : ")
    if(a == "sudah"):
        break
    b= input("titik akhir : ")
    print(nx.dijkstra_path(G,a,b))
    # print(nx.all_pairs_dijkstra_path(G,a,b))
    # print(nx.all_shortest_paths(G,a,b))
    nx.shortest_path_length()
    plt.show()
