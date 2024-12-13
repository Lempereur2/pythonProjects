def main():
    # Ввод размера матрицы
    n = int(input("Введите размер квадратной матрицы (N): "))
    if n <= 0:
        print("Ошибка: размер матрицы должен быть больше 0.")
        return

    # Ввод матрицы
    print("Введите элементы матрицы построчно, через пробел:")
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print("Ошибка: количество элементов в строке должно быть равно N.")
            return
        matrix.append(row)

    # Нахождение наибольших элементов в строках
    max_in_rows = [max(row) for row in matrix]

    # Нахождение наименьших элементов в столбцах
    min_in_columns = [min(matrix[i][j] for i in range(n)) for j in range(n)]

    # Вывод результатов
    print("Наибольшие элементы в строках:")
    for i, value in enumerate(max_in_rows):
        print(f"Строка {i + 1}: {value}")

    print("Наименьшие элементы в столбцах:")
    for j, value in enumerate(min_in_columns):
        print(f"Столбец {j + 1}: {value}")

# Запуск программы
main()
