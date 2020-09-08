seasons = {"зима": [12, 1, 2], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}
month_number = int(input("Введите номер месяца >>>"))
for key, value in seasons.items():
    if month_number in value:
        print(key)
        break
print("Нет такого месяца")

