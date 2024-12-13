# Ввод чисел a и b
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))

# Условия для вычисления x
if a < b and b > 4:
    x = a + b
elif a > b:
    x = a - b
else:
    x = a ** 2

# Вывод результата
print(f"Значение x: {x}")