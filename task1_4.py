number = int(input('Введите целое положительное число: '))
while number < 0:
    print('Введено некорректное число:', number)
    number = int(input('Введите целое положительное число: '))
if number > 0:
    mx = number % 10
    number = number // 10
    while number > 0:
        if number % 10 > mx:
            mx = number % 10
        number = number // 10
    print(mx)
