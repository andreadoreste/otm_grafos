import networkx as nx 
import matplotlib.pyplot as plt

#from backtrack import group_by

#nodes = ['a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#nodes = ['a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t']
nodes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
elist = [(1,2,5),(1,4,3),(2,3,9),(1,3,10),(4,5,9),(2,6,7),(6,7,8),(3,5,1),(4,10,5),(7,9,1),(10,12,4),(9,11,1),(15,2,4),(15,6,5),(5,13,2),(14,11,3),(8,12,5),(12,11,2),(16,3,1),(16,7,1),(16,9,1),(16,10,1),(17,13,3),(17,8,9),(18,4,2),(18,2,1),(18,1,3),(18,15,5),(19,6,6),(19,7,7),(20,12,1),(21,13,7)]
G = nx.Graph()

G.add_nodes_from(nodes)

G.add_weighted_edges_from(elist)

print G.edges()
#print G.nodes()
'''
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

G.add_edge('o','b',weight=4)
G.add_edge('o','f',weight=5)
G.add_edge('e','m',weight=2)
G.add_edge('i','n',weight=9)
G.add_edge('n','l',weight=3)
G.add_edge('h','k',weight=5)
G.add_edge('k','l',weight=2)

G.add_edge('p','c',weight=1)
G.add_edge('p','g',weight=1)
G.add_edge('p','i',weight=1)
G.add_edge('p','j',weight=1)
G.add_edge('q','m',weight=3)
G.add_edge('q','h',weight=9)
G.add_edge('r','d',weight=2)
G.add_edge('r','b',weight=1)
G.add_edge('r','a',weight=3)
G.add_edge('r','o',weight=5)
G.add_edge('s','f',weight=6)
G.add_edge('s','g',weight=7)
G.add_edge('t','k',weight=1)

G.add_edge('u','m',weight=7)
G.add_edge('e','u',weight=3)
G.add_edge('t','v',weight=1)
G.add_edge('v','k',weight=1)
G.add_edge('v','n',weight=2)
G.add_edge('w','g',weight=8)
G.add_edge('x','b',weight=1)
G.add_edge('x','c',weight=3)
G.add_edge('x','g',weight=4)
G.add_edge('x','f',weight=5)
G.add_edge('y','w',weight=10)
G.add_edge('z','k',weight=8)
G.add_edge('z','t',weight=3)
'''

'''
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

#print p
#nx.draw(P)
#plt.savefig("graph.png")
'''
