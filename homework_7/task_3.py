import math

def calculate_wheat_chess_position(kilograms):
    weight_summ = 0.000035
    cell = int(math.log2(kilograms/weight_summ)) + 1
    chessboard_letters = 'abcdefgh'
    return chessboard_letters[cell//8], cell % 8


def main():
    n = float(input('Введіть: '))
    print(calculate_wheat_chess_position(n))


if __name__ == '__main__':
    main()
