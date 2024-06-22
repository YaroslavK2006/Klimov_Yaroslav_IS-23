# Из предложенного текстового файла (text18-11.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить строку наименьшей длины.


with open('text18-11.txt', 'r', encoding='utf-8') as file:# Cтрока открывает файл с именем 'text18-11.txt' в режиме чтения с кодировкой 'utf-8'
    content = file.read() # Эта строка читает содержимое файла и сохраняет его в переменной content
    punctuation_count = sum([1 for symbol in content if symbol in '.,:;!?'])

print(content)
print('Количество знаков препинания:', punctuation_count)

lines = content.split('\n') # Эта строка разбивает содержимое файла на список строк используя символ новой строки в качестве разделителя

shortest_line = min(lines, key=len) # Эта строка находит самую короткую строку в списке строк.

with open('shortest_line.txt', 'w', encoding='utf-8') as file:
    file.write(shortest_line)