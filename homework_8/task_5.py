def get_max_digit(number):
    # перетворюємо число у рядок
    num_str = str(number)
    # знаходимо максимальну цифру у рядку
    max_digit = max(num_str)
    # перетворюємо максимальну цифру знову у число
    return int(max_digit)


import random

def get_max_digit(number):
    # ініціалізуємо максимальну цифру як 0
    max_digit = 0
    # проходимо по кожній цифрі числа
    while number > 0:
        digit = number % 10
        # якщо цифра більша за максимальну, замінюємо її
        if digit > max_digit:
            max_digit = digit
        # ділимо число на 10, щоб перейти до наступної цифри
        number //= 10
    return max_digit

# згенеруємо випадкове 12-ти-значне число для тестування
number = random.randint(10**11, 10**12-1)
print(number)
print(get_max_digit(number))
