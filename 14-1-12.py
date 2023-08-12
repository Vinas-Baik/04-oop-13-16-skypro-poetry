from time import perf_counter, sleep


class TodoList:

    def __init__(self, tasks):
        self.__tasks = tasks

    def __repr__(self):
        # return f'{self.__class__.__name__}([{", ".join([task for task in self.__tasks])}])'
        return (f'{self.__class__.__name__}({type(self.__tasks).__name__}['
                f'{", ".join([type(task).__name__ for task in self.__tasks])}])')

    def __str__(self):
        return '\n'.join([task for task in self.__tasks])

    def __add__(self, other: 'TodoList'):
        return TodoList(self.__tasks + other.__tasks)

    def __len__(self):
        return len(self.__tasks)

class ReIterator:

    def __init__(self, list_el):
        self.__list = list_el

    def __iter__(self):
        self.__start = len(self.__list)
        return self

    def __next__(self):
        self.__start -= 1
        if self.__start >= 0:
            return self.__list[self.__start]
        raise StopIteration

    def __len__(self):
        return len(self.__list)

class MyOpen:

    def __init__(self, filename, mode='r'):
        """
        Класс, который создает объект, который можно использовать
        вместо open(), чтобы автоматически закрывать файл.
        :param filename: имя файла
        :param mode: режим открытия файла (по умолчанию 'r')
        """
        self.__filename = filename
        self.__mode = mode

    def __enter__(self):
        print(f'Файл {self.__filename} был открыт')
        self.__start = perf_counter()
        self.fp = open(self.__filename, self.__mode)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()
        self.__start = perf_counter() - self.__start
        print(f'Файл был открыт {self.__start} секунд и теперь успешно закрыт.')

def print_class(list: 'TodoList'):
    print(list)
    print(f'{repr(list)} - длина списка {len(list)}')
    print(list.__class__.__name__)
    print()

class TL:

    def __init__(self, tasks):
        self.__tasks = tasks

    @property
    def tasks(self):
        return self.__tasks

    def __add__(self, other):
        next_list = self.__tasks + other.tasks
        return next_list

    def __str__(self):
        return f'{self.__tasks}'


print('От Глеба:')
temp_gleb = TL(TL([1,2]) + TL ([3,4]))
print(temp_gleb)
print(temp_gleb.__class__.__name__)
print('-----')

list1 = TodoList(['task1', 'task2'])
print_class(list1)

list2 = TodoList(['task3', 'task4'])
print_class(list2)

list3 = list1 + list2
print_class(list3)

# ----------------

x = ReIterator([8, 9, 10, 1, 2, 3, 4])
for i in x:
    print(i)

print(f'Длина списка - {len(x)}')
print()
#
# # -------------------
#
with MyOpen('text.txt', 'r') as fp:
    content = fp.read()
    print('Чтение данных 2 секунды...')
    sleep(2)

print('Продолжение кода...')