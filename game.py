import random

def play_game():
    """Играет в игру "Камень-ножницы-бумага" с пользователем"""
    options = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(options)
    user_choice = input("Выберите камень, ножницы или бумагу: ").lower()

    print(f"Компьютер выбрал: {computer_choice}")
    print(f"Вы выбрали: {user_choice}")

    if computer_choice == user_choice:
        print("Ничья!")
    elif (computer_choice == "камень" and user_choice == "ножницы") or \
        (computer_choice == "ножницы" and user_choice == "бумага") or \
        (computer_choice == "бумага" and user_choice == "камень"):
        print("Вы проиграли!")
    else:
        print("Вы выиграли!")

if __name__ == '__main__':
    play_game()
