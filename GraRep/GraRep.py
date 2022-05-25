from math import log

from numpy import matmul, sqrt, diag
from numpy.linalg import linalg

from BaseAlgorithm import BaseAlgorithm


class GraRep(BaseAlgorithm):
    """
    Main class for GraRep algorithm model.
    """

    def __init__(self, adjacency_matrix, max_transition_step: int, dimension: int):
        """
        GraRep constructor.
        @param max_transition_step: Maximum number of steps to collect structural data.
        @param adjacency_matrix: Adjacency matrix representing graph.
        @param dimension: Dimension of representation vector.
         """
        if max_transition_step <= 0:
            raise Exception("Maximum transition step must be bigger than 0")
        if dimension <= 0:
            raise Exception("Embedding dimension must be bigger than 0")
        self.K = max_transition_step
        self.S = self.load_adjacency_matrix(adjacency_matrix)
        self.d = dimension
        super().__init__()

    def create_embedding(self):
        """
        Creates embedding from a graph based on GraRep algorithm
        :return w: Created embedding.
        """
        a = self.get_k_step_transition_probability_matrices(self.S, self.K)
        w = []
        for k in range(0, self.K):
            x_k = self.get_positive_log_probability_matrix(a[k], 1./len(self.S))
            u, sigma, _ = linalg.svd(x_k)
            sigma_d = diag(sigma[:self.d])
            u_d = u[:, :self.d]
            w.append(matmul(u_d, sqrt(sigma_d)).tolist())
        return self.matrix_mean(w)

    def get_k_step_transition_probability_matrices(self, adjacency_matrix, max_transition):
        """
        Calculates vector of k-step transition probability matrices.
        :param adjacency_matrix: Ady adjacency matrix.
        :param max_transition: Maximum number of transitions.
        :return matrices: Vector of k-step transition probability matrices.
        """
        i = -1
        for row in adjacency_matrix:
            i += 1
            if len(row) != len(adjacency_matrix):
                raise Exception("Given table is not a quadratic matrix.")
            j = -1
            for column in row:
                j += 1
                if not (column in [0, 1]) or column != adjacency_matrix[i][j]:
                    raise Exception("Given table is not a adjacency matrix.")
        matrices = []
        inv_degree_matrix = self.inverse_matrix(self.degree_matrix(adjacency_matrix))
        base_matrix = self.matrix_multiply(inv_degree_matrix, adjacency_matrix)
        matrices.append(base_matrix)
        for i in range(1, max_transition):
            matrices.append(self.matrix_multiply(matrices[i-1], base_matrix))
        return matrices

    @staticmethod
    def get_positive_log_probability_matrix(transition_probability_matrix, log_shifted_factor):
        """
        Calculates positive log probability matrix.
        :param transition_probability_matrix: Transition probability matrix.
        :param log_shifted_factor: Value which logarithm will be subtracted from each field in matrix.
        :return matrix: Log probability matrix where negative values where changed to zeros.
        """
        for row in transition_probability_matrix:
            if len(row) != len(transition_probability_matrix):
                raise Exception("Given table is not a quadratic matrix.")
        gamma = []
        for j in range(0, len(transition_probability_matrix)):
            gamma_j = 0
            for p in range(0, len(transition_probability_matrix)):
                gamma_j += transition_probability_matrix[p][j]
            gamma.append(gamma_j)
        matrix = []
        for i in range(0, len(transition_probability_matrix)):
            current = []
            for k in range(0, len(transition_probability_matrix)):
                if transition_probability_matrix[i][k] == 0:
                    current.append(0)
                else:
                    current.append(max(log(transition_probability_matrix[i][k] / gamma[k]) - log(log_shifted_factor), 0))
            matrix.append(current)
        return matrix
