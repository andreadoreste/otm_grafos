import networkx as nx 
import matplotlib.pyplot as plt

#from backtrack import group_by

nodes = [1,2,3,4,5,6,7,8,9,10,11]
#nodes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
elist = [(1,2,5),(1,4,3),(2,3,9),(1,3,10),(4,5,9),(2,6,7),(6,7,8),(3,5,1),(4,10,5),(7,9,1),(10,8,4),(8,9,2),(9,11,1)]

G = nx.Graph()

G.add_nodes_from(nodes)

#G.add_weighted_edges_from(elist)

G.add_edge(1,2, weight=5) 
G.add_edge(1,4, weight=6) 
G.add_edge(2,3, weight=9) 
G.add_edge(1,3,weight=10) 
G.add_edge(4,5,weight=9) 
G.add_edge(2,6,weight=7) 
G.add_edge(6,7,weight=8) 
G.add_edge(3,5,weight=1) 
G.add_edge(4,10,weight=5) 
G.add_edge(7,9,weight=1) 
G.add_edge(10,8,weight=4) 
G.add_edge(8,9,weight=2) 
G.add_edge(9,11,weight=1) 
'''
G.add_edge(15,2,weight=4)
G.add_edge(15,6,weight=5)
G.add_edge(5,13,weight=2)
G.add_edge(9,14,weight=9)
G.add_edge(14,11,weight=3)
G.add_edge(8,12,weight=5)
G.add_edge(12,11,weight=2)

G.add_edge(16,3,weight=1)
G.add_edge(16,7,weight=1)
G.add_edge(16,9,weight=1)
G.add_edge(16,10,weight=1)
G.add_edge(17,13,weight=3)
G.add_edge(17,8,weight=9)
G.add_edge(18,4,weight=2)
G.add_edge(18,2,weight=1)
G.add_edge(18,1,weight=3)
G.add_edge(18,15,weight=5)
G.add_edge(19,6,weight=6)
G.add_edge(19,7,weight=7)
G.add_edge(20,12,weight=1)

G.add_edge(21,13,weight=7)
G.add_edge(5,21,weight=3)
G.add_edge(20,22,weight=1)
G.add_edge(22,12,weight=1)
G.add_edge(22,14,weight=2)
G.add_edge(23,7,weight=8)
G.add_edge(24,2,weight=1)
G.add_edge(24,3,weight=3)
G.add_edge(24,7,weight=4)
G.add_edge(24,6,weight=5)
G.add_edge(25,23,weight=10)
G.add_edge(26,12,weight=8)
G.add_edge(26,20,weight=3)
'''
