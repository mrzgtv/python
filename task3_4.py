#Первый вариант

def my_func(a, b):
    try:
        a = abs(float(a))
        b = -abs(int(b))
        res = a ** b
        return res
    except ValueError:
        return 'Error! Please enter correct numbers!'
    except ZeroDivisionError:
        return 'Error! ZERO cannot be raised to a negative power!'


print(my_func(a=input('Введите действительное положительное число: '), b=input('Введите целое отрицательное число: ')))

'''Второй вариант

def my_func(a, b):
    try:
        a = abs(int(a))
        b = -abs(int(b))
        if a == 0 or b == 0:
            return 'Sorry, our program can not work with ZERO!'
        else:
            if b < 0:
                a = 1.0 / a
                b = -b
                res = 1
        while b > 0:
            res = res * a
            b = b - 1
        return res
    except ValueError:
        return 'Error! Please enter correct numbers!'
        
        
print(my_func(a=input('Введите число: '), b=input('Введите степень: ')))'''