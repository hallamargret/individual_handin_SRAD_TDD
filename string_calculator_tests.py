import string_calculator

def test_empty_str():
    assert string_calculator.Add("") == 0

def test_single_number():
    assert string_calculator.Add("1") == 1


def test_two_numbers():
    assert string_calculator.Add("1,2") == 3


def test_unknown_numbers_of_numbers():
    assert string_calculator.Add("1,2,3,4,5") == 15


def test_new_lines_as_a_delimiter_between_nums():
    assert string_calculator.Add("1\n2,3") == 6
