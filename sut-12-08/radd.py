class Summary:

    def __init__(self, arg=1):
        self.arg = arg

    def my_add(self, var1, var2, type_add, type_oper):
        # print(f'{type_add}')
        # print(f'{type_add}-> {var1} + {var2}')

        if isinstance(var1, int | float):
            temp_self = var1
        elif isinstance(var1, Summary):
            temp_self = var1.arg
        else:
            temp_self = None

        if isinstance(var2, int | float):
            temp_other = var2
        elif isinstance(var2, Summary):
            temp_other = var2.arg
        else:
            temp_other = None

        # print(f'{type_add}-> {temp_self} + {temp_other}')

        if temp_self != None and temp_other != None:
            print(f'{type_add}-> {temp_other + temp_self}')
            if type_oper == '+':
                return Summary(temp_self + temp_other)
            elif type_oper == '-':
                return Summary(temp_self - temp_other)
            elif type_oper == '*':
                return Summary(temp_self * temp_other)
        else:
            # print(f'{type_add}-> ошибка {type_add}')
            raise ValueError(f'ошибка {type_add}')

    def __radd__(self, other):
        return self.my_add(self, other, 'сложения', '+')

    def __add__(self, other):
        return self.my_add(self, other, 'сложения', '+')

    def __sub__(self, other):
        return self.my_add(self, other, 'вычитания', '-')

    def __rsub__(self, other):
        return self.my_add(self, other, 'вычитания', '-')

    def __mul__(self, other):
        return self.my_add(self, other, 'умножения', '*')

    def __rmul__(self, other):
        return self.my_add(self, other, 'умножения', '*')




s1 = Summary()
s2 = Summary(5)
s3 = Summary(10)

try:
    s4 = s2 * s2 * 2 + s1 + 100.012 - 10.002 * '10'
    print(s4.arg)
except ValueError as v_err:
    print(v_err.args)
except TypeError as t_err:
    print(t_err.args)

