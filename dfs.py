class Vertex:
    def __init__(self, data):
        self.data = data
        self.color = 0
        self.dt = 0
        self.ft = 0
        self.predecessor = None

class DFSGraph:
    def __init__(self):
        self.adj = {}
        self.time = 0

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = [v]
        else:
            self.adj[u].append(v)

    def DFS(self):
        discovered = {}
        finished = {}
        for v in self.adj.keys():
            discovered[v] = False
            finished[v] = False
        self.time = 0
        for v in self.adj.keys():
            if not discovered[v]:
                self.DFS_Visit(v, discovered, finished)

    def DFS_Visit(self, vertex, discovered, finished):
        self.time += 1
        vertex.dt = self.time
        discovered[vertex] = True
        for v in self.adj[vertex]:
            if not discovered[v]:
                self.DFS_Visit(v, discovered, finished)
        self.time += 1
        vertex.ft = self.time
        finished[vertex] = True

    def __str__(self):
        print("\n ---Adjacency List ---")
        for v in self.adj.keys():
            print(v.data, end=": ")
            for j in self.adj[v]:
                print(j.data, end=" ")
            print("\b")
        return "---End of Adjacency List ---\n"

#Testing the algorithm with the book example
if __name__ == "__main__":
    graph = DFSGraph()
    u, v, w, x, y, z = Vertex('u'), Vertex('v'), Vertex('w'), Vertex('x'), Vertex('y'), Vertex('z')
    graph.add_edge(u, v)
    graph.add_edge(u, x)
    graph.add_edge(x, v)
    graph.add_edge(v, y)
    graph.add_edge(y, x)
    graph.add_edge(w, y)
    graph.add_edge(w, z)
    graph.add_edge(z, z)

    graph.DFS()
    print("DFS Ordering:")
    for i in graph.adj.keys():
        print(f"{i.data} ({i.dt}/{i.ft}),", end=" ")
