import random
import networkx as nx 
import graph_networkx as gnx
from backtrack import find_out_edges

def get_edges(graph):
	edges = graph.edges_iter()
	edges_r = []	
	for e in edges:
		weight = graph.get_edge_data(*e)['weight']
		edges_r.append([weight,e])
	return edges_r

def guloso(graph,k):
	print 'entrou no guloso'
	#result vai armazenar o resultado
	result = []

	nodes_not_visited = graph.nodes()
	#V = numero de vertices
	V = graph.order()

	n = int(round(float(V)/float(k)))

	edges_2 = get_edges(graph)
	edges_2.sort(reverse=True,key=lambda x: x[0])
	is_there_solution = False
	###
	###Adicionar aleatoriedade de edges_2
	#### 

	k_i = 0

	while(k_i<k):
		print 'entrou no while k_i'
		partition_k = []
		A = G.subgraph(nodes_not_visited)
		if nx.is_connected(A):
			print "is connected=True"
			#Iniciando a particao
			#Escolhendo aresta aleatoria de uma lista de vertices
			random_edge = edges_2.pop(0)
			#random_edge = random.choice(edges_2)
			#edges_2.remove(random_edge)
			random_edge = random_edge[1]
			print random_edge
			if (random_edge[0] not in nodes_not_visited) or (random_edge[1] not in nodes_not_visited):
				continue
			for h in random_edge:
				partition_k.append(h)
				nodes_not_visited.remove(h)

			while (len(partition_k)<n and nodes_not_visited):
				weight = 0

				#Percorrer os vizinhos e pegar o que possui aresta de maior peso
				for h in partition_k:
					o = G[h]
					for i in o:
						temp = o[i]['weight']
						if ((temp>weight) and (i in nodes_not_visited)):
							weight = temp
							pair = (h,i,weight)
							node = i

					if node not in partition_k:
						partition_k.append(node)
						nodes_not_visited.remove(node)

			print partition_k
			print nodes_not_visited
			result.append(partition_k)
			is_there_solution = True

		else:
			is_there_solution = False
			break
			##interromper se entrar no else

		k_i+=1
	if is_there_solution:
		s= result
	else:
		s = is_there_solution
	print 'result'
	print result
	return s

def alg(graph,k):
	for i in range(100):
		guloso(graph,k)	

G= gnx.G
print alg(G,3)

