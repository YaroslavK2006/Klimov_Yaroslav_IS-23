n = int(input("Введите количество чисел (n):  "))
print(f"n = {n}")
numbers = [] # Создаем пустой список для хранения чисел
for i in range(n):
    num = int(input(f"Введите {i+1} число: "))
    print(f"numbers[{i}] = {num}")
    numbers.append(num)  # Добавляем число в список

m = 109 # Задаем значение m
print(f"m = {m}")
max_sum = 0
max_pair = None

for i in range(n):
    for j in range(i+1, n):
        if numbers[i] > numbers[j] and (numbers[i] + numbers[j]) % m == 0: # Проверяем что numbers[i] > numbers[j] и сумма делится на m
            print(f"Найдена пара: {numbers[i]} {numbers[j]}")
            if max_sum < numbers[i] + numbers[j]:
                max_sum = numbers[i] + numbers[j]
                max_pair = (numbers[i], numbers[j])
                print(f"Новая максимальная сумма: {max_sum}")

if max_pair:
    print(f"Результат: {max_pair[0]} {max_pair[1]}")
else:
    print("Подходящая пара не найдена")
