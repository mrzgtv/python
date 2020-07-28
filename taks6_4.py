class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f' {self.speed} км/ч'

    def police_or_not(self):
        if self.is_police:
            return f'{self.name} это полицейская машина'
        else:
            return f'{self.name} это НЕ полицейская машина'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'{self.speed} км/ч. Превышена максимальная скорость, ограничение 60 км/ч'
        else:
            return f'{self.speed} км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'{self.speed} км/ч. Превышена максимальная скорость, ограничение 40 км/ч'
        else:
            return f'{self.speed} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


sportcar = SportCar(210, "Красный", "Lada Granta Sport", False)
towncar = TownCar(59, "Зеленый", "Daewoo Matiz", False)
policecar = PoliceCar(112, "Белый", "УАЗ-Буханка", True)
workcar = WorkCar(45, "Желтый", "Камаз-5320", False)
print(policecar.turn_left())
print(f'{sportcar.go()} со скоростью {sportcar.show_speed()}')
print(f'{towncar.go()} со скоростью {towncar.show_speed()}')
print(f'{sportcar.police_or_not()}')
print(f'{towncar.police_or_not()}')
print(f'{workcar.police_or_not()}')
print(f'{policecar.police_or_not()}')
print(f'Когда {policecar.color} {policecar.go()}, {workcar.stop()}')
print(f'Когда {sportcar.color} {sportcar.go()}, {towncar.stop()}')
print(f'Скорость {sportcar.name} равна {sportcar.show_speed()}')
print(f'Скорость {workcar.name} равна {workcar.show_speed()}')
print(f'Скорость {towncar.name} равна {towncar.show_speed()}')
print(f'Скорость {policecar.name} равна {policecar.show_speed()}')
