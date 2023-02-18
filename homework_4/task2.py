text = input("Введите информацию о человеке в формате 'имя*дата_рождения*дата_смерти' (например, 'Taras Shevchenko*1814-03-09*1861-03-10'): ")
new_text = text.split('*')
name = new_text[0]
age = int(new_text[2][0:4]) - int(new_text[1][0:4])
print('Name:', name)
print('Age:', age, 'years')

