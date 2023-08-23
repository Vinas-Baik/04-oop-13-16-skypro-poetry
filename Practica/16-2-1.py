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


class PaymentProcessor(ABC):

 @abstractmethod
 def pay(self, order):
  pass

class DebitPaymentProcessor(PaymentProcessor):

 def __init__(self, security_code):
  self.security_code = security_code

 def pay(self, order):
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

 def __init__(self, email_address):
  self.email_address = email_address

 def pay(self, order):
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
# try:
#  order.pay("debit", "0372846")
# except Exception as t_err:
#  print(t_err)
# try:
#   order.pay("debit_1", "0372846")
# except Exception as t_err:
#  print(t_err)

processor = DebitPaymentProcessor("0372846")
processor.pay(order)
processor = CreditPaymentProcessor("7383903")
processor.pay(order)

processor = PaypalPaymentProcessor("hi@company.com")
processor.pay(order)