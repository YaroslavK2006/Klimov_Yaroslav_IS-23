#1) В последовательности на n целых чисел найти и вывести:
# минимальный среди положительных
# элементы кратные пяти
# их среднее арифметическое
def main():
    n = int(input("Введите количество целых чисел в последовательности: "))
    sequence = [int(input(f"Введите число #{i+1}: ")) for i in range(n)] #  Создает список sequence, заполняя его целыми числами, введенными пользователем по одному для каждого элемента в последовательности.

    positive_numbers = [num for num in sequence if num > 0] # Создает список
    multiples_of_five = [num for num in sequence if num % 5 == 0]

    min_positive = min(positive_numbers) if positive_numbers else None
    average_multiples_of_five = sum(multiples_of_five) / len(multiples_of_five) if multiples_of_five else None #  Вычисляет среднее значение элементов в multiples_of_five если таковые есть в противном случае присваивает None

    print(f"1.1) Минимальный среди положительных: {min_positive}" if min_positive is not None else "1.1) В последовательности нет положительных чисел")
    print(f"1.2) Элементы кратные пяти: {multiples_of_five}")
    print(f"1.3) Среднее арифметическое элементов кратных пяти: {average_multiples_of_five}" if average_multiples_of_five is not None else "1.3) В последовательности нет элементов, кратных пяти")

if __name__ == "__main__": # Проверяет запущен ли скрипт напрямую
    main() # Вызывает функцию main()
