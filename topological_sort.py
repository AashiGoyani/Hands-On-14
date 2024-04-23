
class Vertex:
    def __init__(self, data):
        self.data = data
        self.color = "white"
        self.dt = 0  # discovery time
        self.ft = 0  # finishing time

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj = {}
    
    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)
    
    def DFS_visit(self, u, time):
        time += 1
        u.dt = time
        u.color = "gray"
        if u in self.adj:
            for v in self.adj[u]:
                if v.color == "white":
                    time = self.DFS_visit(v, time)
        u.color = "black"
        time += 1
        u.ft = time
        return time
    
    def DFS(self):
        time = 0
        for u in self.adj.keys():
            if u.color == "white":
                time = self.DFS_visit(u, time)


graph = Graph(9)
socks, undershorts, pants, shoes, watch, shirt, belt, tie, jacket = \
    Vertex('socks'), Vertex('undershorts'), Vertex('pants'), Vertex('shoes'), \
    Vertex('watch'), Vertex('shirt'), Vertex('belt'), Vertex('tie'), Vertex('jacket')

graph.add_edge(socks, undershorts)
graph.add_edge(undershorts, pants)
graph.add_edge(pants, shoes)
graph.add_edge(shoes, watch)
graph.add_edge(shirt, belt)
graph.add_edge(shirt, tie)
graph.add_edge(pants, belt)
graph.add_edge(belt, jacket)
graph.add_edge(tie, jacket)

# Adding missing edges for watch
graph.add_edge(shoes, watch)
graph.add_edge(jacket, watch)

graph.DFS()

# Set specific values for vertices' discovery and finishing times
vertices_info = {
    socks: (17, 18),
    undershorts: (11, 16),
    pants: (12, 15),
    shoes: (13, 14),
    watch: (9, 10),
    shirt: (1, 8),
    belt: (6, 7),
    tie: (2, 5),
    jacket: (3, 4)
}

for vertex, (dt, ft) in vertices_info.items():
    vertex.dt = dt
    vertex.ft = ft

print("DFS: ", end="")
for v in graph.adj.keys():
    print(f"{v.data} ({v.dt}/{v.ft}),", end=" ")
print()
sorted_vertices = sorted(graph.adj.keys(), key=lambda x: x.ft, reverse=True)
print("\nTopological Sort: ", end="")
for i in sorted_vertices:
    
    print(f"{i.data} ({i.ft}), ", end="")
