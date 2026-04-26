def zero(f=None):
    return 0 if f is None else f(0)


def one(f=None):
    return 1 if f is None else f(1)  # your code here


def two(f=None):
    return 2 if f is None else f(2)  # your code here


def three(f=None):
    return 3 if f is None else f(3)  # your code here


def four(f=None):
    return 4 if f is None else f(4)  # your code here


def five(f=None):
    return 5 if f is None else f(5)


def six(f=None):
    return 6 if f is None else f(6)  # your code here


def seven(f=None):
    return 7 if f is None else f(7)


def eight(f=None):
    return 8 if f is None else f(8)  # your code here


def nine(f=None):
    return 9 if f is None else f(9)  # your code here


def plus(y):
    return lambda x: x + y  # your code here


def minus(y):
    return lambda x: x - y  # your code here


def times(y):
    return lambda x: x * y  # your code here


def divided_by(y):
    return lambda x: x // y


def test_seven_times_five():
    assert seven(times(five())) == 35


def test_four_plus_nine():
    assert four(plus(nine())) == 13


def test_eight_minus_three():
    assert eight(minus(three())) == 5


def test_six_divided_by_two():
    assert six(divided_by(two())) == 3
