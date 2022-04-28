import numpy

from BaseAlgorithm import BaseAlgorithm


class GraRep(BaseAlgorithm):
    """
    Main class for GraRep algorithm model.
    """

    def __init__(self,
                 max_transition_step: int):
        """
        GraRep constructor
        @param max_transition_step: Maximum number of steps to collect structural data
         """
        self.K = max_transition_step
        super().__init__()

    def create_embedding(self):
        """
        Creates embedding from a graph based on GraRep algorithm
        """

    @staticmethod
    def degree_matrix(matrix):
        """
        Calculates degree matrix for given adjacency matrix.
        :param matrix: Matrix (list of lists) to inverse.
        :return degree_matrix: Degree matrix.
        """
        for row in matrix:
            if len(row) is not len(matrix):
                raise Exception("Given table is not a quadratic matrix.")
        degree_m = [[0] * len(matrix)] * len(matrix)
        for i in range(0, len(matrix)):
            row_sum = 0
            for j in range(0, len(matrix)):
                row_sum += matrix[i][j]
            degree_m[i][i] == row_sum
        return degree_m

    def get_k_step_transition_probability_matrices(self, adjacency_matrix, max_transition):
        """
        Calculates vector of k-step transition probability matrices.
        :param adjacency_matrix: Ady adjacency matrix.
        :param max_transition: Maximum number of transitions.
        :return matrices: Vector of k-step transition probability matrices.
        """
        for row in adjacency_matrix:
            if len(row) is not len(adjacency_matrix):
                raise Exception("Given table is not a quadratic matrix.")
            for column in row:
                if column is not 0 or column is not 1 or column is not adjacency_matrix[column][row]:
                    raise Exception("Given table is not a adjacency matrix.")
        matrices = []
        inv_degree_matrix = self.inverse_matrix(self.degree_matrix(adjacency_matrix))
        base_matrix = numpy.dot(inv_degree_matrix, adjacency_matrix)
        matrices.append(base_matrix)
        for i in range(1, max_transition):
            matrices.append(numpy.dot(matrices[i-1], base_matrix))
        return matrices
