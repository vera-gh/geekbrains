def my_func(positive, negative):
    extent_number = abs(negative)
    var_positive = int(positive)
    result = 0
    for extent in range(1, extent_number):
        result = var_positive * positive
        var_positive = result

    return 1 / result


test_case_1 = my_func(2, -3)
assert test_case_1 == 0.125
print(test_case_1)

test_case_2 = my_func(2, -4)
assert test_case_2 == 0.0625
print(test_case_2)

test_case_3 = my_func(5, -2)
assert test_case_3 == 0.04
print(test_case_3)
