#2) Иззаданнойстрокиотобразить только символы пунктуации. Использовать
#библиотеку string.
#Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string # Импортируем модуль string

s = '--msg-template="$FileDir$\\{path}:{line}:{column}:{C} ({symbol}){msg}"'

# Создаем список символов пунктуации из строки s
punctuation_chars = [char for char in s if char in string.punctuation]

print("Символы пунктуации из заданной строки:")
print(''.join(punctuation_chars))
