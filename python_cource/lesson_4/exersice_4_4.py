"""Представлен список чисел. Определить элементы списка,
не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести
в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор."""
my_list = [4,5,5,3,2,7,7,8,8,9,10,22,10,23]
origin_list = [el for el in my_list if my_list.count(el) < 2]
print(origin_list)
