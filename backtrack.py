# -*- coding: utf-8 -*-

import itertools
import networkx as nx 

import graph_networkx as gnx

G = gnx.G

g_nodes = G.nodes()

g_nodes = ['a','b','c','d','e','f','g','h','i','j','l']
nodes =[1,2,3,4]

sol =[]
def group_by(graph,ent,n,psol=[]):
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
			a = tuple(a)
			psol_i.append(a)
			sol.append(psol_i)
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
			stack=[]
			psol_i.append(p)
			
			for j in p:
				lista.remove(j)
				stack.append(j)
			
			#BACKTRACK
			
			#transforma de tupla para lista
			p = list(p)
			#cria subgrafo com elementos de comb
			H = G.subgraph(p)
			#verifica se o subgrafo é conexo
			if nx.is_connected(H):
				group_by(graph,lista,n,psol_i)
				#lista.extend(stack)
				psol_i.pop()
			else:
				#print p
				pass
			lista.extend(stack)
			
	return sol
a = group_by(G,g_nodes,4)
#a = group_by(nodes2,4)

newDocument = open('teste_out','a')
newDocument.write(str(a))
newDocument.close()


