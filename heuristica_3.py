import networkx as nx 
import graph_networkx as gnx




def heuristica(k,graph,edge_list_origin):
	result = []
	V=graph.order()	
	# n = numero de vertices maximo numa particao
	n = int(round(float(V)/float(k)))

	#Precisa fazer uma copia?
	nodes_visited = []
	
	edge_list_origin.sort(key=lambda x:x[2])
	edge_list = list(edge_list_origin)
	print edge_list
	
	while (nodes_visited>n):
	
		i_edge = edge_list.pop(0)
		print i_edge
		i_edge_t = (i_edge[0],i_edge[1])
		
		if graph.has_edge(*i_edge_t): 	
			graph.remove_edge(*i_edge_t)
		else:
			continue

		if((i_edge_t[0] in nodes_visited)and (i_edge_t[1] in nodes_visited)):
			continue
		elif ((i_edge_t[0] or i_edge_t[1])in nodes_visited) and ((i_edge_t[0] or i_edge_t[1]) not in nodes_visited):
			print 'FUDEU'


		elif (nx.is_connected(graph)):
			print 'is connected'
			pass
		else:
			connected_components = nx.connected_components(graph)
			print connected_components
			size_components = []
			con_components = []
			for i in connected_components:
				con_components.append(i)
				print i
				print len(i)
				size_components.append(len(i))

			if n in size_components:
				print n
				print size_components
				i = size_components.index(n)
				print 'i: '+str(i)
				print type(i)
				#for i in con_components:
				#	print i
				result.append(con_components[i])
				print con_components[i]
				nodes_visited.extend(con_components[i])
				for v in con_components[i]:
					graph.remove_node(v)
				#reinicia arestas
				edge_list = list(edge_list_origin)
				print 'result='
				print result
			else:
				graph.add_edge(i_edge[0],i_edge[1],weight=i_edge[2])	

	print result
	print graph.nodes()


'''
			graph.add_edge(i_edge[0],i_edge[1],weight=i_edge[2])
			print 'not connected'

		if ((i_edge_t[0] or i_edge_t[1])in nodes_visited) and ((i_edge_t[0] or i_edge_t[1]) not in nodes_visited):
			print 'FUDEU'
'''

G = gnx.G
edge_list = gnx.elist
#print edge_list
heuristica(4,G,edge_list)