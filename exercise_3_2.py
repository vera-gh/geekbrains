def user_data(user_name=None, user_surname=None, user_bd=None, user_city=None, user_email=None, user_number=None):
    return print(f"{user_name}, {user_surname}, {user_bd}, {user_city}, {user_email}, {user_number}")
user_name = input("Ваше имя>>> ")
user_surname = input("Ваша фамилия>>> ")
user_bd = input("Год Вашего рождения>>> ")
user_city = input("Ваш город>>> ")
user_email = input("Ваш email>>> ")
user_number = input("Номер телефона>>> ")
user_data(user_name=user_name, user_surname=user_surname, user_bd=user_bd,user_city=user_city,user_email=user_email, user_number=user_number)

