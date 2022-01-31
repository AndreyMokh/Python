# Для кубов нечётных чисел от 1 до 1000. Вычислить сумму чисел, сумма цифр кубов которых делится нацело
#
# Техническое задание:
#
# Для всех нечетных чисел диапазона [1, 1000]
# При решении задачи использовать только арифмитическое операции и циклы.
# Не используем списки, функцию range, преобразование в строку/список.
# Формат вывода результата:
# Вывод на экран формить в виде: xxxxxxx ^3: xxx; sum: xxx [сумма цифр]
# Например:
# 19 ^3: 6859 sum: 19 [ 28 ]
# 31 ^3: 29791 sum: 50 [ 28 ]
# 43 ^3: 79507 sum: 93 [ 28 ]
#
# Примеры:
# число 19, 19 ^ 3 = 6859, сумма чисел 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Поэтому 19 включаем в вывод.


number = 1
result = 0
while number <= 1000:
    number = number + 1

    if number % 2 != 0:
        cube_number = number ** 3
        sum_of_number = 0
        current_number = cube_number

        while current_number > 0:
            sum_of_number = sum_of_number + current_number % 10
            current_number = int(current_number / 10)

        if sum_of_number % 7 == 0:
            result = result + number
print(result)


