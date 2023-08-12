class Summary:

    def __init__(self, arg=1):
        self.arg = arg

    def __radd__(self, other):
        if isinstance(other, int | float):
            return other + self.arg
        elif isinstance(other, Summary):
            return other.arg + self.arg

        print('ошибка сложения radd')

    def __add__(self, other):
        if isinstance(other, int | float):
            return other + self.arg
        elif isinstance(other, Summary):
            return other.arg + self.arg

        print('ошибка сложения add')


s1 = Summary()
s2 = Summary(5)
s3 = Summary(10)

print(sum([s1, s2, s3]))
print(sum([s1, s2, 2, 10, 15, s1]))
print(s1 + s2 + s3)
print(10 + s1 + s1)