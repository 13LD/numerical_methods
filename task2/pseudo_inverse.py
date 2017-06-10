from singular_decomposition.svd import svd
from util.matrix_tool import *


def p_inv(A):
    U, S, V = svd(A)
    k = min(size(S))

    for i in range(k):
        S[i][i] = 1. / S[i][i]

    return multiply_m(multiply_m(V, transpose(S)), transpose(U)) # V * S' * U'


if __name__ == '__main__':
    from util.contants import A1_15
    print_matrix(p_inv(A1_15), precision=4)
