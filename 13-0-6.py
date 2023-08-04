# 6. Настройка переменных окружения
# https://my.sky.pro/student-cabinet/stream-lesson/81793/theory/6

import os

print(os.getenv('EXCHANGE_RATE_API_KEY'))
# или
print(os.environ.get('USERLOGIN'))
print(os.getenv('USERPROFILE'))
print(os.environ.get('USERNAME'))
