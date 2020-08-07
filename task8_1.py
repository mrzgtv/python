class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Данные введены верно'
                else:
                    return f'Ошибка! Введите год с 0 до 2020'
            else:
                return f'Ошибка! Введите месяц с 1 до 12'
        else:
            return f'Ошибка! Введите день с 1 до 31'

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day_month_year)}'


today = Date('07 - 08 - 2020')
print(today)
print(Date.valid(12, 12, 2099))
print(today.valid(1, 25, 2019))
print(Date.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(Date.valid(1, 11, 2000))
