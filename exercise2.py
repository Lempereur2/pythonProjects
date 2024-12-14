import math
# Ввод значений переменных x и t
x = int(input("Введите значение x: "))
t = int(input("Введите значение t: "))

# Вычисление выражения
try:
    z = ((9 * math.pi * t + 10 * math.cos(x)) / (math.sqrt(t) - math.fabs(math.sin(t)))) * math.pow(math.e, x)
    # Вывод результата с форматированием
    print("Результат вычисления z: {0:.2f}".format(z))
except ZeroDivisionError:
    print("Ошибка: деление на ноль.")
except ValueError:
    print("Ошибка: недопустимое значение (например, корень из отрицательного числа).")
