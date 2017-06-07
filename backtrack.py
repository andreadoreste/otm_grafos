import itertools
import networkx as nx 

import graph_networkx as gnx

G = gnx.G

g_nodes = G.nodes()

g_nodes = ['a','b','c','d','e','f','g','h','i','j','l']
nodes =[1,2,3,4]
global psol
#psol = []
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
		
	if len(lista)<=n:
		#print lista
		a = []
		while len(lista)!=0:
			#print i
			 a.append(lista.pop())
		
		#print "a= "
		#print a
		A = G.subgraph(a)
		if nx.is_connected(A):
			a = tuple(a)
			psol_i.append(a)
			#print 'psol len<n'
		#print psol
		#print 'psol_i'
		#print psol_i
			sol.append(psol_i)
		else:
		#return psol
			print a
	else:
		comb = itertools.combinations(lista,n)
		for p in comb:
			stack=[]
			psol_i.append(p)
			
			for j in p:
				lista.remove(j)
				stack.append(j)
			#print 'psol antes de chamar a recursiva'
			#print psol

			#BACKTRACK
			
			p = list(p)
			H = G.subgraph(p)
			if nx.is_connected(H):
				group_by(graph,lista,n,psol_i)
				#lista.extend(stack)
				psol_i.pop()
			else:
				print p
				#pass
			lista.extend(stack)
			#print lista
	#print 'psol final'
	#print psol
	#psol = []
	#print sol
	return sol
a = group_by(G,g_nodes,4)
#a = group_by(nodes2,4)

newDocument = open('teste_out','a')
newDocument.write(str(a))
newDocument.close()


