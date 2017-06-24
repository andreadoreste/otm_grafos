# -*- coding: utf-8 -*-

import networkx as nx 
import graph_networkx as gnx
import itertools
import operator
import random
import copy
import sets

def main(k,graph,edge_list_origin):
	r = heuristica(k,graph,edge_list_origin)
	result =find_out_edges(r,graph)
	return result

def find_out_edges(list_of_edges,graph):

	NG = nx.blockmodel(graph,list_of_edges)
	eg = NG.edges_iter(data=True)
	count = 0
	for e in eg:
		count+=e[2]['weight']
	return count
	print 'count'
	print count


def heuristica(k,graph,edge_list_origin):
	result = []
	V=graph.order()	
	# n = numero de vertices maximo numa particao
	n = int(round(float(V)/float(k)))

	nodes_visited = []
	
	edge_list_origin.sort(key=lambda x:x[2])
	t =[]
	for key,group in itertools.groupby(edge_list_origin, operator.itemgetter(2)):
		t.append(list(group))
	
	#Arestas de custo igual separados em listas diferentes
	edge_list = copy.deepcopy(t)
	p = []
	while (nodes_visited>n):
	
		#p = lista de arestas de menor custo
		if not(p):
			 
			p = edge_list.pop(0)
			print edge_list
			print "P"
			print p	
		
		#Escolhe aleatoriamente uma aresta da lista de p
		i_edge = random.choice(p)
		p.remove(i_edge)	
		
		i_edge_t = (i_edge[0],i_edge[1])
		
		if graph.has_edge(*i_edge_t): 	
			graph.remove_edge(*i_edge_t)
		else:
			continue

		#Se os vertices da arestas já estiver nos nos visitados, não faz nada
		if((i_edge_t[0] in nodes_visited)and (i_edge_t[1] in nodes_visited)):
			continue

		elif (nx.is_connected(graph)):
			pass
		else:
			
			connected_components = nx.connected_components(graph)
			
			size_components = []
			con_components = []
			for i in connected_components:
				con_components.append(i)
				print i
				print len(i)
				size_components.append(len(i))

			if n in size_components:
				
				i = size_components.index(n)
				
				result.append(con_components[i])
				nodes_visited.extend(con_components[i])
				for v in con_components[i]:
					graph.remove_node(v)
				
				#reinicia arestas
				edge_list = copy.deepcopy(t)
				print 'result='
				print result

			else:
				graph.add_edge(i_edge[0],i_edge[1],weight=i_edge[2])	
	return result


if __name__ == "__main__":
	G = gnx.G
	edge_list = gnx.elist
	main(3,G,edge_list)