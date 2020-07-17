product_qty = int(input('Введите количество товаров: '))
main_list = []
main_dict = []
a = 1
while a <= product_qty:
    main_dict = dict({'Название товара': input("Введите название товара "), 'Цена': input("Введите цену товара "), 'Количество': input('Введите количество товара '), 'Ед.изм.': input("Введите единицу измерения ")})
    main_list.append((a, main_dict))
    a += 1
for el in main_list:
    print(el)
