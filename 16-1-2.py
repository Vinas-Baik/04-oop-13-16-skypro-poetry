try:
    a, b = map(int, input().split())
    result = a / b
    print(result)
except ZeroDivisionError as e:
    print('деление на 0')
    print(e.args)
except ValueError as e:
    print('ошибка типа')
    print(e.args)

