from sympy import Symbol, solve, pprint
x = Symbol('x')
y = Symbol('y')
expr1 = 2*x + 3*y -6
expr2 = 3*x + 2*y -12
solution = solve((expr1,expr2))
pprint(solution)