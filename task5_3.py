with open('text_3.txt', 'r') as my_list:
    sal = []
    poor = []
    new_list = my_list.read().split('\n')
    for el in new_list:
        el = el.split()
        if float(el[1]) < 20000:
            poor.append(el[0])
        sal.append(el[1])
print(f'Оклад меньше 20.000: {poor}')
print(f'Cредний оклад: {sum(map(float, sal)) / len(sal)}')