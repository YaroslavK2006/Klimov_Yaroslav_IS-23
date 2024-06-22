# Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Количество положительных элементов в первой половине:

numbers = [i for i in range(-10, 11)]
with open('input.txt', 'w') as file: # Открывает файл с именем 'input.txt' в режиме записи
    file.write(' '.join(map(str, numbers)))

with open('input.txt', 'r') as file: # Открывает в режиме чтения
    numbers = list(map(int, file.read().split())) # Эта строка читает содержимое файла разбивает его на список строк ( используя пробелы) преобразует каждую строку в целое число и присваивает результат переменной numbers

count = len(numbers)
min_element = min(numbers)
positive_count = sum(1 for num in numbers if num > 0) # Это строка подсчитывает количество положительных элементов в списке
first_half_positive_count = positive_count // 2

with open('output.txt', 'w') as file: # Открывает файл с именем 'output.txt' в режиме записи
    file.write(f'Исходные данные: {numbers}\n')
    file.write(f'Количество элементов: {count}\n')
    file.write(f'Минимальный элемент: {min_element}\n')
    file.write(f'Количество положительных элементов в первой половине: {first_half_positive_count}')