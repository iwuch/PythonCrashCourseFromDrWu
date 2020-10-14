from sympy import Symbol,Derivative,pprint
t = Symbol('t')
S = 5* t**2 + 3*t + 8
der = Derivative(S,t)
expr = der.doit()
sol = expr.subs({t:3})
pprint(expr)
pprint(sol)