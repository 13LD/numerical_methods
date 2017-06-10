from util.matrix_tool import *


def qr(B):
    m, n = size(B)
    U = eye(m)
    V = eye(n)
    k = min([m, n])

    for i in range(k-1):
        c, s = get_givens_coeff(B[i][i], B[i][i + 1])
        Q = generate_Q(c, s, n, i)
        B = multiply_m(B, transpose(Q))
        V = multiply_m(V, transpose(Q))
        replace_small_elements(B)

        c, s = get_givens_coeff(B[i][i], B[i + 1][i])
        Q = generate_Q(c, s, m, i)
        B = multiply_m(Q, B)
        U = multiply_m(U, transpose(Q))
        replace_small_elements(B)

    return U, B, V


def get_givens_coeff(f, g):

    if f == 0:
        c = 0
        s = 1
    elif math.fabs(f) > math.fabs(g):
        t = g / f
        t1 = math.sqrt(1 + t**2)
        c = 1. / t1
        s = t * c
    else:
        t = f / g
        t1 = math.sqrt(1 + t**2)
        s = 1. / t1
        c = t * s

    return c, s


def generate_Q(c, s, n, index):
    Q = eye(n)

    Q[index][index] = Q[index + 1][index + 1] = c
    Q[index + 1][index] = -s
    Q[index][index + 1] = s

    return Q


def replace_small_elements(B):
    m, n = size(B)

    for i in range(m):
        for j in range(n):
            if math.fabs(B[i][j]) < 10**(-7):
                B[i][j] = 0.
