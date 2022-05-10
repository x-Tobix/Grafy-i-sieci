import numpy as np

from BaseAlgorithm import BaseAlgorithm


class Node2Vec(BaseAlgorithm):
    """
    Main class for Node2Vec algorithm model.
    """

    def __init__(self, adjacency_matrix, l, r, p, q, dimension):
        """
        Node2Vec constructor.
        @param adjacency_matrix: Adjacency matrix representing graph.
        @param l: The length of a single random walk.
        @param r: Number of random walks starting at a single vertex.
        @param p: Bias parameter of the random walks (Return).
        @param q: Bias parameter of the random walks (In-Out).
        """
        if dimension <= 0:
            raise Exception("Embedding dimension must be bigger than 0.")
        self.S = self.load_adjacency_matrix(adjacency_matrix)
        self.L = l
        self.R = r
        self.P = p
        self.Q = q
        self.d = dimension
        super().__init__()

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
            l = larger.pop()

            list2[s] = l
            list1[l] = list1[l] + list1[s] - 1.0
            if list1[l] < 1.0:
                smaller.append(l)
            else:
                larger.append(l)

        return list2, list1

    def create_embedding(self):
        print("Not implemented yet")
