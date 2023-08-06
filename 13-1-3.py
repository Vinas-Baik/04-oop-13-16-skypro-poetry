import datetime


class Employee:
    """Класс для представления сотрудника."""

    # Переменная на уровне класса для подсчета количества сотрудников
    nummer_of_employees = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@email.com'

        Employee.nummer_of_employees += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f'{self.fullname()} {self.email} -  {self.pay}'

    # Создаем classmethod в классе Employee
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # создаем экземпляр класса из строки с разделителем -
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

list_Employer = []

# Создаем двух сотрудников
list_Employer.append(Employee('Ivan', 'Ivanov', 50000))
list_Employer.append(Employee('Pert', 'Petrov', 60000))

print(*[f'emp_{num} = {emp}' for num, emp in enumerate(list_Employer)], sep='\n')

print()

print(f'Employee.raise_amt = {Employee.raise_amt}')
print(*[f'emp_{num}.raise_amp = {emp.raise_amt}' for num, emp in enumerate(list_Employer)], sep='\n')

list_Employer[0].raise_amt = 0.8
Employee.set_raise_amt(1.05)

print()

print(f'Employee.raise_amt = {Employee.raise_amt}')
print(*[f'emp_{num}.raise_amp = {emp.raise_amt}' for num, emp in enumerate(list_Employer)], sep='\n')

print()

# Создаем строку и вызываем метод @classmethod (который создает новый элемент
# класса
list_Employer.append(Employee.from_string('Jon-Snow-70000'))
list_Employer.append(Employee.from_string('Ivan-User-30000'))
list_Employer.append(Employee.from_string('Elena-Nikitina-90000'))

print(*[f'emp_{num} = {emp}' for num, emp in enumerate(list_Employer)], sep='\n')


print()

print(f'Employee.raise_amt = {Employee.raise_amt}')
print(*[f'emp_{num}.raise_amp = {emp.raise_amt}' for num, emp in enumerate(list_Employer)], sep='\n')

print()


list_Employer[4].raise_amt = 1
Employee.set_raise_amt(1.06)

print(f'Employee.raise_amt = {Employee.raise_amt}')
print(*[f'emp_{num}.raise_amp = {emp.raise_amt}' for num, emp in enumerate(list_Employer)], sep='\n')

print()

print(f'Количество сотрудников: {Employee.nummer_of_employees}')

my_date = datetime.date(2023, 1, 25)
print(Employee.is_workday(my_date))