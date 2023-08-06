# Полиморфизм
# Полиморфизм — возможность обработки разных типов данных, т. е. принадлежащих к разным классам,
# с помощью одной и той же функции или метода.

class JavaDeveloper:
    """Класс для представления Java-разработчиков."""

    def __init__(self, name):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name

    def info(self):
        """Метод для печати информации о Java-разработчике."""
        print(f'I am {self.name} - Java developer.')

    def code(self):
        """Метод для программирования на языке Java."""
        print("class HelloWorld { public static void main(String[] args)...")


class PythonDeveloper:
    """Класс для представления Python-разработчиков."""

    def __init__(self, name):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name

    def info(self):
        """Метод для печати информации о Python-разработчике."""
        print(f'I am {self.name} - Python developer.')

    def code(self):
        """Метод для программирования на языке Python."""
        print("print('Hello, World!')")


# Создаем экземпляры разных классов
dev1 = JavaDeveloper('Ivan')
dev2 = PythonDeveloper('Petr')

# Но работаем с ними единым образом
for developer in (dev1, dev2):
    developer.info()  # Вызов метода info()
    developer.code()  # Вызов метода code()
    print()