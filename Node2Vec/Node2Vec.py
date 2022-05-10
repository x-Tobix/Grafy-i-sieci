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

    def create_embedding(self):
        print("Not implemented yet")
