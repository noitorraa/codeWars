def bool_to_word(boolean):
    return "Yes" if boolean else "No"


def test_bool_to_word_true():
    assert bool_to_word(True) == "Yes"


def test_bool_to_word_false():
    assert bool_to_word(False) == "No"
