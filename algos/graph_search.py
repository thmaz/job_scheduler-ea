from collections import defaultdict
 
class LIFO:
    def __init__(self):
        self._data = []
        pass
    def push(self, val):
        self._data.append(val)
        pass
    def get(self, idx):
        return self._data[idx]
        pass
    def __len__(self):
        return len(self._data)
        pass
    def pop(self):
        return self._data.pop(-1)
        pass

class FIFO:
    def __init__(self):
        self._data = []
        pass
    def push(self, val):
        self._data.append(val)
        pass
    def get(self, idx):
        return self._data[idx]
        pass
    def __len__(self):
        return len(self._data)
        pass
    def pop(self):
        return self._data.pop(0)
        pass


# This class represents an undirected graph
class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)      # init dictionary of empty lists
 
    # Function to add an undirected edge to graph
    def add_edge(self, u: int, v: int):
        ##############################
        ### add an edge by appending v to the list of graph[u] and vice versa 
        ### write code here

        self.graph[u].append[v]
        self.graph[v].append[u]
        
        ##############################
        pass
    
    def traversal(self, initial_node: int, algorithm='bfs'):
        
        frontier = None
        ##############################
        ### if algorithm is 'bfs', initialize frontier as a FIFO
        ### if algorithm is 'dfs', initialize frontier as a LIFO
        ### write code here
        
        if algorithm == 'bfs':
            frontier = FIFO()
        elif algorithm == 'dfs':
            frontier = LIFO()

        ##############################
                
        frontier.push(initial_node)         # push initial node into frontier
        reached = [initial_node]            # initial node is already reached

        while len(frontier) != 0:           # continue until the queue is empty
            
            node = frontier.pop()           # get first node in queue
            print(node, end=' ')            # print this node

            for child in self.graph[node]:  # iterate through children of node
                ##############################
                ### if child is not yet reached, 
                ###     append it in the reached list
                ###     push child into FIFO/LIFO queue
                ### write code here
                if child != 
                ##############################
                pass