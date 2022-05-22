from GraRep.GraRep import GraRep
from Node2Vec.Node2Vec import Node2Vec
from GraphWave.GraphWave import GraphWave

if __name__ == '__main__':
    print("----- GraRep+++Node2Vec+++GraphWave -----")
    chosen = False
    while not chosen:
        print("A. Use GraRep \nB. Use Node2Vec \nC. Use GraphWave")
        action = input("Choose option: ")
        if action == "A":
            chosen = True
            matrix = input("Give path to adjacency matrix: ")
            k = input("Give maximum transition step: ")
            d = input("Give embedding dimension: ")
            GR = GraRep(matrix, int(k), int(d))
            print(GR.create_embedding())
        elif action == "B":
            chosen = True
            matrix = input("Give path to adjacency matrix: ")
            le = input("Give length of a single random walk: ")
            r = input("Give number of random walks starting at a single vertex: ")
            p = input("Give bias Return parameter: ")
            q = input("Give bias In-Out parameter: ")
            d = input("Give embedding dimension: ")
            NV = Node2Vec(matrix, int(le), int(r), int(p), int(q), int(d))
            print("Provide crucial Word2Vec parameters.")
            negative = input("Give number of negative samples: ")
            alpha = input("Give starting learning rate: ")
            min_alpha = input("Give minimal learning rate: ")
            hs = input("Decide on Hierarchical Softmax: ")
            window = input("Give window size of a network: ")
            num_iter = input("Give number of iterations: ")
            print(NV.create_embedding(negative, alpha, min_alpha, hs, window, num_iter))
        elif action == "C":
            chosen = True
            matrix = input("Give path to adjacency matrix: ")
            s = int(input("Give scale parametr s: "))
            d = int(input("Give parametr d: "))

            GW = GraphWave(matrix, s, d)
            print(GW.create_embedding(s,d))
        else:
            print("Option is not available. Please try again.")
    input("Press enter to exit")
