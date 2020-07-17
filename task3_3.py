def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif b < a < c:
        return a + c
    else:
        return b + c


print(my_func(28.3, 32.7, 10))