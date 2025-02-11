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
				if self.dist[v] < min and sptSet[v] == false:
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

# This code is contributed by Divyanshu Mehta