from functools import reduce

new_list = [el for el in range(99, 1001) if el % 2 == 0]


def my_func(el, prev_el):
    return el * prev_el


print(reduce(my_func, new_list))

'''Результат умножения очень большой. Для проверки использовал range(3, 11). 4*6*8*10 = 1920'''