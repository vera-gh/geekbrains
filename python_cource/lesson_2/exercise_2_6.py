from collections import OrderedDict

product_array = list()

print("Заполните информацию о товаре:")
count = 1
while True:
    product_name = input("Введите название товара >>>")
    product_price = input("Введите цену товара >>>")
    product_amount = input("Введите количество товара >>>")
    product_measure = input("Введите единицы измерения товара >>>")
    another_product = input("Добавить еще один товар ? Введите 'да' или 'нет' >>>")
    product_array.append(
        (count, {"название": product_name, "цена": product_price, "количество": product_amount, "ед.": product_measure})
    )
    if another_product == "да":
        count += 1
        continue
    else:
        break

summary = OrderedDict()
analyze_name = list()
analyze_price = list()
analyze_amount = list()
analyze_measure = list()
analyze_product = list()

for number, product in product_array:
    print(product["название"])
    analyze_name.append(product["название"])
    analyze_price.append(product["цена"])
    analyze_amount.append(product["количество"])
    analyze_measure.append(product["ед."])

summary["название"] = analyze_name
summary["цена"] = analyze_price
summary["количество"] = analyze_amount
summary["ед."] = analyze_measure

print(f"Аналитика по товарам: \n{dict(summary)}")
