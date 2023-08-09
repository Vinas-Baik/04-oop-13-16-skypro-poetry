class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f'{self.fullname} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)

emp_1 = Employee('Ivan', 'Ivanov', 50000)
print(emp_1)

emp_2 = Employee('Test', 'Employee', 60000)
print(emp_1 + emp_2)

print(len(emp_1))