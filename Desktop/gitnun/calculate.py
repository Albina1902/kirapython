def calculate():
    print("Выберите операцию: ")
    print("1: Сложение (+)")
    print("2: Вычитание (-)")
    print("3: Умножение (*)")
    print("4: Деление (/)")

    choice = input("Введите номер операции: ")

    if choice == "1" or choice == "2" or choice == "3" or choice == "4":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
            
        if choice == "1":
            print(f"Результат: {num1 + num2}")
        elif choice == "2":
            print(f"Результат: {num1 - num2}")
        elif choice == "3":
            print(f"Результат: {num1 * num2}")
        elif choice == "4":
            if num2 != 0:
                print(f"Результат: {num1 / num2}")
            else:
                print("Ошибка: Делить на 0 нельзя.")
    else:
        print("Неверный выбор. Попробуйте снова.")

        

calculate()