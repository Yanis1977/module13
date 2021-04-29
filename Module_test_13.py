price = 0
quantity = int(input("Введите количество билетов: "))
for i in range(quantity):
    age = int(input("Введите возраст посетителей: "))
    if 0 <= age <= 17:
        price += 0
    elif 18 <= age <= 24:
        price += 990
    elif age >= 25:
        price += 1390
print("Цена без учёта скидки: ", price)
if quantity > 3:
    discount_price = price - (price / 10)
    print("Итоговая цена: ", discount_price)





