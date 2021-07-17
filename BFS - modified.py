# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)
		
		

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
	# Function to print a BFS of graph
	def BFS(self, s, goal): # "s" is root node 

		# Mark all the vertices as not visited
		
		visited = defaultdict()
		for i in self.graph:
			visited[i]=False
		
		# Create a queue for BFS
		queue = []

		# Mark the source node as 
		# visited and enqueue it
		queue.append(s)
		visited[s] = True
		# print(visited)

		while queue:

			# Dequeue a vertex from 
			# queue and print it
			s = queue.pop(0)
			print (s, end = " ")

			# Get all adjacent vertices of the
			# dequeued vertex s. If a adjacent
			# has not been visited, then mark it
			# visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False and i!=goal:
					queue.append(i)
					visited[i] = True
		print(goal)

# Driver code

# Create a graph given in
# the above diagram
g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
g.addEdge("Oradea","Zerind")
g.addEdge("Oradea","Sibiu")
g.addEdge("Zerind","Arad")
g.addEdge("Zerind","Oradea")
g.addEdge("Arad","Sibiu")
g.addEdge("Arad","Timisoara")
g.addEdge("Sibiu","Fagaras")
g.addEdge("Sibiu","Rimnucu Vilcea")
g.addEdge("Timisoara","Lugoj")
g.addEdge("Timisoara","Arad")
g.addEdge("Lugoj","Mehadia")
g.addEdge("Lugoj","Timisoara")
g.addEdge("Mehadia","Dobreta")
g.addEdge("Mehadia","Lugoj")
g.addEdge("Dobreta","Craiova")
g.addEdge("Dobreta","Mehadia")
g.addEdge("Craiova","Pitesti")
g.addEdge("Craiova","Dobreta")
g.addEdge("Craiova","Rimnucu Vilcea")
g.addEdge("Rimnucu Vilcea","Craiova")
g.addEdge("Rimnucu Vilcea","Pitesti")
g.addEdge("Rimnucu Vilcea","Sibiu")
g.addEdge("Pitesti","Bucharest")
g.addEdge("Pitesti","Rimnucu Vilcea")
g.addEdge("Pitesti","Craiova")
g.addEdge("Bucharest","Giurgiu")
g.addEdge("Giurgiu","Bucharest")
g.addEdge("Bucharest","Urziceni")
g.addEdge("Bucharest","Fagaras")
g.addEdge("Bucharest","Pitesti")
g.addEdge("Fagaras","Bucharest")
g.addEdge("Urziceni","Hirsova")
g.addEdge("Urziceni","Vaslui")
g.addEdge("Urziceni","Bucharest")
g.addEdge("Vaslui","lasi")
g.addEdge("Vaslui","Urziceni")
g.addEdge("lasi","Neamt")
g.addEdge("lasi","Vaslui")
g.addEdge("Neamt","lasi")
g.addEdge("Hirsova","Eforie")
g.addEdge("Hirsova","Urziceni")
g.addEdge("Eforie","Hirsova")



print ("Following is Breadth First Traversal"
				" (starting from vertex 2)")
g.BFS("Arad","Bucharest")

# This code is contributed by Neelam Yadav
