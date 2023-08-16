class Employee:

    def __init__(self, first, last):
        super().__init__()
        self.first = first
        self.last = last

class MixinLog:
    ID = 1

    def __init__(self):
        self.id = self.ID
        MixinLog.ID += 1

    def order_log(self):
        print(f'{self.id}-й сотрудник')

class Developer(Employee, MixinLog):
    pass

dev1 = Developer('Ivan', 'Ivanov')
dev1.order_log()

dev2 = Developer('Elena', 'Ivanova')
dev2.order_log()