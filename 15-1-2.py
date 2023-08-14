class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        print(self.raise_amt)
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    # Переопределяем метод базового класса
    def __init__(self, first, last, pay, prog_lang):
        # Вызываем метод базового класса
        super().__init__(first, last, pay)
        # Дополнительный код
        self.prog_lang = prog_lang

    def fullname(self):
        return f'{super().fullname()} / {self.prog_lang} / {self.pay}'

    def print_develop(self):
        print()
        print(f'  Методы/переменные класса: {self.__dir__()}')
        print(f'                Имя класса: {self.__class__.__name__}')
        print(f'        Родительский класс: {self.__class__.__bases__}')
        print()
        print(f'До применения коэффициента raise_amt {super().raise_amt}: {self.fullname()}')
        super().apply_raise()
        print()
        print(f'Значения/переменные класса: {self.__dict__}')
        print(f'                Имя класса: {self.__class__.__name__}')
        print(f'        Родительский класс: {self.__class__.__bases__}')
        print()
        print(f'После применения коэффициента raise_amt {super().raise_amt}: {self.fullname()}')

    def apply_raise(self, type_func=True):
        if type_func:
            print(self.raise_amt)
            self.pay = int(self.pay * self.raise_amt)
        else:
            super().apply_raise()


dev_1 = Developer('Ivan', 'Ivanov', 70000, 'Python')
dev_2 = Developer('Petr', 'Petrov', 70000, 'C++')
# dev_1.print_develop()
# dev_2.print_develop()
print(dev_1.fullname())
dev_1.apply_raise()
print(dev_1.fullname())

print(dev_2.fullname())
dev_2.apply_raise(False)
print(dev_2.fullname())
