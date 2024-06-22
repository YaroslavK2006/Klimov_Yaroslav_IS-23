# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857 год и поместить ее в новый текстовый файл.

import re
with open('Dostoevsky.txt', 'r',  encoding='utf-8') as file: # Открывает файл 'Dostoevsky.txt' в режиме чтения
    text = file.read()
pattern = r'1857 год\n.*?(?=\nВ 1859|$)' # Определяет регулярное выражение которое ищет строку 1857 год  до встречи строки В 1859 или конца строки
pattern = re.compile(pattern, re.DOTALL)
matches = pattern.findall(text)
with open('1857_year.txt', 'w', encoding='utf-8') as new_file: #Открывает файл 1857_year.txt в режиме записи
        new_file.write('\n'.join(matches))