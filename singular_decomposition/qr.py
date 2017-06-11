from util.matrix_tool import *


def qr(B):
    m, n = size(B)
    U = eye(m)
    V = eye(n)
    k = min([m, n])

    for i in range(k-1):
        c, s = get_givens_coeff(B[i][i], B[i][i + 1])
        G = generate_G(c, s, n, i, i + 1)
        B = multiply_m(B, transpose(G))
        V = multiply_m(V, transpose(G))
        replace_small_elements(B)

        c, s = get_givens_coeff(B[i][i], B[i + 1][i])
        G = generate_G(c, s, m, i, i + 1)
        B = multiply_m(G, B)
        U = multiply_m(U, transpose(G))
        replace_small_elements(B)

    return U, B, V


def replace_small_elements(B):
    m, n = size(B)

    for i in range(m):
        for j in range(n):
            if math.fabs(B[i][j]) < 10**(-7):
                B[i][j] = 0.
