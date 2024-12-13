# Ввод числа
number = input("Введите двузначное число: ")

# Проверка длины и условия
if len(number) == 2 and number.isdigit():
    if number[0] == number[1]:
        print("Да")
    else:
        print("Нет")
else:
    print("Ошибка: введите корректное двузначное число.")