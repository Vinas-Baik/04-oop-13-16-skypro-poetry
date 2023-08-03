# 6. Настройка переменных окружения
# https://my.sky.pro/student-cabinet/stream-lesson/81793/theory/6

import os

print(os.getenv('USER_PASSWORD'))
# или
print(os.environ.get('USERLOGIN'))
print(os.getenv('USERPROFILE'))
print(os.environ.get('USERNAME'))
