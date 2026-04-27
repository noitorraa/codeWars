def get_count(sentence):
    return sum(sentence.count(v) for v in "aeiou")


def test_get_count():
    assert get_count("aeiouynnjcda") == 6
