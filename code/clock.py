def past(h, m, s):
    return h * 3600000 + m * 60000 + s * 1000


def test_past():
    assert past(1, 1, 1) == 3661000
