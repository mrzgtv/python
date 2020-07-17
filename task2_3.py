seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month_n = int(input('Введите порядковый номер месяца (1-12): '))
while month_n < 1 or month_n > 12:
    print("Введен некорректный № месяца!")
    month_n = int(input('Введите порядковый номер месяца (1-12): '))
if month_n == 12 or month_n == 1 or month_n == 2:
    print(seasons_list[0])
    print(seasons_dict.get(1))
elif month_n == 3 or month_n == 4 or month_n == 5:
    print(seasons_list[1])
    print(seasons_dict.get(2))
elif month_n == 6 or month_n == 7 or month_n == 8:
    print(seasons_list[2])
    print(seasons_dict.get(3))
elif month_n == 9 or month_n == 10 or month_n == 11:
    print(seasons_list[3])
    print(seasons_dict.get(4))
