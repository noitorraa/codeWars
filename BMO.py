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


print(basic_op("+", 4, 6))
