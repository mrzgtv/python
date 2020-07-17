dayn = int(input('Результат 1-го дня(км): '))
dayx = int(input('Цель (км): '))
day = 1
dailygrow = 1.1
while dayn < dayx:
    if dayn < dayx:
        dayn = dayn * dailygrow
    day = day + 1
print('Цель будет достигнута на:', f"{day:.0f}" ' день!!!')


