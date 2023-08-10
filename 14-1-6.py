class MyOpen:
    def __init__(self, filename, mode='r'):
        """
        Класс, который создает объект, который можно использовать
        вместо open(), чтобы автоматически закрывать файл.
        :param filename: имя файла
        :param mode: режим открытия файла (по умолчанию 'r')
        """
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        """
        Метод, который вызывается при входе в блок контекста.
        Он открывает файл и возвращает файловый дескриптор.
        :return: файловый дескриптор
        """
        self.fp = open(self.filename, self.mode)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Метод, который вызывается при выходе из блока контекста.
        Он закрывает файл.

        """
        # exc_type, exc_val, exc_tb  в методе __exit__  — это дополнительные
        # параметры, в которые записывается информация об исключении, если
        # исключение возникает. В простых примерах не используется.
        self.fp.close()


class MyContext:
    def __enter__(self):
        print("Вход в класс - Entering context")

    def __exit__(self, type, value, traceback):
        print("Выход из класса - Exiting context")


# Напишите код, который создает контекстный менеджер, используя магические методы __enter__
#  и __exit__, который будет перехватывать все исключения, которые возникают внутри контекста, и выводить на экран сообщение "An error occurred" при возникновении исключения.

class MyContext1:

    def __enter__(self):
        return self

def __exit__(self, type, value, traceback):

    if type:
        print("An error occurred")
    return True


#  НАЧАЛО ПРОГРАММЫ э
#
with MyContext():
    print("Просто так")

print()

with MyOpen('text.txt', 'r') as fp:  # Открываем файл
    print(fp.read())  # Читаем файл
