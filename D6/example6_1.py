from sympy import Symbol, solve, pprint
x = Symbol('x')
expr = x**2 -3*x -5
solution = solve(expr,x)
pprint(solution)
