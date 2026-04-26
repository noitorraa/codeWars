def square_digits(num):
    result = ""
    for x in str(num):
        result += str(int(x) ** 2)
    return int(result)


def square_digits_alternative(num):
    return int("".join(str(int(d) ** 2) for d in str(num)))


def test_square_digits():
    assert square_digits(3312) == 9914


def test_square_digits_alternative():
    assert square_digits_alternative(3312) == 9914
