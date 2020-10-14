from sympy import Symbol,Integral,pprint
x = Symbol('x')
k = Symbol('k')
f = k*x
solution = Integral(f,x).doit()
pprint(solution)
result = Integral(f,x,(x,0,2)).doit()
pprint(result)