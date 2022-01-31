i = 0
while i <= 150:
    value = i % 100
    number = value % 10
    text = ''

    if number > 1 and number < 5:
        text = '%\tпроцента'

    if number == 1:
        text = '%\tпроцент'

    if value > 10 and value < 20 or number >= 5 or number == 0:
        text = '%\tпроценов'

    print(i, text)

    i += 1
