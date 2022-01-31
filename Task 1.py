# Формат вывода результата:
#
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры/Тесты:
#
# duration = 53: 53 сек
# duration = 153: 2 мин 33 сек
# duration = 4153: 1 час 9 мин 13 сек
# duration = 400153: 4 дн 15 час 9 мин 13 сек


# result = day + hour + min + sec
# if duration < 60:
#     print(sec)
# while result > 0:
#     min += 1
#     result -= 60
# print(min, sec)
# while duration >= 60:
#     min = 1
#     print(min, "мин")
#     break
duration = int(input("Введите количсетво секунд: "))
# sec = 1
minute = 0
hour = 0
day = 0
while duration > 59:
    minute = minute + 1
    duration = duration - 60
    if minute > 59:
        hour = hour + 1
        minute = 1
        if hour > 24:
            day = day + 1
            hour = 1
if day > 0:
    print(day, "день", hour, "час", minute, "мин", duration, "сек")
elif hour > 0:
    print(hour, "час", minute, "мин", duration, "сек")
elif minute > 0:
    print(minute, "мин", duration, "сек")
else:
    print(duration, "сек")
# duration = int(input("Введите количсетво секунд: "))


