import sys
from collections import defaultdict, deque

# Begin Data #
e1 = [
    (0, 1), (0, 3), (0, 5),
    (1, 2), (1, 3), (1, 3),
    (2, 1), (2, 3), (2, 5),
    (3, 5),
    (4, 1),
    (5, 2)
]
n1 = 6


# End data #

def adjacency_list(edges):
    adj_list = defaultdict(lambda: defaultdict(lambda: 0))
    for start, end in edges:
        adj_list[start][end] += 1
    return adj_list


class Graph:
    def __init__(self, n_nodes, edges):
        self.adj_list = adjacency_list(edges)
        self.nodes = n_nodes
        self.vis = {}
        self.dist = {}
        self.output = []

    def reset(self):
        self.vis = {}
        self.dist = {}
        for i in range(0, self.nodes):
            self.dist[i] = sys.maxint
        self.output = []

    def print_case(self, str, print_dist=False):
        print str, self.output
        if print_dist:
            for (k, v) in self.dist.iteritems():
                print k, v
        print
        self.reset()

    def dfs(self, cur_node):
        if cur_node in self.vis:
            return
        self.vis[cur_node] = 1
        self.output.append(cur_node)
        for node in self.adj_list[cur_node]:
            self.dfs(node)

    # Using a list as stack
    def dfs_iterative(self, start_node):
        stack = list()
        stack.append(start_node)
        while stack:
            cur_node = stack.pop()
            if cur_node in self.vis:
                pass
            else:
                self.output.append(cur_node)
                self.vis[cur_node] = 1
                for node in self.adj_list[cur_node]:
                    stack.append(node)

    # Using a deque as a queue
    def bfs(self, start_node):
        queue = deque()
        queue.append(start_node)
        self.dist[start_node] = 0
        while queue:
            cur_node = queue.popleft()
            if cur_node in self.vis:
                pass
            else:
                self.output.append(cur_node)
                self.vis[cur_node] = 1
                for node in self.adj_list[cur_node]:
                    node_dist = self.dist[cur_node] + 1
                    if node_dist < self.dist[node]:
                        self.dist[node] = node_dist
                        queue.append(node)


G1 = Graph(n1, e1)

G1.dfs(0)
G1.print_case("DFS recursive")
G1.dfs_iterative(0)
G1.print_case("DFS iterative")
G1.bfs(0)
G1.print_case("BFS", True)
