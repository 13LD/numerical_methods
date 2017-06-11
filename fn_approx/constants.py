import math
import numpy as np

x_6 = [
    -13.648,
    -13.009,
    -12.595,
    -12.292,
    -12.101,
    -11.504,
    -10.837,
    -9.512,
    -9.395,
    -8.964,
    -7.840,
    -7.454,
    -5.591,
    -5.550,
    -5.298,
    -4.840,
    -3.680,
    -2.657,
    -2.297,
    -2.058,
    0.957,
    1.220,
    1.433,
    2.633,
    2.934,
    3.025,
    3.200,
    4.691,
    4.898,
    5.180,
    7.920,
]

y_6 = [
    -853.845,
    -745.547,
    -678.540,
    -630.918,
    -601.405,
    -513.132,
    -422.536,
    -277.368,
    -267.042,
    -232.072,
    -160.742,
    -140.959,
    -62.544,
    -61.094,
    -52.514,
    -38.421,
    -13.453,
    -3.901,
    -2.515,
    -1.943,
    0.843,
    1.024,
    1.178,
    3.783,
    5.549,
    6.226,
    7.726,
    34.297,
    40.064,
    48.661,
    165.059,
]

xval_6 = [
    -11.454,
    -10.239,
    -9.529,
    -8.832,
    -7.970,
    -5.455,
    -0.990,
    0.153,
    0.825,
    1.060,
    3.396,
    6.310,
    7.239,
]

xval_32 = [
    4.977,
    4.979,
    5.869,
    6.306,
    8.452,
    8.821,
    9.257,
    9.832,
    10.082,
    10.240,
    11.620,
    11.635,
    11.778,
    11.808,
    12.495,
    13.904,
    14.234,
]


def f_32(x):
    return np.exp(x) + x**2 * np.log(x) + x


def f_48(x):
    return math.sqrt(abs(x)) + math.log10(x * .2) + math.exp(x) + math.sin(
        x * .5) + x