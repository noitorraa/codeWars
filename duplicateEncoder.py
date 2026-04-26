def duplicate_encode(word):
    return "".join(")" if word.lower().count(ch) > 1 else "(" for ch in word.lower())


def test_duplicate_encode_recede():
    assert duplicate_encode("recede") == "()()()"


def test_duplicate_encode_success():
    assert duplicate_encode("Success") == ")())())"
