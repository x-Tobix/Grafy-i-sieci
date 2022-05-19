
from tkinter import N
import numpy as np
from scipy.sparse import csgraph
from BaseAlgorithm import BaseAlgorithm



class GraphWave(BaseAlgorithm):
    """
    Main class for GraphWave algorithm model.
    """

    def __init__(self, adjacency_matrix, s, d ):
        """
        GraphWave constructor
        @param adjacency_matrix: Adjacency matrix representing graph.
        @param s: scale parametr
        @param d: dimension
        """

        self.s = s
        self.A = self.load_adjacency_matrix(adjacency_matrix)
        self.N = len(self.A)
        self.d = d 
        super().__init__()


    def heat_kernel(self, s, lamb, U):
        lamb = lamb.tolist()
        temp = np.matrix(np.zeros((len(lamb),len(lamb))))
        for i in range(len(lamb)):
            temp[i,i] = s*lamb[i]

        heat = U.dot(temp).dot(U.T)
        return heat
        

    def spectral_graph_wavelet(self, adjacency_matrix, s):
        """
        This method computes the heat diffusion waves for each of the nodes
        """
        D = self.degree_matrix(adjacency_matrix)
        L = self.matrix_subtraction(D, adjacency_matrix)
        lap = csgraph.laplacian(np.array(L))
        lamb, U = np.linalg.eigh(lap)
        lamb = lamb.round(5)
        heat = self.heat_kernel(s, lamb, U)
        
        return heat

    def characteristic_function(self, t, temp, d):
        """
        This method computes the characteristic function
        """

        for a in range(self.N):
            final_sig = np.zeros((2 * d, self.N))
            zeros_vec = np.array([0 for i in range(d)])
            for i in range(d):
                countRe = 0
                countIm = 0
                for m in range(self.N):
                    countRe += np.cos(t[i]*temp[m,a])
                    countIm += np.sin(t[i]*temp[m,a])
                final_sig[::2, i] = zeros_vec[i] + 1.0 / self.N * countRe
                final_sig[1::2, i] = zeros_vec[i] + 1.0 / self.N * countIm

        return final_sig

    def create_embedding(self, s, d):
        """
        Creates embedding from a graph based on GraphWave algorithm
        """
        t= np.linspace(0,100,d)
        heat_print = self.spectral_graph_wavelet(self.A, s)
        chi = self.characteristic_function(t, heat_print,d)
        
        return chi



        
