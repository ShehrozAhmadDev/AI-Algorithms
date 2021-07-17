# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict
import sys

# This class represents a directed graph using
# adjacency list representation


class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v): #u is key v is value
		self.graph[u].append(v)

	# A function used by DFS
	def DFSUtil(self, v, visited, goal):

		# Mark the current node as visited
		# and print it
		visited.add(v)
		print(v, end=' ')

		# Recur for all the vertices
		# adjacent to this vertex
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				if neighbour != goal:
					self.DFSUtil(neighbour, visited,goal)      #recursive function
				else:
					print(goal)
					sys.exit(0)
				
				

	# The function to do DFS traversal. It uses
	# recursive DFSUtil()
	def DFS(self, v,goal):

		# Create a set to store visited vertices
		visited = set()

		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited,goal)

# Driver code


# Create a graph given
# in the above diagram
g = Graph()
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

print("Following is DFS from (starting from vertex 2)")
g.DFS("Arad","Bucharest")

# This code is contributed by Neelam Yadav
