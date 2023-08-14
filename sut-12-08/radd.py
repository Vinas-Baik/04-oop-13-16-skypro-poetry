class Summary:

    def __init__(self, arg=1, error_add=None):
        self.arg = arg
        self.error_add = error_add

    def my_add(self, var1, var2, type_add, type_oper):
        # print(f'{type_add}')
        # print(f'{type_add}-> {var1} + {var2}')

        temp_error = None

        if isinstance(var1, int | float):
            temp_self = var1
        elif isinstance(var1, Summary):
            temp_error = var1.error_add
            temp_self = var1.arg
        else:
            temp_self = None

        if isinstance(var2, int | float):
            temp_other = var2
        elif isinstance(var2, Summary):
            if temp_error == None:
                temp_error = var2.error_add

            temp_other = var2.arg
        else:
            temp_other = None

        # print(f'{type_add}-> {temp_self} + {temp_other} ({temp_error})')

        if temp_self != None and temp_other != None and temp_error == None:
            # print(f'{type_add}-> {temp_other + temp_self}')
            if type_oper == '+':
                return Summary(temp_self + temp_other, temp_error)
            elif type_oper == '-':
                return Summary(temp_self - temp_other, temp_error)
            elif type_oper == '*':
                return Summary(temp_self * temp_other, temp_error)
        else:
            # print(f'{type_add}-> ошибка {type_add}')
            return Summary(0, f'ошибка {type_add}')

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

# print(sum([s1, s2, s3]))
# print(sum([s1, s2, 2, 10, 15, s1]))
# print(s1 + s2 + s3)
# print(10 + s1 + s1)

s4 = s2 * s2 * 2 + s1 + 100.012 - 10.002


if s4.error_add == None:
    print(s4.arg)
else:
    print(s4.error_add)