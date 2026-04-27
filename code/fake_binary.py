def fake_bin(x):
    result = ""
    for i in x:
        if int(i) >= 5:
            result += "1"
        else:
            result += "0"
    return result


def fake_bin_alternative(x):
    return "".join("0" if c < "5" else "1" for c in x)


def test_fake_bin():
    assert fake_bin("45385593107843568") == "01011110001100111"


def test_fake_bin_alternative():
    assert fake_bin_alternative("45385593107843568") == "01011110001100111"
