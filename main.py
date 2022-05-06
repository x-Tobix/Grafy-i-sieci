from GraRep.GraRep import GraRep

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
            print("Not implemented yet")
        elif action == "C":
            chosen = True
            print("Not implemented yet")
        else:
            print("Option is not available. Please try again.")
    input("Press enter to exit")
