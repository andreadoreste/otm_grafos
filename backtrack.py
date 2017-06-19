# -*- coding: utf-8 -*-
#from numba import jit
import itertools
import networkx as nx 
import time
import graph_networkx as gnx

G = gnx.G
#G = nx.karate_club_graph()

g_nodes = G.nodes()
#g_nodes = G.nodes()

#g_nodes = ['a','b','c','d','e','f','g','h','i','j','l']
nodes =[1,2,3,4,5]
#global total_weight
#total_weight = 1000000
#total_weight = 'inf'
#global sol
#sol =[]

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
	print 'n='+str(n)

	result = group_by(graph,ent,n)
	return [result,n]

def group_by(graph,ent,n,psol=[]):
	#print 'entrou no group_by'
	global total_weight
	global sol
	psol_i = list(psol)
	lista = list(ent)
	#print 'psol_i_inicial'
	#print psol_i
	#numero maximo de elementos em cada particao
	#n = teto(|V|/k)
	#n = round(float(len(lista))/float(k))
	#n = int(n)
	#copia da lista
	#lista = list(ent)

	#caso base
	#Se o tamanho da lista for menor que n, forma a ultima particao com os elementos que sobraram (resto da divisao)	
	#print 'len'
	#print len(lista)
	#print lista
	if len(lista)<=n:
		#print "entrando no len<n"
		a = []
		while len(lista)!=0:
			
			 a.append(lista.pop())
		
		#BACKTRACK
		A = G.subgraph(a)
		if nx.is_connected(A):
			#a = tuple(a)
			psol_i.append(a)
			#sol.append(psol_i)

			#Descobrir o valor da soma das arestas entre os blocos
			#print 'psol_i ='
			#print psol_i
			weight_i = find_out_edges(psol_i,graph) 
			#print 'weight_i'
			#print weight_i
			#print psol_i
			if weight_i<total_weight:
				total_weight= weight_i
				sol = psol_i
				#sol.append(psol_i)
				#print "total_weight"
				#print total_weight
		else:
			pass
			#print a
	#resto dos casos
	else:
		#comb e a combinacao dos v elementos totais, em grupos de tamanho n
		comb = itertools.combinations(lista,n)
		
		#coloca os elementos p em uma pilha
		#verificar stack
		for p in comb:
			#print 'entrou no for'
			stack=[]
			p = list(p)
			#psol_i.append(p)
			
			for j in p:
				lista.remove(j)
				stack.append(j)
			
			#BACKTRACK
			#print 'lista antes'
			#print lista
			#cria subgrafo com elementos de comb
			H = G.subgraph(p)
			#verifica se o subgrafo é conexo
			#print p
			if nx.is_connected(H):
				#print 'p is connected'
				#print p
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
				#print p
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
	print 'count'
	print count
'''
t1 = time.time()
#a = group_by(G,g_nodes,7)
k = 3
result = backtrack(G,k)
t2 = time.time()
#a = group_by(nodes2,4)
#print a
total_time= t2-t1
print "time=" + str(total_time)
"n of nodes; k; n; partitions; min; time"
r = str(len(G.nodes())) + ";" + str(k) + ";"+ str(result[1])+ ";" + str(result[0][0]) + ";" + str(result[0][1]) + ";" + str(total_time) + "\n"
print r 

newDocument = open('teste_out.txt','a')
newDocument.write(r)
newDocument.close()
'''

