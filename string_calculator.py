import re

class NegativeNumError(Exception):
    pass

def Add(numbers):
    #empty string
    if numbers == "":
        return 0
    elif len(numbers) == 1:
        return int(numbers)
    else:
        return many_numbers(numbers)


def many_numbers(numbers):
    the_sum = 0
    negative_num_str = "Negatives not allowed: "
    numbers_list = re.split(",|\n", numbers)
    for num in numbers_list:
        if int(num) <= 1000 and int(num) > 0:
            the_sum += int(num)
        elif int(num) < 0:
            if negative_num_str == "Negatives not allowed: ":
                negative_num_str += num
            else:
                negative_num_str += ("," + num)

    if negative_num_str != "Negatives not allowed: ":
        raise NegativeNumError(negative_num_str)
        
    return the_sum