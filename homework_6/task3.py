import cmath

def solve_quadratic_equation(a, b, c):
    # розрахунок дискримінанту
    d = b**2 - 4*a*c
    
    # розрахунок коренів рівняння
    x1 = (-b + cmath.sqrt(d)) / (2*a)
    x2 = (-b - cmath.sqrt(d)) / (2*a)
    
    return x1, x2


a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

x1, x2 = solve_quadratic_equation(a, b, c)

if isinstance(x1, complex):
    print("x1 =", x1)
    print("x2 =", x2)
else:
    if x1 == x2:
        print("x =", x1)
    else:
        print("x1 =", x1)
        print("x2 =", x2)
