from math import sqrt, sin, cos, exp

def f1(x, z):
    return sin(x) * sin(x) + cos(z) * cos(z)

def f2(x, z):
    return x**2 / 20 - z**2 / 20

def f3(x, z):
    return exp(sin(sqrt(x**2 + z**2)))

# эллиптический параболоид
def f4(x, z):
    return x**2 / 20 + z**2 / 20

def f5(x, z):
    return x*z/25

def f6(x, z):
    return sqrt(x**2 + z**2 + 25)