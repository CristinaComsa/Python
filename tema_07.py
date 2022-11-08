from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplemented

    def descrie(self):
        print('Cel mai probabil am colturi')

class Patrat(FormaGeometrica):
    def aria(self):
        aria = self.__latura * self.__latura
        return aria

    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: noua latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura.')
        self.__latura = None

patrat = Patrat(5)
print(f'Aria patratului este {patrat.aria()}')
patrat.latura = 15
patrat.latura
del patrat.latura
patrat.latura

class Cerc(FormaGeometrica):
    def aria(self):
        aria = self.PI * self.__raza * self.__raza
        return aria

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter: noua raza este {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Deleter: Am sters raza.')
        self.__raza = None

    def descrie(self):
        print('Eu nu am colturi!')

cerc = Cerc(5)
print(f'Aria cercului este {cerc.aria()}')
cerc.raza = 10
cerc.raza
del cerc.raza
cerc.raza
cerc.descrie()








