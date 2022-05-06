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

    def load_adjacency_matrix(self, path_to_matrix):
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
        return numpy.linalg.inv(matrix)
