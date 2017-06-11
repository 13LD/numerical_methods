from math import log, cos, fabs

def frange(start, stop, step=1.0):
    while start < stop:
        yield start
        start += step


def expression(x):
    return x * cos(x * x)+log(x * x * x)


def trapec(a, b, epsilon):
    H = b - a
    n = 1
    I_tH = (H/2.0) * (expression(a) + expression(b))
    while True:
        h = H / 2.0
        x_list = [a + h]
        for i in range(1, n):
            x_list.append(x_list[i - 1] + H)
        sum_y = 0
        for x in x_list:
            sum_y += expression(x)

        I_pH = H * sum_y
        I_th = (I_pH + I_tH)/2.0
        R_th = (I_th - I_tH)/3.
        print ('n =%d;  I_tH = %.15f; I_pH = %.15f; I_th = %.15f; R_th = %.15f ' % (n, I_tH, I_pH, I_th, R_th))
        if fabs(R_th) > epsilon:
            n *= 2
            H = h
            I_tH = I_th
        else:
            I_ch = I_th + R_th
            # print(I_ch)
            break

    print(n)
    print(I_ch)

trapec(5, 7, 0.000000001)