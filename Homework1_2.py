num_str = input("Введите число: ").strip()

if not num_str.isdigit():
    print("Ошибка: введено не число")
else:
    num = int(num_str)
    
    if num % 2 == 0:
        print(f"Число {num} является четным")
    else:
        print(f"Число {num} не является четным")
