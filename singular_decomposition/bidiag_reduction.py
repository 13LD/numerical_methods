from util.matrix_tool import *
from copy import deepcopy


def bidiag_reduction(matrix):
    m, n = size(matrix)
    k = min([m, n])
    B = deepcopy(matrix)
    U = eye(m)
    V = eye(n)

    for i in range(k):
        B, U = update_column(B, U, i)

        if i < k - 2:
            B, V = update_row(B, V, i, i + 1)

    if m < n:
        B, V = update_row(B, V, m - 2, m - 1)
        B, V = update_row(B, V, m - 1, m)
        for i in range(k - 1, -1, -1):
            G = get_Gij(B, i, k, n)
            B = multiply_m(B, G)
            V = multiply_m(V, G)

    return U, B, V


def householder(x, k):
    n = len(x)
    u = zeros_v(n)
    u[k] = x[k] + signum(x[k]) * norm(x[k:n])
    u[(k + 1):n] = x[(k + 1):n]
    param = 2. / dot_product(u, u)
    w = scalar_prod(multiply_m(transpose(u), [u]), param)
    return subtract_m(eye(n), w)


def update_column(B, U, index):
    H1 = householder(get_column(B, index), index)
    return multiply_m(H1, B), multiply_m(U, transpose(H1))


def update_row(B, V, i, k):
    H2 = householder(B[i], k)
    return multiply_m(B, transpose(H2)), \
           multiply_m(V, transpose(H2))


if __name__ == '__main__':

    A = [
        [23, -51, 118, -80, -119],
        [120, -21, 46, -90, 69],
        [-85, 66, -138, -36, 45],
        [141, 125, 1, 29, -8],
        [-20, 117, 119, -70, 130],
        [86, -110, -34, 37, -121],
        [8, -114, -63, 92, 30]
    ]

    K = [
        [36, 136, -77, -89, 94, -137, -80],
        [-98, 75, -64, -20, 122, -107, -68],
        [-63, 77, 139, -108, 12, -80, 136],
        [-145, 13, -81, -37, 96, -76, -46],
        [61, -66, 11, 88, 63, -99, -61]
    ]

    C = [[5, 4, 3, 2], [1, 2, 4, 7], [13, 21, 7, 9], [5, 27, 12, 11]]

    U, B, V = bidiag_reduction(K)
    print_matrix(B)
