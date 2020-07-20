def fact(n):
    count = 1
    while count <= n:
        yield count
        count += 1


n = int(input("Введите число для вычисления факториала: "))
i = 1
a = 1
for el in fact(n):
    if i > n:
        break
    else:
        res = a * i
        a = res
        i += 1
print(a)