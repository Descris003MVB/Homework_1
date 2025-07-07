while True:
    user_input = input("Введите число: ").strip()

    if user_input.lower() == "exit":
        print("Выход из программы...")
        break

    if user_input.lstrip('-').isdigit():
        digits_count = len(user_input.lstrip('-'))
        print(f"В этом числе {digits_count} цифр(ы).")
    else:
        print("Ошибка: данные не являются числом.")
