# Ввод массива из 10 элементов
arr = [int(input(f"Введите элемент {i + 1}: ")) for i in range(10)]

# Нахождение максимального элемента
max_elem = max(arr)

# Сравнение элементов с максимальным
less_than_max = sum(1 for x in arr if x < max_elem)  # Количество меньших максимального
greater_than_max = sum(1 for x in arr if x > max_elem)  # Количество больших максимального

# Вывод результата
print(f"Массив: {arr}")
print(f"Максимальный элемент: {max_elem}")
print(f"Количество элементов меньше максимального: {less_than_max}")
print(f"Количество элементов больше максимального: {greater_than_max}")
