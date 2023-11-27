n = int(input("Введите целое число N: "))
if n > 0:
    result = 1.0
    for i in range(1,n + 1):
        result = result * 1.1 * i
    print(f"Произведение {result}")
else:
    print("Пожалуйста, введите положительное целое число.")