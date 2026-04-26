def basic_op(operator, value1, value2):
    match operator:
        case "+":
            return value1 + value2
        case "-":
            return value1 - value2
        case "*":
            return value1 * value2
        case "/":
            return value1 / value2


def test_basic_op_add():
    assert basic_op("+", 4, 6) == 10


def test_basic_op_sub():
    assert basic_op("-", 4, 6) == -2


def test_basic_op_mul():
    assert basic_op("*", 4, 6) == 24


def test_basic_op_div():
    assert basic_op("/", 4, 6) == 0.6666666666666666
