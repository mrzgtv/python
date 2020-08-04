from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, input_par):
        self.input_par = input_par

    @abstractmethod
    def total_fabrics(self):
        pass

    def __add__(self, other):
        return self.total_fabrics + other.total_fabrics


class Coat(Clothes):
    @property
    def total_fabrics(self):
        print(f'Расход ткани для пальто - {round(self.input_par / 6.5) + 0.5}')
        return round(self.input_par / 6.5) + 0.5


class Jacket(Clothes):
    @property
    def total_fabrics(self):
        print(f'Расход ткани для костюма - {(self.input_par * 2) + 0.3}')
        return (self.input_par * 2) + 0.3


coat = Coat(20)
jacket = Jacket(30)
print(coat + jacket)
