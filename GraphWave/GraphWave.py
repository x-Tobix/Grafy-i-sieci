
from tkinter import N
import numpy as np
from scipy.sparse import csgraph
from BaseAlgorithm import BaseAlgorithm



class GraphWave(BaseAlgorithm):
    """
    Main class for GraphWave algorithm model.
    """

    def __init__(self, adjacency_matrix, d, J = 1, eta = 0.85, gamma = 0.95):
        """
        GraphWave constructor
        @param adjacency_matrix: Adjacency matrix representing graph.
        @param d: dimension
        @param J: parametr J
        """

        self.A = self.load_adjacency_matrix(adjacency_matrix)
        self.N = len(self.A)
        self.d = d 
        self.J = J
        self.__eta = eta
        self.__gamma = gamma
        super().__init__()

    def calculate_s(self, lamb):
        temp = np.sort(lamb)
        geom_mean = np.sqrt(temp[1] * temp[-1])
        s_max = -np.log(self.__eta) * geom_mean
        s_min = -np.log(self.__gamma) * geom_mean
        if self.J == 1:
            s = np.reshape((s_min+s_max)/2, 1)
        else:
            s = np.linspace(s_min, s_max, self.J)
        return s


    def heat_kernel(self, s, lamb, U):
        lamb = lamb.tolist()
        temp = np.matrix(np.zeros((len(lamb),len(lamb))))
        heat = []
        for j in range(self.J):
            for i in range(len(lamb)):
                temp[i,i] = np.exp(-s[j]*lamb[i])
            heat.append(U.dot(temp).dot(U.T))
        return heat
        

    def spectral_graph_wavelet(self, adjacency_matrix):
        """
        This method computes the heat diffusion waves for each of the nodes
        """
        D = self.degree_matrix(adjacency_matrix)
        L = self.matrix_subtraction(D, adjacency_matrix)
        #lap = csgraph.laplacian(np.array(L))
        lamb, U = np.linalg.eigh(L)
        lamb = lamb.round(5)
        s = self.calculate_s(lamb)
        heat = self.heat_kernel(s, lamb, U)
        
        return heat

    def characteristic_function(self, t, temp, d):
        """
        This method computes the characteristic function
        """
        final_sig = np.zeros((2 * d * self.J, self.N))
        for a in range(self.N):
            for j in range(self.J):
                for i in range(d):
                    countRe = 0
                    countIm = 0
                    for m in range(self.N):
                        countRe += np.cos(t[i]*temp[j][m,a])
                        countIm += np.sin(t[i]*temp[j][m,a])
                    final_sig[2*i+4*j, a] =  1.0 / self.N * countRe
                    final_sig[2*i+4*j + 1, a] =  1.0 / self.N * countIm

        return final_sig

    
    def create_embedding(self, d, interval_start = 0, interval_stop = 1):
        """
        Creates embedding from a graph based on GraphWave algorithm
        """
        
        t = np.linspace(interval_start,interval_stop,d)
        heat_print = self.spectral_graph_wavelet(self.A)
        chi = self.characteristic_function(t, heat_print,d)
        
        return chi



        
