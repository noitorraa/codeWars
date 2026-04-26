def quarter_of(month):
    return (
        1 if 1 <= month <= 3 else 2 if 4 <= month <= 6 else 3 if 7 <= month <= 9 else 4
    )


def test_quarter_of_june():
    assert quarter_of(6) == 2


def test_quarter_of_august():
    assert quarter_of(8) == 3


def test_quarter_of_october():
    assert quarter_of(10) == 4


def test_quarter_of_april():
    assert quarter_of(4) == 2
