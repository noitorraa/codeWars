def square_digits(num):
    result = ""
    for x in str(num):
        result += str(int(x) ** 2)
    return int(result)


def square_digits_alternative(num):
    return int("".join(str(int(d) ** 2) for d in str(num)))


print(square_digits(3312))
