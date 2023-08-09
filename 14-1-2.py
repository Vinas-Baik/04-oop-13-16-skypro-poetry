class BigFuncClass:

    def __init__(self, attr1, attr2):
        # __init__ — магический метод для инициализации объекта из класса:
        self.attr1 = attr1
        self.attr2 = attr2

    def __repr__(self):
        # __repr__  — магический метод для отображения информации об объекте
        # класса в режиме отладки (для разработчиков):
        return f'{self.__class__.__name__}({self.attr1}, {self.attr2})'

    def __str__(self):
        # __str__ — магический метод для отображения информации об объекте
        # класса для пользователей, например для функций print, str
        return f'{self.attr1} - {self.attr2}'

    def __len__(self):
        # __len__ - магический метод, который позволяет применять функцию
        # len() к экземплярам класса:
        return len(f'{self.attr1}{self.attr2}')

    def __add__(self, other):
        # __add__ — магический метод, который позволяет прибавлять
        # к экземпляру класса объект произвольного типа:
        self.attr1 += other.attr1
        self.attr2 += other.attr2

    def __call__(self, *args, **kwargs):
        # __call__ — магический метод, который позволяет
        # экземпляр класса сделать callable-объектом, т. е. вызвать
        # как обычную функцию для выполнения заложенной функциональности
        print(f'Был вызван объект {self}')

    def __iter__(self):
        # __iter__  — магический метод, который возвращает сам итератор для
        # перебора объекта:
        self.current_value = -1
        return self

    def __next__(self):
        # __next__  — магический метод, который позволяет переходить
        # к следующему значению и его считывать:
        if self.current_value + 1 < len(self):
            self.current_value += 1
            return str(self)[self.current_value]
        else:
            raise StopIteration

    def __enter__(self):
        # __enter__  — магический метод, который определяет,
        # что должен сделать менеджер контекста в начале блока,
        # созданного инструкцией with:
        self.fp = open(self.attr1, self.attr2)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        # __exit__ — магический метод, который определяет действия
        # менеджера контекста после того, как блок будет выполнен или прерван
        # во время работы; отрабатывает автоматически.
        self.fp.close()

bfc1 = BigFuncClass('1', '2')
bfc2 = BigFuncClass('3', '4')
print(bfc1)
print(bfc2)
print(bfc1.__repr__())
print(bfc2.__repr__())