import queue
import networkx as nx
import matplotlib.pyplot as plt
import random

#Configs
SPARES_RATIO = 0.2


def randTreeGenerator(numVertices: int, maxChild : int = 0):	

	if numVertices<=0:
		return {}

	numVertices-=1

	#set the default maxChild if not given
	if maxChild == 0:
		maxChild = int(numVertices * SPARES_RATIO)

	#put the root node onto the graph
	graph = {0:[]}
	currentNumVertices=1

	#create a queue and enqueue root node
	toVisit = queue.SimpleQueue()
	toVisit.put(0)
	
	while toVisit.empty()==False and currentNumVertices <= numVertices:
		node = toVisit.get()
		numChild = int(min(random.random()*maxChild,numVertices-currentNumVertices))		
		if numChild == 0:
			children = []
			if toVisit.empty() and currentNumVertices <= numVertices:
				graph.update({node:[currentNumVertices]})
				toVisit.put(currentNumVertices)
				currentNumVertices += 1
		else:
			children = list(range(currentNumVertices, currentNumVertices+numChild))
			graph.update({node:children})
			for child in children:
				toVisit.put(child)
			currentNumVertices+=numChild		
	return graph

def drawGraph(graph:dict):
	G=nx.Graph()
	for key in graph:
		for child in graph[key]:
			G.add_edge(key,child)
	print("Nodes of graph: ")
	print(G.nodes())
	print("Edges of graph: ")
	print(G.edges())

	nx.draw(G, with_labels=True)
	plt.savefig("simple_path.png") # save as png
	plt.show() # display

graph = randTreeGenerator(30)
print(graph)
drawGraph(graph)