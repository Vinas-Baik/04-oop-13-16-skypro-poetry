# Библиотека json входит в стандартную библиотеку Python, поэтому ее установка не требуется.
#
# Основные методы
# json.loads()  — преобразует строку JSON в объект Python.
# json.dumps()  — преобразует объект Python в строку JSON.
# json.load()   — читает данные из файла в формате JSON и возвращает объект Python.
# json.dump()   — записывает данные в файл в формате JSON.

import json

# Преобразование объекта Python в строку JSON
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(my_dict)
print(json_string)

# Преобразование строки JSON в объект Python
json_string = '{"name": "John", "age": 30, "city": "New York"}'
my_dict = json.loads(json_string)
print(my_dict)

# Запись данных в файл в формате JSON
with open('data.json', 'w', encoding='UTF-8') as f:
    json.dump(json_string, f)
    # json.dump(json_string, f)

# Чтение данных из файла и преобразование в объект Python
with open('data.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)
print(data)

