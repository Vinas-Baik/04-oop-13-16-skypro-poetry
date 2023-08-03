# Библиотека datetime является частью стандартной библиотеки Python, поэтому установка не требуется.
#
# Основные методы
# datetime.datetime.now()                           — возвращает текущую дату и время.
# datetime.datetime.strptime(date_string, format)   — преобразует строку в объект datetime в соответствии с заданным форматом.
# datetime.datetime.strftime(format)                — преобразует объект datetime в строку в соответствии с заданным форматом.
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)    — представляет собой интервал времени, который можно добавлять или вычитать из объектов datetime.
# datetime.datetime.replace(year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, tzinfo=None, *fold=0) — возвращает новый объект datetime с измененными атрибутами.


import datetime

# Получение текущей даты и времени
now = datetime.datetime.now()
print(now)

# Преобразование строки в объект datetime
date_string = '2022-12-31'
date_format = '%Y-%m-%d'
date = datetime.datetime.strptime(date_string, date_format)
print(date)

# Преобразование объекта datetime в строку
date_string = date.strftime(date_format)
print(date_string)

# Работа с интервалами времени
delta = datetime.timedelta(days=7)
print(now + delta)

# Замена атрибутов объекта datetime
new_date = date.replace(year=2023)
print(new_date)