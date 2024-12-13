# Ввод массива из 10 элементов
arr = [int(input(f"Введите элемент {i + 1}: ")) for i in range(10)]

# Вычисление суммы чисел, которые больше 5
sum_greater_than_5 = sum(x for x in arr if x > 5)

# Вывод результата
print(f"Массив: {arr}")
print(f"Сумма чисел, которые больше 5: {sum_greater_than_5}")
