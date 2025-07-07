age_str = input("Введите ваш возраст: ").strip()

try:
    age = int(age_str)
    if age < 0:
        print("Ошибка: возраст не может быть отрицательным!")
    elif age >= 18:
        print("Вы совершеннолетний.")
    else:
        print("Вы несовершеннолетний.")
except ValueError:
    print("Ошибка: введено не число!")
