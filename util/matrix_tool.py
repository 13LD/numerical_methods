import math
from itertools import product


def eye(n):
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        a[i][i] = 1
    return a


def ones(n, m):
    return [[1] * m for _ in range(n)]


def zeros(n, m=None):
    m = n if not m else m
    return [[0] * m for _ in range(n)]


def zeros_v(n):
    return [0] * n


def norm(vector):
    return math.sqrt(sum(map(lambda x: x * x, vector)))


def size(matrix):
    return len(matrix), len(matrix[0])


def flatten_v(vertical_v):
    return [e[0] for e in vertical_v]


def max_norm_m(matrix):
    res = float("-inf")
    for row in matrix:
        for elem in row:
            res = max(res, elem)
    return res


def max_col_norm_m(matrix):
    m = len(matrix[0])
    res = float("-inf")
    for j in range(m):
        res = max(res, sum(row[j] for row in matrix))
    return res


def scalar_prod(matrix, scalar):
    if isinstance(matrix[0], (list, tuple)):
        return [[item * scalar for item in row] for row in matrix]
    else:
        return [item * scalar for item in matrix]


def scalar_div(matrix, scalar):
    if isinstance(matrix[0], (list, tuple)):
        return [[item * 1. / scalar for item in row] for row in matrix]
    else:
        return [item * 1. / scalar for item in matrix]


def scalar_sum(matrix, scalar):
    if isinstance(matrix[0], (list, tuple)):
        return [[item + scalar for item in row] for row in matrix]
    else:
        return [item + scalar for item in matrix]


def get_row(matrix, index):
    return matrix[index]


def get_column(matrix, index):
    return [row[index] for row in matrix]


def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))


def transpose(matrix):
    if isinstance(matrix[0], (list, tuple)):
        return [get_column(matrix, i) for i in range(len(matrix[0]))]
    else:
        return [[i] for i in matrix]


def append_column(A, x):
    S = []
    for i in range(len(A)):
        S.append(A[i][:])
        [S[i].append(xj) for xj in x[i]]
    return S


def sum_m(A, B):
    C = zeros(len(A), len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C


def sum_v(v, u):
    return [x + y for x, y in zip(v, u)]


def subtract_v(v, u):
    return [x - y for x, y in zip(v, u)]


def subtract_m(A, B):
    C = zeros(len(A), len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] - B[i][j]
    return C


def multiply_m(A, B):
    if len(A[0]) != len(B):
        raise ValueError("The number of A columns does not equal the number of B rows")
    rows, cols = len(B), len(B[0])
    res_rows = range(len(A))
    res_matrix = [[0] * cols for _ in res_rows]
    for idx in res_rows:
        for j, k in product(range(cols), range(rows)):
            res_matrix[idx][j] += A[idx][k] * B[k][j]

    if len(res_matrix) == 1 and len(res_matrix[0]) == 1:
        return res_matrix[0][0]

    return res_matrix


def power_m(A, p):
    B = []
    for i in range(len(A)):
        B.append(A[i][:])
    for i in range(1, p):
        B = multiply_m(B, A)
    return B


def multiply_m_v(m, v):
    _size = len(v)
    return [
        sum(m[i][j] * v[j] for j in range(_size)) for i in range(_size)
    ]


def multiply_v(lhs, rhs):
    res = 0
    for l, r in zip(lhs, rhs):
        res += l * r
    return res


def print_matrix(A, precision=2, plain=False, round_elem=False):
    for row in A:
        for elem in row:
            if plain:
                print("{: }\t".format(elem), end="")
            elif round_elem:
                print("{: 7.0f} ".format(round(elem)), end="")
            else:
                print("{2: {1}.{0}f} ".format(precision, precision + 5, elem), end="")
        print()


def print_vector(x, **kwargs):
    print_matrix([[xi] for xi in x], **kwargs)


def signum(x):
    return (x > 0) - (x < 0)


def get_diagonal(m):
    k = min(size(m))
    diagonal = []

    for i in range(k):
        diagonal.append(m[i][i])

    return diagonal
