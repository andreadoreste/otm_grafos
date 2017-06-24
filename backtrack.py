# -*- coding: utf-8 -*-

import itertools
import networkx as nx 
import time
import graph_networkx as gnx

G = gnx.G

g_nodes = G.nodes()

def backtrack(graph,k):
	#graph -> grafo
	# k -> numero de particoes
	global sol, total_weight
	sol =[]

	total_weight = 'inf'
	
	#lista de vertices:
	ent = graph.nodes()

	#determinando n a partir de k:
	n = round(float(len(ent))/float(k))
	n = int(n)
	#print 'n='+str(n)

	result = group_by(graph,ent,n)
	return [result,n]

def group_by(graph,ent,n,psol=[]):
	global total_weight
	global sol
	psol_i = list(psol)
	lista = list(ent)
	
	#caso base
	#Se o tamanho da lista for menor que n, forma a ultima particao com os elementos que sobraram (resto da divisao)	
	if len(lista)<=n:
		a = []
		while len(lista)!=0:
			
			 a.append(lista.pop())
		
		#BACKTRACK
		A = G.subgraph(a)
		if nx.is_connected(A):
			
			psol_i.append(a)
			
			#Descobrir o valor da soma das arestas entre os blocos
			weight_i = find_out_edges(psol_i,graph) 
			if weight_i<total_weight:
				total_weight= weight_i
				sol = psol_i
			else:
				pass
			
	#resto dos casos
	else:
		#comb e a combinacao dos v elementos totais, em grupos de tamanho n
		comb = itertools.combinations(lista,n)
		
		#coloca os elementos p em uma pilha
		#verificar stack
		for p in comb:
			
			stack=[]
			p = list(p)
						
			for j in p:
				lista.remove(j)
				stack.append(j)
			
			#BACKTRACK
			
			#cria subgrafo com elementos de comb
			H = G.subgraph(p)
			#verifica se o subgrafo é conexo
			
			if nx.is_connected(H):
				
				#stack=[]
				#for j in p:
				#	lista.remove(j)
				#	stack.append(j)
			
				psol_i.append(p)
				group_by(graph,lista,n,psol_i)
				#lista.extend(stack)
				psol_i.pop()
				#lista.extend(stack)
			
			else:
				pass
			lista.extend(stack)
			#print 'lista depois'
			#print lista

	return (sol,total_weight)


def find_out_edges(list_of_edges,graph):

	NG = nx.blockmodel(graph,list_of_edges)
	eg = NG.edges_iter(data=True)
	count = 0
	for e in eg:
		count+=e[2]['weight']
	return count


if __name__ == "__main__":	
	t1 = time.time()

	k = 4
	result = backtrack(G,k)
	t2 = time.time()

	total_time= t2-t1
	print "time=" + str(total_time)
	"n of nodes; k; n; partitions; min; time"
	r = str(len(G.nodes())) + ";" + str(k) + ";"+ str(result[1])+ ";" + str(result[0][0]) + ";" + str(result[0][1]) + ";" + str(total_time) + "\n"
	print r 

	newDocument = open('teste_out.txt','a')
	newDocument.write(r)
	newDocument.close()


