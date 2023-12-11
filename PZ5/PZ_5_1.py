# Составить функцию, которая напечатает сорок любых символов.
import random # Импортируем модуль 'random' для генерации случайных символов
import string # Импортируем модуль 'string' для доступа к функциям работы со строками.

def print_forty_random_chars():
    random_chars = ''.join(random.choice(string.printable) for _ in range(40))
    # Генерируем случайную строку из 40 символов с помощью функции 'random.choice()' из модуля 'string.printable'.
    # Функция 'random.choice()' выбирает случайный символ из множества 'string.printable'.
    # Цикл 'for' используется для повторения этого процесса 40 раз.
    # Функция ''.join()', которая объединяет символы в одну строку.

    print(random_chars)

print_forty_random_chars()
