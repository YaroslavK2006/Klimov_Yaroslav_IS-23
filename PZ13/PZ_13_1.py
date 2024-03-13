# В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).

def main():
    # Запрашиваем размер матрицы и создаем её
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Введите элемент [{i+1}][{j+1}]: ")))
        matrix.append(row)

    # Выводим матрицу
    print("Матрица:")
    for row in matrix:
        print(row)

    # Запрашиваем номер строки, сумму и произведение которой нужно найти
    n = int(input("Введите номер строки для нахождения суммы и произведения элементов: ")) - 1

    # Находим сумму и произведение элементов строки
    sum_row = sum(matrix[n])
    product_row = 1
    for element in matrix[n]:
        product_row *= element

    # Выводим результаты
    print(f"Сумма элементов строки {n+1}: {sum_row}")
    print(f"Произведение элементов строки {n+1}: {product_row}")

if __name__ == "__main__":
    main()
