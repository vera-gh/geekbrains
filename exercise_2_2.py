user_list = input("Введите последовательность значений, разделенных пробелом>>>")

result_list = user_list.split()

print(f"Исходный список значений: {result_list}")

for num in range(0, len(result_list), 2):
    try:
        result_list[num], result_list[num + 1] = result_list[num + 1], result_list[num]
    except:
        pass

print(f"Результат: {result_list}")
