
number = int(input("Введите целое число от 1 до 999: "))

if 1 <= number <= 999:
    if number % 2 == 0:
        if 1 <= number < 10:
            print("Четное однозначное число")
        elif 10 <= number < 100:
            print("Четное двузначное число")
        else:
            print("Четное трехзначное число")
    else:
        if 1 <= number < 10:
            print("Нечетное однозначное число")
        elif 10 <= number < 100:
            print("Нечетное двузначное число")
        else:
            print("Нечетное трехзначное число")
else:
    print("Число вне диапазона 1-999")

