#Дан словарь с произвольным количеством элементов. Выяснить имеется ли в нем элемент с ключом «фрукт = груша» и если он присутствует, то удалить его из словаря. Вывести на экран первоначальный словарь и измененный.
dictionary = {"фрукт": "груша", "цвет": "красный", "животное": "собака"}

print("Первоначальный словарь:")
print(dictionary)

if "фрукт" in dictionary and dictionary["фрукт"] == "груша":
    del dictionary["фрукт"]

print("Измененный словарь:")
print(dictionary)