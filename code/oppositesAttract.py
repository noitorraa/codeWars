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


def test_lovefunc_true():
    assert lovefunc(1288, 1223) == True


def test_lovefunc_false():
    assert lovefunc(1288, 1288) == False


def test_lovefunc_alternative_true():
    assert lovefunc_alternative(1288, 1223) == 1


def test_lovefunc_alternative_false():
    assert lovefunc_alternative(1288, 1288) == 0


def test_lovefunc_alternative2_true():
    assert lovefunc_alternative2(1288, 1223) == True


def test_lovefunc_alternative2_false():
    assert lovefunc_alternative2(1288, 1288) == False
