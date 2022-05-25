import time

from GraRep.GraRep import GraRep
from Node2Vec.Node2Vec import Node2Vec
from GraphWave.GraphWave import GraphWave
from Utilities import save_matrix

if __name__ == '__main__':
    print("----- GraRep+++Node2Vec+++GraphWave -----")
    chosen = False
    result = None
    while not chosen:
        print("A. Use GraRep \nB. Use Node2Vec \nC. Use GraphWave")
        action = input("Choose option: ")
        if action == "A":
            chosen = True
            matrix = input("Give path to adjacency matrix: ")
            k = input("Give maximum transition step: ")
            d = input("Give embedding dimension: ")
            start = time.time()
            GR = GraRep(matrix, int(k), int(d))
            result = GR.create_embedding()
            end = time.time()
            print(result)
            print(end - start)
        elif action == "B":
            chosen = True
            matrix = input("Give path to adjacency matrix: ")
            le = int(input("Give length of a single random walk: "))
            r = int(input("Give number of random walks starting at a single vertex: "))
            p = float(input("Give bias Return parameter: "))
            q = float(input("Give bias In-Out parameter: "))
            d = int(input("Give embedding dimension: "))
            start = time.time()
            NV = Node2Vec(matrix, int(le), int(r), int(p), int(q), int(d))
            result = NV.create_embedding()
            end = time.time()
            print(result)
            print(end - start)
        elif action == "C":
            chosen = True
            matrix = input("Give path to adjacency matrix: ")
            d = int(input("Give parameter d: "))
            J = int(input("Give parameter J: "))
            interval_start = int(input("Give interval_start: "))
            interval_stop = int(input("Give interval_stop: "))
            start = time.time()
            GW = GraphWave(matrix, d, J)
            result = GW.create_embedding(d, interval_start, interval_stop)
            end = time.time()
            print(result)
            print(end - start)
        else:
            print("Option is not available. Please try again.")
    save = input("Do you want to save embedding? Type Y if yes.")
    if save == "Y":
        path = input("Give embedding path: ")
        save_matrix(result, path)
    input("Press enter to exit")
