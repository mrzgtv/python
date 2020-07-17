def my_sum():
    total_sum = 0
    quit_f = False
    while quit_f == False:
        number = input('Input numbers or Q for quit - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                quit_f = True
                break
            else:
                res = res + int(number[el])
        total_sum = total_sum + res
        print(f'Current sum is {total_sum}')
    print(f'Your final sum is {total_sum}')


my_sum()