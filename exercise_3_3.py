# def my_func(arg_1, arg_2, arg_3):
#     result_list = []
#     const_args_list = [arg_1, arg_2, arg_3]
#     var_args_list = [arg_1, arg_2, arg_3]
#     max_arg = max(const_args_list)
#     for element in range(len(const_args_list)):
#         if max_arg == const_args_list[element]:
#             result_list.append(const_args_list[element])
#             var_args_list.remove(const_args_list[element])
#             if len(var_args_list) == 1:
#                 break
#             else:
#                 # result_list.append(max_element)
#                 max_arg = max(var_args_list)
#         else:
#             continue
#     if len(result_list) != 2:
#
#     return sum(result_list)

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
