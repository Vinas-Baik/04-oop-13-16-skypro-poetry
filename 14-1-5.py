class EvenRange:
    """Итератор, возвращающий только четные числа в диапазоне от 0 до stop."""

    def __init__(self, stop):
        """Инициализирует итератор.

        Args:
            stop (int): Верхняя граница диапазона чисел.

        Raises:
            ValueError: Если переданное значение не является целым неотрицательным числом.
        """
        if not isinstance(stop, int):
            raise ValueError('Число должно быть целым')
        if stop < 0:
            raise ValueError('Число должно быть неотрицательным')
        self.stop = stop

    def __iter__(self):
        """Возвращает итератор."""
        self.current_value = -2
        return self

    def __next__(self):
        """Возвращает следующее четное число в диапазоне.

        Returns:
            int: Следующее четное число.

        Raises:
            StopIteration: Если достигнута верхняя граница диапазона.
        """
        if self.current_value + 2 < self.stop:
            self.current_value += 2
            return self.current_value
        else:
            raise StopIteration

r = EvenRange(20)
print(list(r))
# [0, 2, 4, 6, 8]
for i in r:
    print(i)
