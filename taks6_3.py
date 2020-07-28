class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return f'{sum(self._income.values())}'


result = Position('Ivan', 'Ivanov', 'Manager', 134343, 10000)
print(result.get_full_name())
print(result.position)
print(result.get_total_income())
