class ShellScriptError(Exception):
    """Общий класс исключения для скриптов"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка скрипта.'

    def __str__(self):
        return self.message


class ShellScriptEmpty(ShellScriptError):
    """Класс исключения при отсутствии кода скрипта"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл пустой.'


class ShellScriptShebang(ShellScriptError):
    """Класс исключения при отсутствии shebang"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'В файле отсутствует shebang.'


class ShellScript:
    """Класс для работы с шелл-скриптами."""

    def __init__(self, script: str):
        script = script.strip()
        if not script:  # Если скрипт пустой
            raise ShellScriptEmpty
        elif script[0:2] != '#!':  # Если отсутствует shebang
            raise ShellScriptShebang
        else:
            self.script = script

    def evaluate(self):
        # Код исполнения скрипта
        pass


for content in ('', '#!/bin/bash', '#/bin/bash','    #!     ', '    '):
    print(content, end=' - ')
    try:
        script = ShellScript(content)
    except ShellScriptEmpty:
        print('Отсутствует текст скрипта.')
    except ShellScriptShebang:
        print('Добавьте шебанг #! в начало скрипта.')
    except ShellScriptError:
        print('Ошибка при работе скрипта.')
    else:
        print('Все хорошо')