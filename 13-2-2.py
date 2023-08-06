# Объявляем функцию printing,
# которая принимает на вход другую функцию function
def printing(function):
    # Внутри функции printing объявляем функцию inner,
    # которая принимает любое количество аргументов
    def inner(*args, **kwargs):
        # Вызываем функцию function с переданными аргументами
        # и сохраняем результат в переменную result
        result = function(*args, **kwargs)
        # result = 1
        # Выводим на экран строку с результатом
        print('result =', result)
        # Возвращаем результат вызова функции function
        return result
    # Возвращаем функцию inner в качестве результата работы функции printing
    return inner

# Объявляем функцию add_one, которая принимает на вход число x
# и возвращает x + 1
# Декорируем функцию add_one с помощью функции printing
@printing
def add_one(x):
    return x + 1

# Декорируем функцию add_one с помощью функции printing
# add_one = printing(add_one)

# Вызываем декорированную функцию add_one с аргументом 10
# и сохраняем результат в переменную y
add_one(15)
y = add_one(10)
# => result = 11
print(y)
# 11