def lovefunc(flower1, flower2):
    if (flower1 % 2 == 0 and flower2 % 2 != 0) or (
        flower1 % 2 != 0 and flower2 % 2 == 0
    ):
        return True
    else:
        return False


def lovefunc_alternative(flower1, flower2):
    return (flower1 + flower2) % 2


def lovefunc_alternative2(flower1, flower2):
    return flower1 % 2 != flower2 % 2


print(lovefunc(1288, 1222))
