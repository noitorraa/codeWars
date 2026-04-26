def rgb(r, g, b):
    return ((1 << 24) + (r << 16) + (g << 8) + b).to_bytes(4, "big")[1:].hex().upper()


def test_rgb_black():
    assert rgb(0, 0, 0) == "000000"


def test_rgb_small_values():
    assert rgb(1, 2, 3) == "010203"


def test_rgb_white():
    assert rgb(255, 255, 255) == "FFFFFF"
