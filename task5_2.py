#Подсчет количества строк и слов в строке (из файла сохраненного в первой задаче)#

with open("text_1.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = line.count(" ") + 1
        print(f"{letters} слов в строке")
    print(f"Количество строк: {lines}")