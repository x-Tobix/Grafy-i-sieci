import numpy as np
from BaseAlgorithm import BaseAlgorithm


class Node2Vec(BaseAlgorithm):
    """
    Main class for Node2Vec algorithm model.
    """

    def __init__(self, g, adjacency_matrix, le, r, p, q, dimension):
        """
        Node2Vec constructor.
        @param adjacency_matrix: Adjacency matrix representing graph.
        @param le: The length of a single random walk.
        @param r: Number of random walks starting at a single vertex.
        @param p: Bias parameter of the random walks (Return).
        @param q: Bias parameter of the random walks (In-Out).
        """
        if dimension <= 0:
            raise Exception("Embedding dimension must be bigger than 0.")
        self.S = self.load_adjacency_matrix(adjacency_matrix)
        self.L = le
        self.R = r
        self.P = p
        self.Q = q
        self.d = dimension
        self.G = g
        super().__init__()

    def get_alias_edge(self, source, other):
        """
        Get alias edge based on normalized probabilities.
        @param source: Source node.
        @param other: Node on the other end of the edge.
        :return list: Utility list from normalized probabilities
        """

        probabilities = []
        for neighbor in sorted(self.G.neighbors(other)):
            if neighbor == source:
                probabilities.append(1 / self.P)
            elif not self.G.has_edge(neighbor, source):
                probabilities.append(1 / self.Q)
            else:
                probabilities.append(1)
        normalized_probabilities = [float(probability) / sum(probabilities) for probability in probabilities]

        return self.create_utility_lists(normalized_probabilities)

    @staticmethod
    def create_utility_lists(probabilities):
        """
        Compute utility lists for non-uniform sampling from discrete distributions using Alias Sampling method.
        @param probabilities: List of normalized probabilities.
        :return p,list1: Lists of samplings.
        """
        list1 = np.zeros(len(probabilities))
        list2 = np.zeros(len(probabilities), dtype=np.int)
        smaller = []
        larger = []
        for i in range(0, len(probabilities)):
            list1[i] = len(probabilities) * probabilities[i]
            if list1[i] < 1.0:
                smaller.append(i)
            else:
                larger.append(i)

        while len(smaller) > 0 and len(larger) > 0:
            s = smaller.pop()
            la = larger.pop()

            list2[s] = la
            list1[la] = list1[la] + list1[s] - 1.0
            if list1[la] < 1.0:
                smaller.append(la)
            else:
                larger.append(la)

        return list2, list1

    def create_embedding(self):
        print("Not implemented yet")
