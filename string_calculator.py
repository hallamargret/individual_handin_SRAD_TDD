import re

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
    numbers_list = re.split(",|\n", numbers)
    for num in numbers_list:
        if int(num) <= 1000:
            the_sum += int(num)
    return the_sum