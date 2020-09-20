user_value = input("Введите любое целое положительное число >>>")

max_number = 9

while max_number > 0:
    if str(max_number) in str(user_value):
        print(f"Максимальная цифра: {max_number}")
        break
    else:
        max_number -= 1
        continue
