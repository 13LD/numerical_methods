import numpy as np
import math

# import matplotlib.pyplot as plt


def get_finite_diff(y):
    diff = []
    for i in range(1, len(y)):
        diff.append(y[i] - y[i - 1])
    return diff


def get_finite_diff_matrix(y):
    diffs = [y]
    next_diff = y

    for i in range(len(y) - 1):
        next_diff = get_finite_diff(next_diff)
        diffs.append(next_diff)
    return diffs


def get_nearest(x, x_array, h):
    n = len(x_array)

    for i in range(n - 1):
        if x < x_array[i + 1]:
            return i, (x - x_array[i]) / h

    return -1, (x - x_array[-1]) / h


def get_newton_first(x_arr, y_arr):
    n = len(x_arr)

    h = x_arr[1] - x_arr[0]
    finite_diffs = get_finite_diff_matrix(y_arr)

    def f(x):
        pos, q = get_nearest(x, x_arr, h)
        res = y_arr[pos]

        for i in range(1, n):
            if len(finite_diffs[i]) == pos:
                break

            prod = q / math.factorial(i) * finite_diffs[i][pos]
            for j in range(2, i + 1):
                prod *= (q - j + 1)
            res += prod

        return res

    return f


if __name__ == '__main__':
    from fn_approx.constants import f_32 as f_init, xval_32 as xvals
    start = 4.5
    end = 25
    step = 0.5

    x = np.arange(start, end, step)
    y = f_init(x)

    f = get_newton_first(x, y)

    # plt.plot(x, y, 'ro')
    # ls = np.linspace(np.min(x) - step, np.max(x), 1000)
    # res = []
    # for i in ls:
    #     res.append(f(i))

    # plt.plot(ls, res, 'b')
    # plt.title("Newton first formula")
    # plt.show()

    print("#32")
    np_ys = np.interp(xvals, x, y)
    for xval, yval in zip(xvals, np_ys):
        print("x: {:10.3f}\t y: {:15.6f}\t y: {:15.6f}".format(xval, f(xval),
                                                               yval))
