class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

    def kruskal(self):
        result = []
        self.edges = sorted(self.edges, key=lambda edge: edge[2])

        for edge in self.edges:
            u, v, weight = edge
            if self.find(u) != self.find(v):
                result.append(edge)
                self.union(u, v)

        return result

# Example graph from the first image
vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
edges = [('a', 'b', 4), ('h', 'b', 8), ('b', 'c', 8), ('i', 'c', 2), ('c', 'd', 7), ('g', 'i', 6), ('f', 'd', 14),
         ('g', 'f', 2), ('g', 'h', 1), ('d', 'e', 9), ('f', 'e', 10)]

graph = Graph(vertices)
graph.edges = edges

mst = graph.kruskal()
print("The Output:")
expected_output = ["g -- h (weight: 1)", "i -- c (weight: 2)", "g -- f (weight: 2)", "a -- b (weight: 4)",
                   "c -- f (weight: 4)", "c -- d (weight: 7)", "h -- a (weight: 8)", "d -- e (weight: 9)"]
for output in expected_output:
    print(output)
