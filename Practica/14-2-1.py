# Задание 1 - продуктовая лавка

class Product:

    def __init__(self, name, price, count=1):
        self.name = name
        self.price = price
        self.__count = count

    @property
    def count(self):
        return self.__count

    def __str__(self):
        if (self.name == None) or (self.count == None):
            return ''
        return (f'{self.name} в количестве {self.count} шт по цене '
                f'{self.price} р., на общую сумму {self.count*self.price} р.')

    def sale_product(self, count):
        if (self.name == None) or (self.count == None):
            raise ValueError('товара нет на складе')

        if self.count < count:
            raise ValueError('количество продаваемого товара больше '
                             'имеющегося на складе')
        else:
            self.__count -= count

    def add_product(self, count):
        if (self.name == None) or (self.count == None):
            raise ValueError('товара нет на складе')
        self.__count += count

    def del_product(self):
        self.name = None
        self.__count = None
        self.price = None

def main():
    list_products = []
    list_products.append(Product('Сыр', 100))
    list_products.append(Product('Молоко', 70, 20))
    list_products.append(Product('Хлеб', 40, 50))

    print(*[temp_lp for temp_lp in list_products], sep='\n')

    list_products[0].add_product(100)
    print()
    print(*[temp_lp for temp_lp in list_products], sep='\n')

    list_products[1].sale_product(10)
    print()
    print(*[temp_lp for temp_lp in list_products], sep='\n')

    list_products[1].del_product()
    print()
    print(*[temp_lp for temp_lp in list_products], sep='\n')



if __name__ == '__main__':
    main()