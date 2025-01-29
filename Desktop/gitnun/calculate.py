import math

def calculate():
    print("Выберите операцию: ")
    print("1: Сложение (+)")
    print("2: Вычитание (-)")
    print("3: Умножение (*)")
    print("4: Деление (/)")
    print("5: Процент (%)")
    print("6: Степень (^)")
    print("7: Квадратный корень (√)")

    choice = input("Введите номер операции: ")

    if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7":
        num1 = float(input("Введите первое число: "))
        
        if choice in ["1", "2", "3", "4", "5", "6"]:
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
        elif choice == "5":
            print(f"Результат: {num1 * num2 / 100}")
        elif choice == "6":
            print(f"Результат: {num1 ** num2}")
        elif choice == "7":
            if num1 >= 0:
                print(f"Результат: {math.sqrt(num1)}")
            else:
                print("Ошибка: Квадратный корень из отрицательного числа не существует.")
    else:
        print("Неверный выбор. Попробуйте снова.")

calculate()
