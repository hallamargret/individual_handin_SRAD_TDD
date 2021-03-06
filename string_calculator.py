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
    delim = ",|\n"
    if numbers[0] == "/":
        #numbers have different delimiter, find it in the delimiter handler
        numbers_list = delimiter_handler(numbers)
    else:
        #numbers have "normal" delimeters, comma and a whitespace
        numbers_list = re.split(delim, numbers)

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


def delimiter_handler(numbers):
    #finds the new delimiter and splits numbers so we get a list of the numbers
    delimstart = 2
    delim = numbers[delimstart]
    while numbers[(delimstart + 1)] != "\n":
        delim += numbers[delimstart]
        delimstart += 1
    numbers_list = numbers.split("\n")[1].split(delim)
    return numbers_list
