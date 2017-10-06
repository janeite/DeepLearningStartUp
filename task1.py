from sympy import diff, Symbol, sin
x=Symbol('x')
print(diff(sin(x**2)*x,x))
