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
		self.distance = defaultdict()

	# function to add an edge to graph
	def addEdge(self, u, v): #u is key v is value
		self.graph[u].append(v)

	def addval(self,city,cost):
		self.distance[city] = cost

	def Pqueue(self,city):
		self.queue = []
		dist = []
		for neighbor in self.graph[city]:
			dist.append(self.distance[neighbor])
		dist.sort()
		for cost in dist:
			self.queue.append(cost)

	# A function used by DFS
	def DFSUtil(self, v, visited, goal):

		# Mark the current node as visited
		# and print it

		visited.add(v)
		print(v, end=' ')
		self.Pqueue(v)
		city = self.get_key(self.queue.pop(0))

		if city not in visited:
			if city != goal:
				self.DFSUtil(city, visited,goal)      #recursive function
			else:
				print(goal)
				sys.exit(0)
		# Recur for all the vertices
		# adjacent to this vertex
		
		# for neighbour in self.graph[v]:
				
				

	# The function to do DFS traversal. It uses
	# recursive DFSUtil()
	def DFS(self, v,goal):

		# Create a set to store visited vertices
		visited = set()

		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited,goal)

	def get_key(self,val):
		for key, value in self.distance.items():
			if val == value:
				return key
		return "key doesn't exist"

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
g.addEdge("Sibiu","Rimnicu Vilcea")
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
g.addEdge("Craiova","Rimnicu Vilcea")
g.addEdge("Rimnicu Vilcea","Craiova")
g.addEdge("Rimnicu Vilcea","Pitesti")
g.addEdge("Rimnicu Vilcea","Sibiu")
g.addEdge("Pitesti","Bucharest")
g.addEdge("Pitesti","Rimnicu Vilcea")
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
g.addval("Arad",366)
g.addval("Bucharest",0)
g.addval("Craiova",160)
g.addval("Dobreta",242)
g.addval("Eforie",161)
g.addval("Fagaras",176)
g.addval("Giurgiu",77)
g.addval("Hirsova",151)
g.addval("lasi",226)
g.addval("Lugoj",244)
g.addval("Mehadia",241)
g.addval("Neamt",234)
g.addval("Oradea",380)
g.addval("Pitesti",101)
g.addval("Rimnicu Vilcea",193)
g.addval("Sibiu",253)
g.addval("Timisoara",329)
g.addval("Urziceni",80)
g.addval("Vaslui",199)
g.addval("Zerind",374)

print("Following is DFS from (starting from vertex 2)")
g.DFS("Arad","Bucharest")
