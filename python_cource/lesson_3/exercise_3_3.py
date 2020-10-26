def max_element_from_list(numbers_list):
    """Возвращаем максимальное значение из списка"""
    return max(numbers_list)


def my_func(arg_1, agr_2, arg_3):
    args_list = [arg_1, agr_2, arg_3]
    result_list = []
    for _ in range(2):
        max_elem = max_element_from_list(args_list)
        args_list.remove(max_elem)
        result_list.append(max_elem)

    return sum(result_list)


test_case_1 = my_func(1, 2, 3)
print(test_case_1)
test_case_2 = my_func(6, 5, 4)
print(test_case_2)
test_case_3 = my_func(7, 9, 8)
print(test_case_3)
