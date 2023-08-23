# Описание задачи
# 📮 Для существующего кода необходимо сделать рефакторинг с использованием принципов SOLID.
#
# Есть существующий код системы продаж, представленный классом Order (Заказ).
#
# В этом классе содержатся:
# списки товаров в заказе (items)
# количество каждого товара (quantities)
# цена товара (prices)
# статус заказа (status)
# В классе Order есть методы для:
# добавления товара в заказ (add_item)
# подсчета стоимости заказа (total_price)
# оплаты заказа (pay)

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

 def pay(self, payment_type, security_code):
  if payment_type.lower().strip() == "debit":
   print("Обработка дебетового типа платежа")
   print(f"Проверка кода безопасности: {security_code}")
   self.status = "paid"
  elif payment_type.lower().strip() == "credit":
   print("Обработка кредитного типа платежа")
   print(f"Проверка кода безопасности: {security_code}")
   self.status = "paid"
  else:
   raise Exception(f"Неизвестный способ оплаты: {payment_type}")


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
try:
 order.pay("debit", "0372846")
except Exception as t_err:
 print(t_err)
try:
  order.pay("debit_1", "0372846")
except Exception as t_err:
 print(t_err)