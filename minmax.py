def high_and_low(numbers):
    numbers_list = [int(x) for x in numbers.split()]
    return "".join(str(max(numbers_list)) + " " + str(min(numbers_list)))


def test_high_and_low():
    assert high_and_low("8 3 1 4 9 84 19 90 -1 -5 993 20 -2 4") == "993 -5"
