def horse_move(start, end):
    return abs(abs(ord(start[0]) - ord(end[0])) - abs(int(start[1]) - int(end[1]))) == 1


def main():
    start_step = input('Введіть початок руху ')
    end_step = input('Введіть куди рухатися ')
    print(horse_move(start_step, end_step))


if __name__ == '__main__':
    main()