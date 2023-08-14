
class Base:
    def price(self):
        print(f'Вызов метода класса {self.__class__.__name__}')
        return 10


class InterFoo(Base):
    def price(self):
        print(f'Вызов метода класса {self.__class__.__name__}')
        return super().price() * 1.1


class Discount(InterFoo):
    def price(self):
        print(f'Вызов метода класса {self.__class__.__name__}')
        return super().price() * 0.8


print(Discount().price())