def save_matrix(matrix, path):
    """
    Saves matrix to file.
    :param matrix: Matrix to be saved.
    :param path: Output path.
    """
    for row in matrix:
        f = open(path, "a")
        f.write(" ".join(map(str, row)) + "\n")
        f.close()


def save_matrix_numpy(matrix, path):
    """
    Saves numpy array to file.
    :param matrix: Numpy array to be saved.
    :param path: Output path.
    """
    for row in matrix:
        f = open(path, "a")
        f.write(" ".join(map(str, row.tolist())) + "\n")
        f.close()
