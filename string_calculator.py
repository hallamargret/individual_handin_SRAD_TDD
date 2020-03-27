def Add(numbers):
    #empty string
    if numbers == "":
        return 0
    elif len(numbers) == 1:
        return int(numbers)
    else:
        the_sum = 0
        numbers_list = numbers.split(",")
        for num in numbers_list:
            the_sum += int(num)
        return the_sum
        