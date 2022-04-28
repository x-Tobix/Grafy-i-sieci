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
        degree_m = [[0]*len(matrix)]*len(matrix)
        for i in range(0, len(matrix)):
            row_sum = 0
            for j in range(0, len(matrix)):
                row_sum += matrix[i][j]
            degree_m[i][i] == row_sum
        return degree_m
