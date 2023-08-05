class Employee:
    """Класс для представления сотрудника."""

    # Переменная на уровне класса для подсчета количества сотрудников
    nummer_of_employees = 0

    def __init__(self, first, last, pay):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@email.com'

        Employee.nummer_of_employees += 1

# Создаем двух сотрудников
emp_1 = Employee('Ivan', 'Ivanov', 50000)
emp_2 = Employee('Pert', 'Petrov', 60000)

# Выводим количество сотрудников
print(f'Количество сотрудников: {Employee.nummer_of_employees}')
print(dir(Employee))
print(dir(emp_1))
print(emp_2)