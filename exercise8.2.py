
def main():
    # Ввод размера матрицы
    n = int(input("Введите порядок квадратной матрицы (N): "))
    if n <= 0 or n % 2 == 0:
        print("Ошибка: порядок матрицы должен быть нечетным положительным числом.")
        return

    # Ввод матрицы
    print("Введите элементы матрицы построчно, через пробел:")
    matrix = []
    for i in range(n):
        row = list(map(float, input().split()))
        if len(row) != n:
            print("Ошибка: количество элементов в строке должно быть равно N.")
            return
        matrix.append(row)

    # Нахождение пересечения диагоналей
    center_index = n // 2

    # Поиск наибольшего элемента среди главной и побочной диагоналей
    max_value = float('-inf')
    max_position = None

    for i in range(n):
        # Главная диагональ: элементы matrix[i][i]
        if matrix[i][i] > max_value:
            max_value = matrix[i][i]
            max_position = (i, i)

        # Побочная диагональ: элементы matrix[i][n - 1 - i]
        if matrix[i][n - 1 - i] > max_value:
            max_value = matrix[i][n - 1 - i]
            max_position = (i, n - 1 - i)

    # Меняем наибольший элемент с элементом на пересечении диагоналей
    center_value = matrix[center_index][center_index]
    max_i, max_j = max_position

    matrix[center_index][center_index], matrix[max_i][max_j] = max_value, center_value

    # Вывод результата
    print("Обработанная матрица:")
    for row in matrix:
        print(" ".join(map(str, row)))

# Запуск программы
main()
