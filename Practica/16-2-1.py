# Описание задачи
#
# Для существующего кода необходимо сделать рефакторинг с использованием принципов SOLID.
# S - Принцип единой ответственности (Single Responsibility)
#     Описание: каждый класс должен иметь только одну зону ответственности.
#     Подход к реализации: выделите зоны ответственности в отдельные классы.
#
# O - Принцип открытости/закрытости (Open/Closed)
#     Описание: программные сущности (классы, модули, функции и т. п.) должны
#     быть открыты для расширения, но закрыты для изменения.
#     Подход к реализации: используйте абстрактные классы.
#     Они могут определить, какие подклассы требуются,
#     и усилить принцип единой ответственности, разделив обязанности кода.
#
# L - Принцип подстановки Барбары Лисков (Liskov Substitution)
#     Описание: если класс Parent является родительским классу Child,
#     то любые методы класса Parent могут заменяться методами класса Child
#     без возникновения ошибок в программе.
#     Подход к реализации: используйте аргументы конструктора,
#     чтобы обеспечить гибкость наследования.
#
# I - Принцип разделения интерфейсов (Interface Segregation)
#     Описание: сделайте интерфейсы (родительские абстрактные классы) более
#     конкретными, а не общими.
#     Подход к реализации: при необходимости создайте дополнительные
#     интерфейсы (классы).
#
# D - Принцип инверсии зависимостей (Dependency Inversion)
#     Описание: сделать классы зависимыми от абстрактных классов,
#     а не от обычных классов.
#     Подход к реализации: наследовать классы от абстрактных классов.
#

from abc import ABC, abstractmethod

class Order:

 def __init__(self):
  self.items = []
  self.quantities = []
  self.prices = []
  self.status = "open"

 def add_item(self, name, price, quantity=1):
  self.items.append(name)
  self.quantities.append(quantity)
  self.prices.append(price)

 def total_price(self):
  return sum(quantities * prices for quantities, prices in
             zip(self.quantities, self.prices))

 def __str__(self):
  return '\n'.join(f'{item}, стоимостью {price} руб. в количестве {quantitie} шт.'
                   for item, quantitie, price in zip(self.items, self.quantities, self.prices))

class Authorizer(ABC):
 @abstractmethod
 def is_authorized(self) -> bool:
  pass


class AuthorizerSMS(Authorizer):

 def __init__(self):
  self.authorized = False

 def verify_code(self, code):
  print(f"Верификация SMS кода {code}")
  self.authorized = True

 def is_authorized(self) -> bool:
  return self.authorized


class AuthorizerRobot(Authorizer):

 def __init__(self):
  self.authorized = False

 def not_a_robot(self):
  self.authorized = True

 def is_authorized(self) -> bool:
  return self.authorized


class PaymentProcessor(ABC):

 @abstractmethod
 def pay(self, order):
  pass


class DebitPaymentProcessor(PaymentProcessor):

 def __init__(self, security_code, authorizer: Authorizer):
  self.security_code = security_code
  self.authorizer = authorizer

 def pay(self, order):
  if not self.authorizer.is_authorized():
   raise Exception("Не авторизован")
  print("Обработка дебетового типа платежа")
  print(f"Проверка кода безопасности: {self.security_code}")
  order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

 def __init__(self, security_code):
  self.security_code = security_code

 def pay(self, order):
  print("Обработка кредитного типа платежа")
  print(f"Проверка кода безопасности: {self.security_code}")
  order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

 def __init__(self, email_address, authorizer: Authorizer):
  self.email_address = email_address
  self.authorizer = authorizer

 def pay(self, order):
  if not self.authorizer.is_authorized():
   raise Exception("Не авторизован")
  print("Обработка paypal платежа")
  print(f"Использование адреса электронной почты: {self.email_address}")
  order.status = "paid"

# Создаем заказ
order = Order()
# Добавляем товары в заказ
order.add_item("Клавиатура", 2500)
order.add_item("SSD", 7500)
order.add_item("USB-кабель", 250, 2)
# Печатаем стоимость заказа
print(order)
print(f'Общая сумма заказа = {order.total_price()} руб.')
# Оплачиваем заказ

authorizer = AuthorizerRobot()
# authorizer.verify_code(465839)
authorizer.not_a_robot()
processor = PaypalPaymentProcessor("hi@company.com", authorizer)
processor.pay(order)
