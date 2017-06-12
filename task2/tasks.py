from singular_decomposition.svd import svd
from util.matrix_tool import *
import numpy as np


def p_inv(A):
    U, S, V = svd(A)
    k = min(size(S))

    for i in range(k):
        S[i][i] = 1. / S[i][i]

    return multiply_m(multiply_m(V, transpose(S)), transpose(U)) # V * S' * U'


def rang(A):
    s = get_singular_values(A)

    rang = 0

    for i in range(len(s)):
        if s[i] != 0:
            rang += 1

    return rang


def condition(A, invA=None):
    if invA is None:
        s = get_singular_values(A)
        return math.fabs(s[0] / s[-1])

    return euclid_norm(A) * euclid_norm(invA)


def slar_norm(A, b):
    return flatten_v(multiply_m(p_inv(A), b))


def solve_slar(A, b):
    U, S, V = svd(A)
    z = flatten_v(multiply_m(transpose(U), b))
    s = get_diagonal(S)
    rang_A = rang(A)

    if len(U) > len(V):
        for i in range(rang_A, len(U)):
            if z[i] > 10**(-7):
                return None

    return [z[i] / s[i] for i in range(rang_A)]


def get_singular_values(A):
    U, S, V = svd(A)
    return get_diagonal(S)

if __name__ == '__main__':
    from util.contants import A2_5 as A, b2_5 as b
    U, S, V = svd(A)
    print_matrix(S, precision=4)
    print("Pseudo Inv:")
    print_matrix(p_inv(A), precision=4)
    print(rang(A))
    print(condition(A))
    print(condition(A, p_inv(A)))
    print(slar_norm(A, transpose(b)))
    print(solve_slar(A, transpose(b)))

    print_matrix(np.linalg.pinv(A), precision=4)
    print(np.linalg.cond(A))
    print(np.linalg.matrix_rank(A))
