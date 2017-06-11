import numpy as np
import matplotlib.pyplot as plt


def get_lagrange_polynom(x_arr, y_arr):
    def f(x):
        res = 0
        n = len(x_arr)

        for i in range(n):
            prod = y_arr[i]
            for j in range(n):
                if j != i:
                    prod *= (x - x_arr[j]) / (x_arr[i] - x_arr[j])
            res += prod
        return res
    return f


def test_func(x):
    return np.exp(x) + x ** 2 * np.log(x) + x


if __name__ == '__main__':
    start = 4.5
    end = 25
    step = 0.5

    x = np.arange(start, end, step)
    y = test_func(x)

    f = get_lagrange_polynom(x, y)

    plt.plot(x, y, 'ro')
    ls = np.linspace(np.min(x) - step, np.max(x) + step, 1000)
    plt.plot(ls, f(ls), 'b')
    plt.title("Lagrange polynom")
    plt.show()
    print(f(5))