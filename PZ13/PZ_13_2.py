# В матрице найти сумму элементов второй половины матрицы.
def sum_second_half(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows % 2 != 0:
        return "Матрица должна иметь четное количество строк"

    half_rows = rows // 2
    second_half_sum = 0

    for i in range(half_rows, rows):
        for j in range(cols):
            second_half_sum += matrix[i][j]

    return second_half_sum


# Пример матрицы
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

result = sum_second_half(matrix)
print("Сумма элементов второй половины матрицы:", result)
