class StripChars:
    """Класс, удаляющий определенные символы из строки"""
    def __init__(self, chars):
        """Инициализация крайних рядом стоящих символов для удаления"""
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        """Удаление крайних рядом стоящих  символов из строки"""
        return args[0].strip(self.__chars)

# Cоздаем два экземпляра класса StripChars: st1 и st2
st1 = StripChars('!"№;%')
st2 = StripChars('_')

print(st1('!"№Attention!;%№'))
# Attention
print(st1('_Attention_'))
# _Attention_
print(st2('_Attention_'))
# Attention