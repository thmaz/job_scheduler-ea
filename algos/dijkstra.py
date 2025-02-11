# Python program for Dijkstra's single source shortest path algorithm. 
# The program is for adjacency matrix representation of the graph
class AdjacencyGraph:

	def __init__(self, graph: list[list[int]]):
		self.V = len(graph)
		self.graph = graph
		self.dist = None

	def print_solution(self):
		print("Node \t Distance from Source")
		for node in range(self.V):
			print(node, "\t\t", self.dist[node])

	# A utility function to find the node with
	# minimum distance value, from the set of nodes
	# not yet included in shortest path tree
	def min_distance(self, sptSet):

		
		##############################
		### Initialize minimum distance as infinity
		min = float("inf")
        ##############################
		
		# Search through nodes not in the shortest path tree
		# that are less than min
		min_index = -1
		for v in range(self.V):
			##############################
			### compare node with minimum and check whether node is not in the shortest path tree
			### 	assign new minimum and minimum index
				if self.dist[v] < min and sptSet[v] == False:
					min = self.dist[v]
					min_index = v 
		return min_index

	def dijkstra(self, src):

		self.dist = [1e7] * self.V
		self.dist[src] = 0
		sptSet = [False] * self.V	# shortest path tree set

		for _ in range(self.V):

			# Pick the minimum distance node from
			# the set of nodes not yet processed.
			# u is always equal to src in first iteration
			u = self.min_distance(sptSet)

			# Put the minimum distance node in the
			# shortest path tree
			sptSet[u] = True

			# Update dist value of the adjacent vertices
			# of the picked node only if the current
			# distance is greater than new distance and
			# the node is not in the shortest path tree
			for v in range(self.V):
				if (self.graph[u][v] > 0 and sptSet[v] == False and \
					self.dist[v] > self.dist[u] + self.graph[u][v]):

					self.dist[v] = self.dist[u] + self.graph[u][v]

		self.print_solution()

graph = [
	[0, 4, 0, 0, 0, 0, 0, 8, 0],
	[4, 0, 8, 0, 0, 0, 0, 11, 0],
	[0, 8, 0, 7, 0, 4, 0, 0, 2],
	[0, 0, 7, 0, 9, 14, 0, 0, 0],
	[0, 0, 0, 9, 0, 10, 0, 0, 0],
	[0, 0, 4, 14, 10, 0, 2, 0, 0],
	[0, 0, 0, 0, 0, 2, 0, 1, 6],
	[8, 11, 0, 0, 0, 0, 1, 0, 7],
	[0, 0, 2, 0, 0, 0, 6, 7, 0]
]

# Example of a directed graph
# note that the adjacency matrix is not symmetric along the diagonal
graph2 = [
	[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,2,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,2,0,3,0,0,0,0,1,2,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,4,0,0,1,0,0,0,0,0,0,0,0],
	[0,0,0,1,0,0,0,0,0,5,2,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,1,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

g = AdjacencyGraph(graph2)

g.dijkstra(0)

# This code is contributed by Divyanshu Mehta