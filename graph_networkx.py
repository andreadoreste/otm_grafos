import networkx as nx 
import matplotlib.pyplot as plt

#from backtrack import group_by

nodes = ['a','b','c','d','e','f','g','h','i','j','l']

G = nx.Graph()

G.add_nodes_from(nodes)
#print G.nodes()

G.add_edge('a','b', weight=5)
G.add_edge('a','d', weight=6)
G.add_edge('b','c', weight=9)
G.add_edge('a','c',weight=10)
G.add_edge('d','e',weight=9)
G.add_edge('b','f',weight=7)
G.add_edge('f','g',weight=8)
G.add_edge('c','e',weight=1)
G.add_edge('d','j',weight=5)
G.add_edge('g','i',weight=1)
G.add_edge('j','h',weight=4)
G.add_edge('h','i',weight=2)
G.add_edge('i','l',weight=1)

pto = [['a', 'b', 'c', 'e'], ['f', 'g', 'i', 'l'], ['j', 'd', 'h']]
P = nx.blockmodel(G,pto)
print P.nodes()


print P.edges(data=True)

eg = P.edges_iter(data=True)

count = 0
for e in eg:
	count+=e[2]['weight']
#print G.edges()
print count
'''
nodes_list = G.nodes()
sol=[]
p = group_by(nodes_list,5)
t= len(p)
for j in p:
	for i in j:
		i = list(i)
		#print i
		H = G.subgraph(i)
		if nx.is_connected(H):
			#print H.nodes()
			print j
'''
#print p
#nx.draw(P)
#plt.savefig("graph.png")