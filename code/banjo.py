def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


def test_are_you_playing_banjo_true():
    assert are_you_playing_banjo("Richard") == "Richard plays banjo"


def test_are_you_playing_banjo_false():
    assert are_you_playing_banjo("ichard") == "ichard does not play banjo"
