def find_closest_value(R, A):
    closest_value = None  # Переменная closest_value будет использоваться для хранения ближайшего значения
    min_difference = float('inf')  # Переменной min_difference со значением бесконечности эта переменная будет содержать наименьшую разницу между текущим числом из списка и числом R

    for num in A:  # Цикл for который перебирает каждое число num из списка A
        difference = abs( num - R)  # Вычисляет разницу между числом num и значением R с помощью функции abs которая возвращает абсолютное значение
        if difference < min_difference:
            min_difference = difference  # Значение переменной min_difference обновляется на текущую разницу difference потому что она является новым наименьшим значением разницы
            closest_value = num

    return closest_value  # Возврат значения переменной closest_value из функции


R = 5
A = [1, 3, 7, 9, 11]
closest = find_closest_value(R,A)  # Вызов функции find_closest_value с аргументами R и A результат функции присваивается переменной closest
print(f"Ближайшее значение к {R} равно {closest}")
