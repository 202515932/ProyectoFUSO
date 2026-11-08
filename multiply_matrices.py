import numpy as np

class Error_Matrices_Incompatibles(Exception):
    """Error raised when two matrices are impossible to multiply"""
    pass

SEED = 32

def multiply_matrices(matrix_a: np.ndarray, matrix_b: np.ndarray) -> np.ndarray:
    """
    Two matrices are multiplied using loops of order i-j-k

    Args:
        matrix_a (np.ndarray): First matrix
        matrix_b (np.ndarray): Second matrix

    Return:
        matrix_c (np.ndarray): Result matrix 

    Raise Error_Matrices_Incompatibles
    """
    m = matrix_a.shape[0]
    n = matrix_a.shape[1]
    o = matrix_b.shape[0]
    p = matrix_b.shape[1]

    # we dont have to check if the matrices are compatible as the are created with the same dimensions
    if n != o:
        raise Error_Matrices_Incompatibles(f"Incompatible matrices")
    
    matrix_c = np.zeros((m, p))

    for i in range(m):
        for j in range(p):
            for k in range(n):
                matrix_c[i, j] = matrix_c[i, j] + matrix_a[i, k] * matrix_b[k, j]
    return matrix_c

def generate_random_matrix(rows: int, columns: int, seed: int) -> np.ndarray:
    """
    Generation of a matrix with parameters between 0 and 100

    Args:
        rows (int): Number of rows of the matrix
        columns (int): Number of columns of the matrix
        seed (int): Seed used to generate random numbers
    
    Return:
        matrix (np.ndarray): Random generated matrix
    """
    np.random.seed(seed)
    matrix = np.random.randint(0, 101, size=(rows, columns))
    return matrix

def execute_multiply_matrices(sizes: list[int]):
    """
    Generation of two matrix of the same order and multiply them for each int of the list "sizes"

    Args:
        sizes (list[tuple]): List that contians a int that represent the dimensions of our square matrix
    """
    for i in range(len(sizes)):
        # en nuestro caso como el enunciado nos dice que crear dos matrices cuadradas para cada tamaño especificado
        matrix_a = generate_random_matrix(sizes[i], sizes[i], SEED)
        # sumo uno al seed ya que sino ambas matrices van a tener los mismos números para un mismo tamaño
        matrix_b = generate_random_matrix(sizes[i], sizes[i], SEED + 1)
        try:
            matrix_c = multiply_matrices(matrix_a, matrix_b)
        except Error_Matrices_Incompatibles as error:
            print(error)