import string_calculator

def test_empty_str():
    assert string_calculator.Add("") == 0

def test_single_number():
    assert string_calculator.Add("1") == 1


def test_two_numbers():
    assert string_calculator.Add("1,2") == 3