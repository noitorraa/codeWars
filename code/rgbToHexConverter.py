def rgb(r, g, b):
    r, g, b = (max(0, min(255, x)) for x in (r, g, b))
    return f"{r:02X}{g:02X}{b:02X}"


def test_rgb_black():
    assert rgb(0, 0, 0) == "000000"


def test_rgb_small_values():
    assert rgb(1, 2, 3) == "010203"


def test_rgb_white():
    assert rgb(255, 255, 255) == "FFFFFF"


def test_rgb():
    assert rgb(-20, 275, 125) == "00FF7D"
