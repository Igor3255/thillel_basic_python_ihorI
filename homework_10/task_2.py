import random
import string

def generate_password(length):
    # Перевіряємо, чи вказана довжина менше 8
    if length < 8:
        raise ValueError("Довжина паролю повинна бути не менше 8 символів")

    # Задаємо доступні символи для паролю
    available_chars = string.ascii_letters + string.digits + "_"
    
    # Генеруємо пароль
    password = ""
    while True:
        # Додаємо випадковий символ з доступних
        password += random.choice(available_chars)
        
        # Перевіряємо, чи пароль задовольняє умови
        if (len(password) >= length and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            not any(password[i] == password[i+1] for i in range(len(password)-1))):
            return password


password = generate_password(10)
print(password)