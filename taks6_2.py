class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc(self):
        weight = 25
        thickness = float(input('Введиту толщину дорожного полотна(см): '))
        calc = self.length * self.width * weight * thickness / 1000
        print(f'Для постройки дороги необходимо {calc} тонн асфальта')


asph_calc = Road(float(input('Введиту длину дороги(м): ')), float(input('Введиту ширину дороги(м): ')))
asph_calc.calc()
