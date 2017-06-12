import math


def trapezoidal(f, a, b, n):
	"""
	Вычисляет приближенное значение интеграла с помощью формулы трапеций
	f - подынтегральная функция
	a, b - пределы интегрирования
	n - количество частичных отрезков
	"""
	h = float(b - a)/int(n)
	result = 0.5*(f(a) + f(b))
	for i in range(1, int(n)):
		result += f(a + i*h)
	result *= h
	return result

a = 5
b = 7
v = lambda x: x*math.cos(x*x)+math.log(x*x*x)
# a = 0.5
# b = 1
# v = lambda x: (1+ math.sqrt(1/math.tan(x)))/(math.sin(x)*math.sin(x))
n = 498260
while  1:

	numerical = trapezoidal(v, a, b, n)
	h1 = float(b - a)/int(n)

# Сравнение с точным решением
# f'(x) = cos(x2)−2⋅x2⋅sin(x2)+3⋅x−1
# f''(x) = −6⋅x⋅sin(x2)−4⋅x⋅x2⋅cos(x2)−3⋅x−2
# x выбираем такой, чтобы значение функции было максимальным на промежутке

	x = 7
	rT = -(b - a)/12 * h1 * h1 *((-6) * x * math.sin(x*x) - 4*x*x*x*math.cos(x*x) - 3*x**(-2))
# 	x = 1
# 	rT = -(b - a)/12 * h1 * h1 *(math.sqrt(math.sin(2 * x)) * (-(math.cos(2*x) * (math.cos(2*x))) * math.sin(2*x)**(-2) - 2))
	V = lambda x: x*math.cos(x*x)+math.log(x*x*x)

	# V = lambda x: (1+ math.sqrt(1/math.tan(x)))/(math.sin(x)*math.sin(x))
	exact = V(7) - V(5)
# 	exact = V(1) - V(0.5)

	error = (exact - numerical) / exact * 100
	n += 1
	epsl = 1.e-9
	if rT < epsl:
		break



print ('n = %s: %.15f, погрешность: %g ' % (n, numerical, rT))



