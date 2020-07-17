def my_f(a, b):
    try:
        a = int(a)
        b = int(b)
        res = a / b
        return res
    except ValueError:
        return 'Error! Please enter correct numbers!'
    except ZeroDivisionError:
        return 'Error! Division by zero!'


print(my_f(input("Enter first #: "), input("Enter second #: ")))