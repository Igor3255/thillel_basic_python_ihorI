import random

# Створюємо список питань та відповідей
questions = [
    "Який мовний шаблон використовується в Python? (a) MVC (b) MVVM\n",
    "Яке ключове слово використовується для створення функції в Python? (a) func (b) def\n",
    "Як називається інтерпретатор Python? (a) IDLE (b) Visual Studio Code\n",
    "Які з цих типів даних є не змінюваними? (a) int, float, str (b) list, set, dict\n",
    "Яке ключове слово використовується для створення умовного оператора в Python? (a) while (b) if\n"
]

# Створюємо список відповідей
answers = [
    "b",
    "b",
    "a",
    "a",
    "b"
]

# Змінна, що зберігає кількість правильних відповідей
score = 0

# Перемішуємо список питань, щоб вони були випадковими
random.shuffle(questions)

# Цикл, який пропонує користувачу вибрати правильну відповідь для кожного питання
for i in range(len(questions)):
    # Виводимо питання та варіанти відповідей
    print(questions[i])
    user_answer = input("Введіть відповідь (a або b): ")
    # Перевіряємо, чи правильна відповідь була введена користувачем
    if user_answer == answers[i]:
        print("Правильно!")
        score += 1
    else:
        print("Неправильно.")
    print()

# Виводимо кількість правильних відповідей та вітальне повідомлення
print("Ви набрали", score, "балів.")
if score == len(questions):
    print("Вітаємо, ви дали правильні відповіді на всі питання!")
else:
    print("Спробуйте ще раз.")    

