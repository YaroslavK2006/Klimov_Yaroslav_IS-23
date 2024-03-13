#2) Иззаданнойстрокиотобразить только символы пунктуации. Использовать
#библиотеку string.
#Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string

# Заданная строка
s = '--msg-template="$FileDir$\\{path}:{line}:{column}:{C} ({symbol}){msg}"'

# Используем списковое включение и генератор для извлечения символов пунктуации
punctuation_chars = [char for char in s if char in string.punctuation]

# Выводим результат
print("Символы пунктуации из заданной строки:")
print(''.join(punctuation_chars))
