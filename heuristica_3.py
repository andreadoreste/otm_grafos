import networkx as nx 
import graph_networkx as gnx


def heuristica(k,graph,edge_list):
	#Precisa fazer uma copia?
	edge_list.sort(key=lambda x:x[2])
	print edge_list
	i_edge = edge_list.pop(0)
	print i_edge
	i_edge_t = (i_edge[0],i_edge[1])
	print i_edge
	graph.remove_edge(*i_edge_t)
	if nx.is_connected(graph):
		print 'is connected'
		pass
	else:
		graph.add_edge(i_edge[0],i_edge[1],weight=i_edge[2])

G = gnx.G
edge_list = gnx.elist
#print edge_list
heuristica(3,G,edge_list)