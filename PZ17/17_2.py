#Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ № 2 – 9.

import tkinter as tk
from tkinter import messagebox

def check_number():
    try:
        number = int(entry.get())
        if 1 <= number <= 999: # Проверяем, находится ли число в диапазоне от 1 до 999
            if number % 2 == 0: # Проверяем, является ли число четным
                if 1 <= number < 10:
                    result = "Четное однозначное число"
                elif 10 <= number < 100:
                    result = "Четное двузначное число"
                else:
                    result = "Четное трехзначное число"
            else:
                if 1 <= number < 10:
                    result = "Нечетное однозначное число"
                elif 10 <= number < 100:
                    result = "Нечетное двузначное число"
                else:
                    result = "Нечетное трехзначное число"
        else:
            result = "Число вне диапазона 1-999"
    except ValueError:
        result = "Введено не целое число"
    messagebox.showinfo("Результат", result)

root = tk.Tk() # Создаем новое окно tkinter
root.title("Проверка четности числа")

label = tk.Label(root, text="Введите целое число от 1 до 999:") # Создаем метку с указанным текстом
label.pack() # Добавляем метку в окно

entry = tk.Entry(root) # # Создаем поле ввода
entry.pack()

button = tk.Button(root, text="Проверить", command=check_number) # Создаем кнопку с указанным текстом и связываем ее с функцией check_number
button.pack()

root.mainloop()