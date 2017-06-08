# -*- coding: utf-8 -*-

import itertools
import networkx as nx 

import graph_networkx as gnx

G = gnx.G

g_nodes = G.nodes()

g_nodes = ['a','b','c','d','e','f','g','h','i','j','l']
nodes =[1,2,3,4,5]
global total_weight
total_weight = 1000000
global sol
sol =[]
def group_by(graph,ent,n,psol=[]):
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
	if len(lista)<=n:
		
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
			print 'psol_i ='
			print psol_i
			weight_i = find_out_edges(psol_i,graph) 
			print 'weight_i'
			print weight_i
			print psol_i
			if weight_i<total_weight:
				total_weight= weight_i
				sol = psol_i
				#sol.append(psol_i)
				print "total_weight"
				print total_weight
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
			#stack=[]
			p = list(p)
			#psol_i.append(p)
			
			#for j in p:
			#	lista.remove(j)
			#	stack.append(j)
			
			#BACKTRACK
			
			#cria subgrafo com elementos de comb
			H = G.subgraph(p)
			#verifica se o subgrafo é conexo
			if nx.is_connected(H):
				stack=[]
				for j in p:
					lista.remove(j)
					stack.append(j)
			
				psol_i.append(p)
				group_by(graph,lista,n,psol_i)
				#lista.extend(stack)
				psol_i.pop()
				lista.extend(stack)
			
			else:
				#print p
				pass
			#lista.extend(stack)
			
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

a = group_by(G,g_nodes,4)
#a = group_by(nodes2,4)
print a
newDocument = open('teste_out.txt','w')
newDocument.write(str(a))
newDocument.close()


