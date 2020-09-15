def number_division(first_arg, second_arg):

    if second_arg > 0:
        return first_arg / second_arg
    else:
        print("На ноль делить нельзя!")
        return None


a = int(input("Введите делимое>>> "))
b = int(input("Введите делитель>>> "))
result = number_division(a, b)
print(result)
