class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByZero(9, 18)
print(DivisionByZero.divide_by_zero(9, 0))
print(DivisionByZero.divide_by_zero(9, 0.2))
print(div.divide_by_zero(888, 0))