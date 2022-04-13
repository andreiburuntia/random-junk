from collections import defaultdict


parents = [] # [a,b] means that a is the parent of b

lst = ['1.2.3', '1.2.4', '1.2.5', '1.6.7', '8.9.10', '8.9.11', '8.12.13.14', '8.12.13.15']

for e in lst:
    split_nodes = e.split('.')
    for i in range(1, len(split_nodes)):
        parents.append([split_nodes[i-1], split_nodes[i]])

#print(parents)

class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=True):
        self._graph = defaultdict(set)
        self._directed = directed
        self.roots = []
        self.add_connections(connections)
        not_roots = set()
        all_elements = set()
        for c in connections:
            all_elements.add(c[0])
            all_elements.add(c[1])
            not_roots.add(c[1])
        for e in all_elements:
            if e not in not_roots:
                self.roots.append(e)

    def get_roots(self):
        return self.roots

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def draw(self):
        """ Visualize graph """

        import networkx as nx
        import matplotlib.pyplot as plt

        plt.figure(figsize=(12, 12))
        nx.draw_networkx(nx.Graph(self._graph))
        plt.show()
    
    def go(self, node, ind):
        if self.has_children(node):
            if node in self.roots:
                print(node)

            else:
                print('-' * ind + node)
            for child in self.get_children(node):
                self.go(child, ind+1)
        else:
            print('-' * ind + node)

    def has_children(self, node):
        return node in self._graph
    
    def get_children(self, node):
        return self._graph[node]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

g = Graph(parents)
print(lst)
for n in g.get_roots():
    g.go(n, 0)
#g.draw()
