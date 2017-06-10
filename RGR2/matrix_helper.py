

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

def get_column(matrix, index):
    return [row[index] for row in matrix]

def transpose(matrix):
    if isinstance(matrix[0], (list, tuple)):
        return [get_column(matrix, i) for i in range(len(matrix[0]))]
    else:
        return [[i] for i in matrix]

def multiply_m (A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
      raise ValueError("The number of A columns does not equal the number of B rows")


    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

def identity_matrix(n):
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        a[i][i] = 1
    return a





