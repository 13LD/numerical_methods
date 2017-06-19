import numpy as np
import util.matrix_tool as mt
import math
from copy import deepcopy

def jacoby_eigen(matrix, epsilon, get_next_coords):
    THRESHOLD = 100 # use to check is one number much greater than other, a >> b
    n = len(matrix)

    B = matrix
    iter = 1
    T = mt.eye(n)

    while True:
        i, j = get_next_coords(B) # get coords for next elements based on some algorithm

        print("========================================")
        print("Iteration #{}. i = {}, j = {}".format(iter, i, j))

        if i == -1 or j == -1 or stop_criterion(B) < epsilon:
            return get_diagonal(B), mt.transpose(T), iter

        p = 2. * B[i][j]
        q = B[i][i] - B[j][j]
        d = math.sqrt(p**2 + q**2)

        print("p = {}".format(p))
        print("q = {}".format(q))
        print("d = {}".format(d))

        # Compute c and s variables
        if q != 0:
            r = math.fabs(q) / (2. * d)
            print("r = {}".format(r))
            c = math.sqrt(0.5 + r)
            s = math.sqrt(0.5 - r) if math.fabs(q / p) > THRESHOLD else math.fabs(p) / (2 * c * d)
            s *= mt.signum(p * q)
        else:
            c = s = math.sqrt(2) / 2.

        print("c = {}, s = {}".format(c, s))

        T_curr = mt.eye(n)
        T_curr[i][i] = T_curr[j][j] = c
        T_curr[i][j] = -s
        T_curr[j][i] = s

        print("T matrix:")
        mt.print_matrix(T_curr, precision=4)

        T = mt.multiply_m(T, T_curr)

        B_new = deepcopy(B)

        # Set new diagonal elements
        B_new[i][i], B_new[j][j] = c**2 * B[i][i] + s**2 * B[j][j] + 2 * c * s * B[i][j], \
                           s**2 * B[i][i] + c**2 * B[j][j] - 2 * c * s * B[i][j]

        B_new[i][j] = B_new[j][i] = 0

        # Update other elements
        for m in range(n):
            if m != i and m != j:
                B_new[m][i] = B_new[i][m] = c * B[m][i] + s * B[m][j]
                B_new[m][j] = B_new[j][m] = -s * B[m][i] + c * B[m][j]

        print("B matrix:")
        mt.print_matrix(B_new, precision=4)
        iter += 1
        B = B_new

        print("Stop criterium: {}".format(stop_criterion(B_new)))


# Frobenius norm for all non-diagonal elements
def stop_criterion(matrix):
    n = len(matrix)
    s = 0

    for i in range(n):
        for j in range(n):
            if i != j:
                s += matrix[i][j] ** 2

    return math.sqrt(s)


def get_diagonal(matrix):
    diagonal = []

    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])

    return diagonal


def jacoby_original(matrix, epsilon):
    def get_max_element_coords(m):
        max_i = max_j = -1
        max_el = -1

        for i in range(len(m)):
            for j in range(len(m)):
                if i != j and math.fabs(m[i][j]) > max_el:
                    max_el = math.fabs(m[i][j])
                    max_i = i
                    max_j = j

        #if max_el == 0:
         #   return -1, -1

        return max_i, max_j

    return jacoby_eigen(matrix, epsilon, get_max_element_coords)



print(jacoby_original([[49, -26, -22], [-26, 31, 15], [-22, 15, 39]], 10**(-2)))