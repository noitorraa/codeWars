import string

pangrams = [
    "The quick brown fox jumps over the lazy dog.",
    "Cwm fjord bank glyphs vext quiz",
    "Pack my box with five dozen liquor jugs.",
    "How quickly daft jumping zebras vex.",
    "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ",
    "wefwfvt",
]


def is_pangram(st):
    alphabet = set(string.ascii_lowercase)
    return True if alphabet <= set(st.lower()) else False


def test_is_pangram():
    assert is_pangram("The quick brown fox jumps over the lazy dog.") == True
    assert is_pangram("Cwm fjord bank glyphs vext quiz") == True
    assert is_pangram("Pack my box with five dozen liquor jugs.") == True
    assert is_pangram("How quickly daft jumping zebras vex.") == True
    assert is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ") == True
    assert is_pangram("wefwfvt") == False
