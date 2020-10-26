beginning_distance = int(input("Введите начальное значение дистанции >>>"))
result_distance = int(input("Введите значение желаемой дистанции >>>"))
counter = 1
while beginning_distance < result_distance:
    regular_addition = beginning_distance / 100 * 10
    beginning_distance = beginning_distance + regular_addition
    counter += 1

print(f"Спортсмен достигнет результата не менее {result_distance} км на {counter} день тренировок.")
