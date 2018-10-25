import math


def read_from_console():
    a = int(input("Enter upper bound(a):"))
    b = int(input("Enter lower bound(b):"))
    n = int(input("Enter number of divisions(n):"))
    return a, b, n


def f(x):
    return x * pow(x ** 2 - 4, 3 / 2)


def method_of_trapezium(a, b, n):
    integral = 0
    h = (b - a) / n
    x = a + h
    fa = f(a)
    fb = f(b)
    for i in range(1, n - 1):
        integral += f(x)
        x += h
    integral = h * ((fa + fb)/2 + integral)
    return integral


if __name__ == '__main__':
    a, b, n = read_from_console()
    integral = method_of_trapezium(a, b, n)
    print(integral)