
import numpy as np
from scipy.sparse import csgraph
from BaseAlgorithm import BaseAlgorithm



class GraphWave(BaseAlgorithm):
    """
    Main class for GraphWave algorithm model.
    """

    def __init__(self, adjacency_matrix, s ):
        """
        GraphWave constructor
        @param adjacency_matrix: Adjacency matrix representing graph.
        @param s: scale parametr
        """

        self.s = s
        self.N = len(self.nodes)
        self.A = self.load_adjacency_matrix(adjacency_matrix)
        super().__init__()

    def spectral_graph_wavelet(self, adjacency_matrix, s):
        """
        This method computes the heat diffusion waves for each of the nodes
        """
        D = self.degree_matrix(adjacency_matrix)
        L = self.matrix_subtraction(D - adjacency_matrix)
        lap = csgraph.laplacian(L)
        lamb, U = np.linalg.eigh(lap)
        heat = U.dot(np.diagflat(np.exp(- s * lamb).flatten())).dot(U.T)
        
        return heat

    def characteristic_function(t, temp):
        """
        This method computes the characteristic function
        """
        temp2 = temp.T.tolil()
        d = temp2.data
        n_nodes = temp.shape[1]
        final_sig = np.zeros((2 * len(t), n_nodes))
        zeros_vec = np.array([1.0 / n_nodes*(n_nodes - len(d[i])) for i in range(n_nodes)])
        for i in range(n_nodes):
            final_sig[::2, i] = zeros_vec[i] + 1.0 / n_nodes *\
                np.cos(np.einsum("i,j-> ij", t, np.array(d[i]))).sum(1)
        for it_t, t in enumerate(t):
            final_sig[it_t * 2 + 1, :] = 1.0 / n_nodes * ((t*temp).sin().sum(0))

        return final_sig

    def create_embedding(self, s, t: int = 2):
        """
        Creates embedding from a graph based on GraphWave algorithm
        """
        
        heat_print = self.spectral_graph_wavelet(self, s)
        chi = self.characteristic_function(t, heat_print)
        
        return chi



        
