def get_age(age):
    return int(list(age)[0])


def get_age_alternative(age):
    return int(age[0])


def test_get_age():
    assert get_age("2 years old") == 2


def test_get_age_alternative():
    assert get_age_alternative("2 years old") == 2
