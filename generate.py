number = input("Введите номер карты: ")

if len(number) == 16 and number.isdigit():
    print('*' * 12 + number[-4:])
else:
    print("Incorrect number")
