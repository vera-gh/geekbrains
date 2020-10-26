""" Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее."""

from itertools import count

print("Exercise with count tool:")
for el in count(1):
    if el > 20:
        break
    else:
        print(el)

from itertools import cycle

print("Exercise with cycle tool:")
count = 0
my_list = [1, 3, 5, 7, 9]
for el in cycle(my_list):
    print(el)
    count += 1
    if count > 20:
        break
