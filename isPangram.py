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


for i in pangrams:
    print(is_pangram(i))
