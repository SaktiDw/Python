import networkx as nx
import pylab as plt
from stuck import stuck


s = stuck()
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

E = {}
for m in range(len(V)):
    for i in range(len(V)):
        edge = []
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                edge.append(V[j])
                # edge = set([V[i],V[j]])
        E[str(V[i])] = (edge)
print(E)
visited = []
def dfs(E,source,target):
    s.push(source)
    visited.append(source)
    print(s.items)
    for i in range(len(E[source])):
        if target == (E[source][i]):
            s.push(E[source][i])
            break
        elif E[source][i] not in s.items:
            dfs(E,E[source][i],target)
            s.pop()
            break
        elif s.items in visited:

            s.pop()
            dfs(E,s.peek(),target)
            break
            # break

def Graph(V,E):
    G = nx.Graph() # Empty Graph
    for vertex in V: # Menambahkan semua vertexnya
        G.add_node(vertex)
    for i in E: # Menambahkan edgesnya
        for j in range(len(E[i])):
            G.add_edge(i,E[i][j])

    print('G: {0} nodes, {1} edges'.format(G.number_of_nodes(),G.number_of_edges()))
    pos = nx.spring_layout(G) # menentukan posisi node secara random
    nx.draw_networkx_nodes(G,pos) # membuat node graph
    nx.draw_networkx_labels(G,pos) # membuat weight graph
    nx.draw_networkx_edges(G,pos) # membuat edge graph
    plt.show()
Graph(V,E)
dfs(E,'a','z')
print("visited : ",visited)
print("item : ",s.items)
