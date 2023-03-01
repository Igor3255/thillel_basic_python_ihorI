import random

def get_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Будь ласка, введіть ціле число")

def get_str(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text

def guess_number_game():
    secret_number = random.randint(1, 100)
    print("Загадано число від 1 до 100. Спробуйте відгадати!")
    while True:
        guess = get_integer("Введіть число: ")
        if guess == secret_number:
            print("Ви виграли!")
            break
        elif guess < secret_number:
            print("Загадане число більше.")
        else:
            print("Загадане число менше.")

def guess_my_number_game():
    print("Загадайте число від 1 до 100, а я спробую відгадати!")
    min_number = 1
    max_number = 100
    while True:
        guess = random.randint(min_number, max_number)
        print("Чи загадане число: ", guess)
        user_feedback = get_str("Чи відгадав я правильно? Введіть 'більше', 'менше', або 'вірно': ")
        if user_feedback == 'вірно':
            print("Я виграв!")
            break
        elif user_feedback == 'більше':
            min_number = guess + 1
        elif user_feedback == 'менше':
            max_number = guess - 1

def main():
    while True:
        print("Виберіть гру:")
        print("1. Вгадайте число.")
        print("2. Я відгадаю ваше число.")
        game_choice = get_integer("Ваш вибір: ")
        if game_choice == 1:
            guess_number_game()
        elif game_choice == 2:
            guess_my_number_game()
        else:
            print("Невірний вибір. Спробуйте ще раз.")
        play_again = get_str("Хочете зіграти ще раз? (Так/Ні) ").lower()
        if play_again != 'так':
            break

if __name__ == '__main__':
    main()
