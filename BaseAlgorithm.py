import numpy


class BaseAlgorithm(object):
    """
    Base class for used algorithms.
    """

    def __init__(self):
        """
        Base Algorithm class constructor
        """
        self.nodes = []

    def load_nodes(self, path_to_nodes):
        """
        Load nodes.
        :param path_to_nodes: Adjacency matrix in csv format.
        """
        with open(path_to_nodes, "rb") as file:
            graph = file.readlines()

        for i in range(len(graph)):
            self.nodes.append(i)

    @staticmethod
    def load_adjacency_matrix(path_to_matrix):
        """
        Load adjacency matrix. Can be any type of graph.
        :param path_to_matrix: Adjacency matrix in csv format.
        """
        with open(path_to_matrix, "rb") as file:
            graph = file.readlines()

        matrix = []
        for line in graph:
            matrix.append(list(map(int, line.decode("utf-8")
                                   .replace('\t', ' ')
                                   .replace('\r', '')
                                   .replace('\n', '')
                                   .split(' '))))
        return matrix

    @staticmethod
    def inverse_matrix(matrix):
        """
        Inverse given matrix. Throws an error if matrix is singular or not quadratic
        :param matrix: Matrix (list of lists) to inverse.
        :return inv_matrix: Inversed matrix.
        """
        np_array = numpy.array(matrix)
        inv = numpy.linalg.inv(np_array).tolist()
        return inv

    @staticmethod
    def degree_matrix(matrix):
        """
        Calculates degree matrix for given adjacency matrix.
        :param matrix: Matrix (list of lists) to inverse.
        :return degree_matrix: Degree matrix.
        """
        for row in matrix:
            if len(row) != len(matrix):
                raise Exception("Given table is not a quadratic matrix.")
        degree_m = []
        for i in range(0, len(matrix)):
            row_sum = 0
            for j in range(0, len(matrix)):
                row_sum += matrix[i][j]
            current = [0] * len(matrix)
            current[i] = row_sum
            degree_m.append(current)
        return degree_m

    @staticmethod
    def matrix_multiply(matrix_a, matrix_b, p=-1):
        result = []
        for row in matrix_a:
            current = [0] * len(matrix_b[0])
            for i in range(0, len(matrix_b[0])):
                for j in range(0, len(matrix_b)):
                    current[i] += row[j] * matrix_b[j][i]
            if p >= 1:
                for i in range(0, len(current)):
                    current[i] = current[i] % p
            result.append(current)
        return result

    @staticmethod
    def matrix_subtraction(matrix_a, matrix_b):
        if (len(matrix_a) != len(matrix_b)) or (len(matrix_a[0]) != len(matrix_b[0])):
            raise Exception("Given matrices have different dimensions")
        result = []
        for i in range(len(matrix_a)):
            current = [0] * len(matrix_a[0])
            for j in range(len(matrix_a[0])):
                    current[j] = matrix_a[i][j] - matrix_b[i][j]
            result.append(current)
        return result
