print("\t\tНАЧАЛО программы\n")
is_error = True
while is_error:
    try:
        a, b = map(int, input('Введите 2 целых числа через пробел: ').split())
        result = a / b

    except ZeroDivisionError as temp_e:
        print('деление на 0')
        print(temp_e.args)

    except TypeError as temp_e:
        print('ошибка типа')
        print(temp_e.args)

    except Exception as temp_e:
        print('Общая ошибка')
        print(temp_e)

    else:
        is_error = False
        print(f'Результат деления {a} на {b} = {result}')

    finally:
        if not is_error:
            print("\t\tКОНЕЦ программы\n")
