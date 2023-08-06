# https://my.sky.pro/student-cabinet/stream-lesson/55019/theory/5


import pytest
# from src.class_testing import PositiveNumber


class PositiveNumber:
    """Класс для хранения неотрицательного целого числа."""

    def __init__(self, value):
        """Экземпляр класса инициализируется только целым неотрицательным числом."""
        if not isinstance(value, int):
            raise ValueError('Значение должно быть числом.')
        elif value <= 0:
            raise ValueError('Число должно быть неотрицательным.')
        self.value = value

    def increment(self):
        """Метод для увеличения значения числа на единицу."""
        self.value += 1

    def get_value(self):
        """Метод для получения значения числа."""
        return self.value


@pytest.fixture
def number5():
    return PositiveNumber(5)


def test_positive_number_init(number5):
    """Когда мы создаем экземпляр класса со значением Х, то get_value вернет нам Х."""
    assert number5.get_value() == 5


def test_positive_number_increment(number5):
    """Когда мы создаем класс со значением Х, затем вызываем increment, то get_value вернет нам Х + 1."""
    number5.increment()
    assert number5.get_value() == 6


def test_positive_number_not_int():
    """Когда мы создаем экземпляр класса с нечисловым значением, вернется ошибка."""
    with pytest.raises(ValueError):
        PositiveNumber('abc')


def test_positive_number_negative():
    """Когда мы создаем экземпляр класса с числовым, но отрицательным значением, вернется ошибка."""
    with pytest.raises(ValueError):
        PositiveNumber(-5)