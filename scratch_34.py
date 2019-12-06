import networkx as nx
import pylab as plt

V = ['a','b','c','d','e','f','g','z']
matrix = [
    [0,0,0,1,0,0,1,1],
    [0,0,1,1,1,0,0,1],
    [0,1,0,0,0,1,1,1],
    [1,1,0,0,1,0,0,0],
    [0,1,0,1,0,1,0,0],
    [0,0,1,0,1,0,1,0],
    [1,0,1,0,0,1,0,0],
    [1,1,1,0,0,0,0,0]
]

E = []

for i in range(len(V)):
    for j in range(len(matrix)):
        if matrix[i][j] != 0:
            edge = (V[i],V[j])
            E.append(edge)
print(E)

G = nx.Graph() # Empty Graph
for vertex in V: # Menambahkan semua vertexnya
    G.add_node(vertex)
for v1,v2 in E: # Menambahkan edgesnya
    if(v1 and v2 is not None):
        G.add_edge(v1,v2)
print('G: {0} nodes, {1} edges'.format(G.number_of_nodes(),G.number_of_edges()))


pos = nx.spring_layout(G) # menentukan posisi node secara random
nx.draw_networkx_nodes(G,pos) # membuat node graph
nx.draw_networkx_labels(G,pos) # membuat weight graph
# nx.draw_networkx_edge_labels(G,pos,edge_labels=eL) # memasang weight graph di edgenya
nx.draw_networkx_edges(G,pos) # membuat edge graph
plt.show()

while True:
    # eL = nx.get_edge_attributes(G,'weight')
    print("Rute terpendek")
    pos = nx.spring_layout(G) # menentukan posisi node secara random
    nx.draw_networkx_nodes(G,pos) # membuat node graph
    nx.draw_networkx_labels(G,pos) # membuat weight graph
    # nx.draw_networkx_edge_labels(G,pos,edge_labels=eL) # memasang weight graph di edgenya
    nx.draw_networkx_edges(G,pos) # membuat edge graph
    plt.show() # menampilkan graph
    a= input("titik mulai : ")
    if(a == "sudah"):
        break
    b= input("titik akhir : ")
    print("Rute terpendek harusnya : ",nx.dijkstra_path(G,a,b))
    # print(nx.all_pairs_dijkstra_path(G,a,b))
    print(nx.all_shortest_paths(G,a,b))
    print(list(nx.dfs_edges(G,a)))
    print(list(nx.dfs_tree(G,a)))
    lol = list(nx.all_simple_paths(G,a,b))
    for i in range(len(lol)):
        print(lol[i],end="\n")
    plt.show()

#
# class stack:
#     def __init__(self):
#         self.items = []
#
#     def kosong(self):
#         return self.items == []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         return self.items[len(self.items)-1]
#
#     def size(self):
#         return len(self.items)
#
# def dfs(edge,awal,akhir):
#     s=stack()
#     s.push(awal)
#     while(True):
#         for i in edge:
#             if i[0] == awal:
#                 s.push(i[1])





