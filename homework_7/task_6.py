def fibonacci_numbers(idx_fib):
    first_digit, second_digit = 1, 0
    for i in range(idx_fib):
        first_digit, second_digit = second_digit, first_digit + second_digit
    return second_digit


def main():
    idx_fib = int(input('Введіть індекс '))
    print(fibonacci_numbers(idx_fib))


if __name__ == '__main__':
    main()
