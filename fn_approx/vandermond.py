import numpy as np
import matplotlib.pyplot as plt
from fn_approx.constants import f_32 as f_init, xval_32 as xvals

start = 4.5
end = 25
step = 0.5

x = np.arange(start, end, step)
y = f_init(x)

order = 11 # order of polynom

A = np.fliplr(np.vander(x, order))
coefs, _, _, _ = np.linalg.lstsq(A, y)

cnt = 1000 # number of points to plot
interp_x = np.linspace(start, end, cnt)
interp_y = np.zeros(cnt)

for ind, ix in enumerate(interp_x):
    interp_y[ind] = np.sum(coefs * ix ** np.arange(0, order))

plt.figure()
plt.plot(interp_x, interp_y, '-b', label='interp line')
plt.plot(x, y, '*r', label='data points')
plt.xlabel('x value')
plt.ylabel('y value')
plt.title('Vandermond Interpolation')
plt.show()