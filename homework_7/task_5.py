import random

random_number = random.randint(1, 10)

while True:
    x = int(input("Введіть число від 1 до 10: "))
    if x == random_number:
        print("Ви вгадали!")
        break
    elif x < random_number:
        print("Загадане число більше.")
    else:
        print("Загадане число менше.")
