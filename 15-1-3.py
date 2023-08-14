
class Base:
    price_class = 10
    my_price = 0

    def price(self):
        print(f'{self.__class__.__dict__}')
        print(f'{self.price_class}')
        print(f'Вызов метода класса {self.__class__}')
        return self.price_class


class InterFoo(Base):
    # price_class = 50

    def price(self):
        print(f'{self.__class__.__dict__}')
        print(f'{self.price_class}')
        print(f'Вызов метода класса {self.__class__}')
        return super().price() * 1.1


class Discount(InterFoo):
    # price_class = 100
    def price(self):
        print(f'Вызов метода класса {self.__class__}')
        print(f'{self.price_class}')
        return super().price() * 0.8 + self.my_price


print(Discount().price())