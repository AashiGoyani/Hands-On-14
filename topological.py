from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.finishing_times = {}

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, stack)
        stack.append(v)
        self.finishing_times[v] = len(self.finishing_times)

    def topological_sort(self):
        visited = set()
        stack = []
        for vertex in list(self.graph.keys()):  # Create a copy of the keys
            if vertex not in visited:
                self.dfs(vertex, visited, stack)
        sorted_vertices = sorted(stack, key=lambda x: self.finishing_times[x], reverse=True)
        return sorted_vertices


# Create the graph
graph = Graph()
graph.add_edge("shirt", "tie")
graph.add_edge("tie", "jacket")
graph.add_edge("jacket", "undershorts")
graph.add_edge("shirt", "belt")
graph.add_edge("belt", "jacket")
graph.add_edge("undershorts", "pants")
graph.add_edge("pants", "shoes")
graph.add_edge("shirt", "shoes")
graph.add_edge("watch", "shirt")
graph.add_edge("watch", "pants")

# Perform topological sort
sorted_vertices = graph.topological_sort()

# Print the order of decreasing finishing time
print("Order of decreasing finishing time:")
for vertex in sorted_vertices:
    print(vertex)

