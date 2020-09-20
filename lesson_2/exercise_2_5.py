my_list = [9, 7, 7, 5, 4, 4, 3, 2]

user_number = int(input(" Введите число >>>"))

if user_number not in my_list:
    for index, number in enumerate(my_list):
        if user_number > number:
            my_list.insert(index, user_number)
            break
        else:
            my_list.append(user_number)
            break
else:
    for index, number in enumerate(my_list):
        if user_number == number:
            my_list.insert(index + 1, user_number)
            break

print(my_list)
