str_in = input("Введите несколько значений через пробел: ")
for ind, el in enumerate(str_in.split(), 1):
    print(ind, el[0:10])
