name = input("Введите имя: ").strip()
surname = input("Введите фамилию: ").strip()
age = input("Введите возраст: ").strip()

print("Реализация через format:")
print("Ваше имя: {0}, Фамилия: {1}, Возраст: {2} лет.".format(name, surname, age))

print("Реализация через f-string:")
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет.")