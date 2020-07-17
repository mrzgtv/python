rev = int(input('Введите выручку Вашей фирмы: '))
costs = int(input('Введите издержки Вашей фирмы: '))
if rev > costs:
    profit = rev - costs
    print('Прибыль Вашей фирмы составляет: $', profit)
    print('Рентабельность выручки составляет:', f"{profit / rev:.2f}")
    staff = int(input('Введите численность сотрудников: '))
    print('Прибыль фирмы в расчете на сотрудника:', f"{profit / staff:.2f}")
if rev < costs:
    loss = costs - rev
    print('Убыток Вашей фирмы составляет: $', loss)
