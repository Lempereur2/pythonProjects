def is_prime(n, divisor=None):
    """
    Рекурсивная функция для проверки, является ли число n простым.

    """
    if divisor is None:
        divisor = n - 1

    # Базовый случай: если дошли до 1, число простое
    if divisor == 1:
        return True

    # Если n делится на divisor, то оно составное
    if n % divisor == 0:
        return False

    # Рекурсивный вызов с уменьшением делителя
    return is_prime(n, divisor - 1)

# Чтение числа от пользователя
n = int(input("Введите натуральное число n (> 1): "))

# Проверка числа на простоту
if is_prime(n):
    print("YES")
else:
    print("NO")
