def triangle_square_and_perimeter(a, b):
    c = (a ** 2 + b ** 2) ** 0.5 # знаходимо гіпотенузу
    perimeter = a + b + c # знаходимо периметр
    square = (a * b) / 2 # знаходимо площу
    return square, perimeter


a = float(input("Введіть довжину першого катета: "))
b = float(input("Введіть довжину другого катета: "))

square, perimeter = triangle_square_and_perimeter(a, b)

print("Площа трикутника:", square)
print("Периметр трикутника:", perimeter)
