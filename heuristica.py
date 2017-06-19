import networkx as nx 
import graph_networkx as gnx

G = gnx.G

#adj_list = G.adjacency_list()
#print adj_list
def guloso(graph,k):
	#array que vai armazenar o resultado
	result=[]

	nodes_not_visited=graph.nodes()

	V = graph.order()
	# n = numero de vertices maximo numa particao
	n = int(round(float(V)/float(k)))
	print 'n igual'
	print n
	#edges do grafo
	edges_2 = get_edges(graph)
	#ordenando em ordem decrescente
	edges_2.sort(reverse=True,key=lambda x: x[0])
	
	
	###### mudar 1 do range para k
	
	#for i in range(k):
	k_i = 1
    
	while(k_i<=k):
	#while (len(nodes_not_visited)!=0):
		print "k_i="+str(k_i)
                #print 'iter='
                #print i
		#partition_k e o array que vai armazenar a particao do momento
		partition_k = []
		print 'nodes not visited'
		print nodes_not_visited
		if len(nodes_not_visited)>n:

			#Pega a mais pesada da aresta
			most_heavy = edges_2.pop(0)
			print most_heavy
		
			if (most_heavy[1][0] not in nodes_not_visited) or (most_heavy[1][1] not in nodes_not_visited):
				continue
                
			for h in most_heavy[1]:
				
				#most_heavy_neighboor = 0
				partition_k.append(h)
				nodes_not_visited.remove(h)
			print 'nodes not visited:'
			print nodes_not_visited
			print len(partition_k)
		
			while (len(partition_k)<n and nodes_not_visited):
			#while nodes_not_visited:
				weight = 0
				for h in partition_k:
					o = G[h]
					print o
					for i in o:
						temp = o[i]['weight']
						print weight
						if (temp>weight and i in nodes_not_visited) :
							weight = temp
							pair = (h,i,weight)
							node = i
				#partition_k.append(node)
				print pair
				print node
				print 'weight=' + str(weight)
				if node not in partition_k:
					partition_k.append(node)
					nodes_not_visited.remove(node)
				#print weight
				print partition_k
				print 'nodes not visited'
				print nodes_not_visited
			print 'over'
			result.append(partition_k)
			print result

		
		else:
			print 'nodes not visited'
			print nodes_not_visited
			partition_k = nodes_not_visited
			A = G.subgraph(partition_k)
			if nx.is_connected(A):
			#adicionar condicao aqui de ser conectado ou nao
				result.append(partition_k)
			else:
				result = False
		k_i+=1

	print result

	
def get_edges(graph):
	edges = graph.edges_iter()
	edges_r = []
	for e in edges:
		weight = graph.get_edge_data(*e)['weight']
		edges_r.append([weight,e])
	return edges_r


guloso(G,4)
