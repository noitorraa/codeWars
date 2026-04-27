def double_char(s):
    return "".join(f * 2 for f in s)


def test_double_char():
    assert double_char("String") == "SSttrriinngg"
