from util.matrix_tool import *
from singular_decomposition.bidiag_reduction import bidiag_reduction
from singular_decomposition.qr import qr


def svd(A):
    U, B, V = bidiag_reduction(A)

    while compute_error(B) > 10**(-7):
        U2, B, V2 = qr(B)
        U = multiply_m(U, U2)
        V = multiply_m(V, V2)

    return U, B, V


def compute_error(B):
    k = min(size(B))

    second_diagonal = []

    for i in range(k - 1):
        second_diagonal.append(B[i][i + 1])

    return norm(second_diagonal)


if __name__ == '__main__':
    from util.contants import A1_15
    U, S, V = svd(A1_15)
    print_matrix(S)