orig_list = []
n = int(input('Введите количество элементов списка: '))
for i in range(n):
    orig_list.append((input('Введите элемент списка: ')))

for i in range(1, len(orig_list), 2):
    orig_list[i - 1], orig_list[i] = orig_list[i], orig_list[i - 1]
print(' '.join([str(i) for i in orig_list]))
