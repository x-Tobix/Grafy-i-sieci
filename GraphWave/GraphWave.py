
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
                    #final_sig[::2, i] = zeros_vec[i] + 1.0 / n_nodes*np.cos(np.einsum("i,j-> ij", t, np.array(d[i]))).sum(1)
                    




        #temp2 = temp.T
        #d = temp2.data
        #n_nodes = temp.shape[1]
        #final_sig = np.zeros((2 * len(t), n_nodes))
        #zeros_vec = np.array([1.0 / n_nodes*(n_nodes - len(d[i])) for i in range(n_nodes)])
        #for i in range(n_nodes):
        #    final_sig[::2, i] = zeros_vec[i] + 1.0 / n_nodes *\
        #        np.cos(np.einsum("i,j-> ij", t, np.array(d[i]))).sum(1)
        #for it_t, t in enumerate(t):
        #    final_sig[it_t * 2 + 1, :] = 1.0 / n_nodes * ((t*temp).sin().sum(0))

        return final_sig

    def create_embedding(self, s, d):
        """
        Creates embedding from a graph based on GraphWave algorithm
        """
        t= np.linspace(0,100,d)
        heat_print = self.spectral_graph_wavelet(self.A, s)
        chi = self.characteristic_function(t, heat_print,d)
        
        return chi



        
