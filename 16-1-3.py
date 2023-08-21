class Exp:

    def func1(self):
        try:
            self.func2()
        except ZeroDivisionError:
            print('Ошибка в func1()')
        else:
            print('прошел else в func1()')

        print('Штатное завершение func1()')

    def func2(self):
        try:
            self.func3()
        except ZeroDivisionError:
            print('Ошибка в func2()')
        else:
            print('прошел else в func2()')
        print('Штатное завершение func2()')

    def func3(self):
        try:
            print(100 / 0)
        except ZeroDivisionError:
            print('Ошибка в func3()')
        else:
            print('прошел else в func3()')
        print('Штатное завершение func3()')


ob = Exp()

try:
    ob.func1()
except ZeroDivisionError:
    print('Ошибка где-то в классе Exp.')
else:
    print('нет ошибки в классе Exp')

print("Выход.")