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
        self.edges = []

    # TODO: Decide how files should look like
    def load_nodes(self, path_to_nodes):
        with open(path_to_nodes, "rb") as file:
            graph = file.readlines()

        self.nodes = []
        for node in graph:
            self.nodes.append(node.split(' ', 1)[0])

    # TODO: Decide how files should look like
    def load_edges(self):
        raise Exception("Not implemented yet")

    @staticmethod
    def inverse_matrix(matrix):
        """
        Inverse given matrix. Throws an error if matrix is singular or not quadratic
        :param matrix: Matrix (list of lists) to inverse.
        :return inv_matrix: Inversed matrix.
        """
        return numpy.linalg.inv(matrix)
