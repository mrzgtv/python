new_list = [9, 6, 4, 3, 1]
print('Текущий рейтинг: ', new_list)
num = int(input("Введите новый элемент рейтинга: "))
for el in range(len(new_list)):
    if new_list[el] == num:
        new_list.insert(el + 1, num)
        break
    elif new_list[0] < num:
        new_list.insert(0, num)
        break
    elif new_list[-1] > num:
        new_list.append(num)
        break
    elif new_list[el] > num and new_list[el + 1] < num:
        new_list.insert(el + 1, num)
        break
print('Обновленный рейтинг', new_list)