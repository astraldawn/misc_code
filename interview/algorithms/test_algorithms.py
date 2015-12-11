import unittest
from collections import defaultdict

import algorithms


class AlgorithmTest(unittest.TestCase):
    def setUp(self):
        self.e1 = [
            (0, 1),
            (1, 2), (1, 3), (1, 3),
            (2, 1), (2, 3), (2, 5),
            (3, 1),
            (4, 1),
            (5, 2)
        ]
        self.n1 = 5

    def test_adj_list(self):
        sample_adj_list = defaultdict(lambda: defaultdict(lambda: 0))
        for start, end in self.e1:
            sample_adj_list[start][end] += 1
        adj_list = algorithms.adjacency_list(self.e1)
        self.assertEquals(sample_adj_list, adj_list)

    def test_dfs(self):
        G1 = algorithms.Graph(self.n1, self.e1)