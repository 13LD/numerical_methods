from util.matrix_tool import *
from singular_decomposition.bidiag_reduction import bidiag_reduction
from singular_decomposition.twodiagonal_decomposition import twodiagonal_decomposition


def svd(A, verbose=False):
    U, B, V = bidiag_reduction(A)

    i = 0
    while compute_error(B) > 10**(-7):
        U2, B, V2 = twodiagonal_decomposition(B)
        U = multiply_m(U, U2)
        V = multiply_m(V, V2)
        i += 1

    if verbose:
        print("Iteration: {}", i)

    return U, B, V


def compute_error(B):
    k = min(size(B))

    second_diagonal = []

    for i in range(k - 1):
        second_diagonal.append(B[i][i + 1])

    return norm(second_diagonal)


if __name__ == '__main__':
    from util.contants import A2_5 as A
    import numpy as np
    U, S, V = svd(A, verbose=True)
    print_matrix(S, precision=4)
    print_matrix(U)
    print("v")
    print_matrix(V)
    U, S, V = np.linalg.svd(A, compute_uv=True)
    print("S")
    print(S)
    print_matrix(U)
    print_matrix(np.transpose(V))