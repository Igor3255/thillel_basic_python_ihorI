def solve_quadratic_equation(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        return x1, x2
    elif d == 0:
        x = -b / (2*a)
        return x, None
    else:
        return None, None

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

x1, x2 = solve_quadratic_equation(a, b, c)

if x1 is not None and x2 is not None:
    print("x1 =", x1)
    print("x2 =", x2)
elif x1 is not None:
    print("x =", x1)
else:
    print("No solutions")
