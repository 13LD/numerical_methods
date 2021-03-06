from math import log, cos, sin, tan, sqrt, fabs

def frange(start, stop, step=1.0):
    while start < stop:
        yield start
        start += step


def expression_1(x):
    return x * cos(x * x)+log(x * x * x)

def expression_16(x):
    return (1+ sqrt(1/tan(x)))/(sin(x)*sin(x))

def trapec(a, b, epsilon):
    H = b - a
    n = 1
    I_tH = (H/2.0) * (expression_1(a) + expression_1(b))
    while True:
        h = H / 2.0
        x_list = [a + h]
        for i in range(1, n):
            x_list.append(x_list[i - 1] + H)
        sum_y = 0
        for x in x_list:
            sum_y += expression_1(x)

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


## 10.3118439923192 Wolfram VAR - 1
## integrate x * cos(x * x)+log(x * x * x) dx, x=5..7
trapec(5, 7, 0.000000001)


## 2.49643 Wolfram VAR - 16
## integrate (1+ sqrt(1/tan(x)))/(sin(x)*sin(x)) dx, x=0.5..1
# trapec(0.5, 1, 0.000000001)
