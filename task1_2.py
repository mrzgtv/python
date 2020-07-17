sec = int(input("Введите время в секундах(sec): "))
minutes = sec // 60
hours = minutes // 60
print(f"{hours:02d}:{minutes % 60:02d}:{sec % 60:02d}")
