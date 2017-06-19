import random
import networkx as nx 
import graph_networkx as gnx
from backtrack import find_out_edges



def alg(graph,k):
	c= 0
	for i in range(100):
		try:
			print "entrou no try"
			r = guloso(graph,k)
			print r
		except:
			print "There is no result"	
			r = False

	#if r!=False:
	#	c = find_out_edges(r,graph)
	#else:
	#	c = False
		
	#return c	


def guloso(graph,k):
	print "entrou no guloso"
	#array que vai armazenar o resultado
	result=[]

	nodes_not_visited=graph.nodes()

	V = graph.order()
	print "V: " + str(V)
	# n = numero de vertices maximo numa particao
	n = int(round(float(V)/float(k)))
	print "n: " + str(n)
	#edges do grafo
	edges_2 = get_edges(graph)
	#ordenando em ordem decrescente
	edges_2.sort(reverse=True,key=lambda x: x[0])
	print "edges_2 sort"
	
	###### mudar 1 do range para k
	
	k_i = 0
    
	while(k_i<=k):
		print "entrou no while k"
		#partition_k e o array que vai armazenar a particao do momento
		partition_k = []
		if len(nodes_not_visited)>n:
			print nodes_not_visited
			#Pega a mais pesada da aresta
			#most_heavy = edges_2.pop(0)
			most_heavy = random.choice(edges_2)
			edges_2.remove(most_heavy)
			#print most_heavy

			if (most_heavy[1][0] not in nodes_not_visited) or (most_heavy[1][1] not in nodes_not_visited):
				continue
                
			for h in most_heavy[1]:
				
				partition_k.append(h)
				nodes_not_visited.remove(h)
		
			while (len(partition_k)<n and nodes_not_visited):
				weight = 0
				for h in partition_k:
					o = G[h]
					for i in o:
			#			print nodes_not_visited
			#			print 'i: ' + str(i)
			#			if i in nodes_not_visited:
			#				print True
						temp = o[i]['weight']
						if ((temp>weight) and (i in nodes_not_visited)) :
							#print 'i: ' + str(i)
			#				print result
							weight = temp
							pair = (h,i,weight)
							node = i
				print 'weight=' + str(weight)
				if weight==0:
					print 'partition_k'
					print partition_k
					nodes_not_visited.extend(partition_k)
					break
				if node not in partition_k and nodes_not_visited:
			#		print 'not in'
			#		print node
					partition_k.append(node)
			#		print partition_k
					nodes_not_visited.remove(node)
			#print nodes_not_visited
			#print partition_k
			result.append(partition_k)
			#print result
		
		else:
			print 'entrando no else'
			partition_k = nodes_not_visited
			A = G.subgraph(partition_k)
			if nx.is_connected(A):
			#adicionar condicao aqui de ser conectado ou nao
				result.append(partition_k)
				#result.append(A)
			else:
				result = False
		k_i+=1
		print k
	return result

	
def get_edges(graph):
	edges = graph.edges_iter()
	edges_r = []	
	for e in edges:
		weight = graph.get_edge_data(*e)['weight']
		edges_r.append([weight,e])
	return edges_r

G = gnx.G
print "G is loaded"
#print guloso(G,3)
print alg(G,6)