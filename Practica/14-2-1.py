# Задание 1 - продуктовая лавка

class Product:

    def __init__(self, name, price, count=1):
        self.__name = name
        self.price = price
        self.__count = count

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, new_count):
        self.__count = new_count


    @property
    def name(self):
        return self.__name

    def __str__(self):
        if (self.name == None) or (self.count == None):
            return ''
        return (f'{self.name} в количестве {self.count} шт по цене '
                f'{self.price} р., на общую сумму {self.count*self.price} р.')


    def add_count(self, count):
        if (self.name == None) or (self.count == None):
            raise ValueError('товара нет на складе')
        if self.count + count < 0:
            print('\n\tОШИБКА: -> количество продаваемого товара больше имеющегося на складе !\n')
            return
        self.__count += count

class Category:

    def __init__(self, name, products=[]):
        self.name = name
        self.__products = products
        self.__is_active = True

    @property
    def products(self):
        return self.__products

    @property
    def is_active(self):
        return self.__is_Active

    @is_active.setter
    def is_active(self, set_active):
        self.__is_Active = set_active

    def add_product(self, product: Product):
        is_find_product = False
        for index_pr, temp_pr in enumerate(self.products):
            if temp_pr.name.lower().split() == product.name.lower().split():
                is_find_product = True
                if product.count != None:
                    self.products[index_pr].add_count(product.count)
                if product.price != None:
                    self.products[index_pr].price = product.price
                break
        if not is_find_product:
            if product.count == None:
                product.count = 1
            if product.price == None:
                product.price = 0
            self.products.append(product)


    def del_product(self, pruduct_name):
        is_find_product = False

        for index_pr, temp_pr in enumerate(self.products):
            if temp_pr.name.lower().split() == product_name.lower().split():
                is_find_product = True
                self.products.pop(index_pr)
                break

    def __str__(self):
        return '\n'.join(f'{temp_lp}' for temp_lp in self.products)


def main():
    category1 = Category('Молочка')

    category1.add_product(Product('Сыр', 100))
    category1.add_product(Product('Молоко', 70, 20))
    category1.add_product(Product('Хлеб', 40, 50))

    print(category1)

    category1.add_product(Product('Сыр', None, 100))
    print()
    print(category1)

    category1.add_product(Product('Сыр', 500, None))
    print()
    print(category1)

    category1.add_product(Product('Сыр', 500, -10))
    print()
    print(category1)

    category1.add_product(Product('Сыр', 500, -100))
    print()
    print(category1)

    category1.add_product(Product('Сыр твердый', 500, None))
    category1.add_product(Product('Сыр в подарок', None, 10))
    print()
    print(category1)



if __name__ == '__main__':
    main()