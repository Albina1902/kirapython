import random

scrt_number = random.randrange(1,100)
guess = None

print("Угадай число от 1 до 100. У тебя 3 попытки")

while guess != scrt_number: 
    guess = int(input("Введи число: "))

    if guess < scrt_number:
        print("Число меньше! Попробуй еще раз.")
    elif guess > scrt_number:
        print("Число больше! Попробуй еще раз.") 

print("Поздравляю! Правильно .")          